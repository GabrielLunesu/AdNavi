#!/usr/bin/env python3
"""Test script for Google OAuth endpoints.

WHAT:
    Tests the Google OAuth authorize endpoint and validates configuration.
    
WHY:
    Ensures OAuth endpoints are properly configured before manual testing.

USAGE:
    python test_google_oauth.py
    
    Requires:
    - Backend API running on http://localhost:8000
    - Valid user credentials (or register a test user first)
    - Environment variables: GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET (optional for basic tests)
"""

import os
import sys
import httpx
import json
from urllib.parse import urlparse, parse_qs

API_BASE = os.getenv("API_BASE", "http://localhost:8000")
TEST_EMAIL = os.getenv("TEST_EMAIL", "test@example.com")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "password123")


def test_health():
    """Test API health endpoint."""
    print("🔍 Testing API health...")
    try:
        response = httpx.get(f"{API_BASE}/health", timeout=5.0)
        if response.status_code == 200:
            print("✅ API is healthy")
            return True
        else:
            print(f"❌ API health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API health check failed: {e}")
        return False


def register_user():
    """Register a test user if needed."""
    print(f"\n🔍 Registering user {TEST_EMAIL}...")
    try:
        response = httpx.post(
            f"{API_BASE}/auth/register",
            json={"email": TEST_EMAIL, "password": TEST_PASSWORD},
            timeout=5.0
        )
        if response.status_code == 201:
            print("✅ User registered successfully")
            return True
        elif response.status_code == 400:
            print("ℹ️  User already exists (this is OK)")
            return True
        else:
            print(f"❌ Registration failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Registration failed: {e}")
        return False


def login_user():
    """Login and get auth cookie."""
    print(f"\n🔍 Logging in as {TEST_EMAIL}...")
    try:
        response = httpx.post(
            f"{API_BASE}/auth/login",
            json={"email": TEST_EMAIL, "password": TEST_PASSWORD},
            timeout=5.0,
            follow_redirects=True
        )
        if response.status_code == 200:
            cookies = response.cookies
            access_token = cookies.get("access_token")
            if access_token:
                print("✅ Login successful")
                return access_token
            else:
                print("❌ Login successful but no access_token cookie found")
                return None
        else:
            print(f"❌ Login failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Login failed: {e}")
        return None


def get_current_user(access_token):
    """Get current user info."""
    print("\n🔍 Getting current user info...")
    try:
        response = httpx.get(
            f"{API_BASE}/auth/me",
            cookies={"access_token": access_token},
            timeout=5.0
        )
        if response.status_code == 200:
            user_data = response.json()
            print(f"✅ User: {user_data.get('email')} (workspace: {user_data.get('workspace_id')})")
            return user_data
        else:
            print(f"❌ Failed to get user: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Failed to get user: {e}")
        return None


def test_oauth_config():
    """Test OAuth configuration."""
    print("\n🔍 Checking OAuth configuration...")
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/google/callback")
    developer_token = os.getenv("GOOGLE_DEVELOPER_TOKEN")
    
    config_status = {
        "GOOGLE_CLIENT_ID": "✅" if client_id else "❌",
        "GOOGLE_CLIENT_SECRET": "✅" if client_secret else "❌",
        "GOOGLE_REDIRECT_URI": f"✅ ({redirect_uri})",
        "GOOGLE_DEVELOPER_TOKEN": "✅" if developer_token else "❌",
    }
    
    for key, status in config_status.items():
        print(f"  {key}: {status}")
    
    if not client_id or not client_secret:
        print("\n⚠️  Warning: GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET are required for OAuth")
        print("   Set these environment variables before testing the full OAuth flow")
        return False
    
    return True


def test_authorize_endpoint(access_token, workspace_id):
    """Test the authorize endpoint."""
    print("\n🔍 Testing /auth/google/authorize endpoint...")
    try:
        response = httpx.get(
            f"{API_BASE}/auth/google/authorize",
            cookies={"access_token": access_token},
            follow_redirects=False,  # Don't follow redirect to Google
            timeout=5.0
        )
        
        if response.status_code == 307 or response.status_code == 302:
            redirect_url = response.headers.get("location", "")
            print(f"✅ Authorize endpoint redirects correctly")
            print(f"   Redirect URL: {redirect_url[:100]}...")
            
            # Parse redirect URL
            parsed = urlparse(redirect_url)
            if parsed.netloc == "accounts.google.com":
                params = parse_qs(parsed.query)
                print(f"\n   OAuth Parameters:")
                print(f"   - client_id: {'✅' if params.get('client_id') else '❌'}")
                print(f"   - redirect_uri: {'✅' if params.get('redirect_uri') else '❌'}")
                print(f"   - response_type: {'✅' if params.get('response_type') == ['code'] else '❌'}")
                print(f"   - scope: {'✅' if params.get('scope') else '❌'}")
                print(f"   - state: {'✅' if params.get('state') == [str(workspace_id)] else '❌'}")
                print(f"   - access_type: {'✅' if params.get('access_type') == ['offline'] else '❌'}")
                print(f"   - prompt: {'✅' if params.get('prompt') == ['consent'] else '❌'}")
                
                return True
            else:
                print(f"❌ Redirect URL is not to Google: {parsed.netloc}")
                return False
        elif response.status_code == 500:
            error_detail = response.text
            print(f"❌ Authorize endpoint returned 500: {error_detail}")
            if "not configured" in error_detail.lower():
                print("   This is expected if GOOGLE_CLIENT_ID/SECRET are not set")
            return False
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Authorize endpoint test failed: {e}")
        return False


def test_callback_endpoint_error_cases():
    """Test callback endpoint error handling."""
    print("\n🔍 Testing /auth/google/callback error handling...")
    
    test_cases = [
        ("Missing code", "/auth/google/callback", {}),
        ("Missing state", "/auth/google/callback?code=test123", {}),
        ("OAuth error", "/auth/google/callback?error=access_denied", {}),
    ]
    
    all_passed = True
    for name, url, cookies in test_cases:
        try:
            response = httpx.get(
                f"{API_BASE}{url}",
                cookies=cookies,
                follow_redirects=False,
                timeout=5.0
            )
            
            if response.status_code == 302 or response.status_code == 307:
                redirect_url = response.headers.get("location", "")
                if "google_oauth=error" in redirect_url:
                    print(f"✅ {name}: Correctly redirects with error")
                else:
                    print(f"❌ {name}: Redirect URL doesn't contain error: {redirect_url}")
                    all_passed = False
            else:
                print(f"❌ {name}: Unexpected status code: {response.status_code}")
                all_passed = False
        except Exception as e:
            print(f"❌ {name}: Test failed: {e}")
            all_passed = False
    
    return all_passed


def main():
    """Run all tests."""
    print("=" * 60)
    print("Google OAuth Endpoint Test Suite")
    print("=" * 60)
    
    # Test health
    if not test_health():
        print("\n❌ API is not available. Please start the backend server.")
        sys.exit(1)
    
    # Register user
    if not register_user():
        print("\n❌ Failed to register user")
        sys.exit(1)
    
    # Login
    access_token = login_user()
    if not access_token:
        print("\n❌ Failed to login")
        sys.exit(1)
    
    # Get user info
    user_data = get_current_user(access_token)
    if not user_data:
        print("\n❌ Failed to get user info")
        sys.exit(1)
    
    workspace_id = user_data.get("workspace_id")
    
    # Test OAuth config
    oauth_configured = test_oauth_config()
    
    # Test authorize endpoint
    authorize_works = test_authorize_endpoint(access_token, workspace_id)
    
    # Test callback error handling
    callback_errors_work = test_callback_endpoint_error_cases()
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"API Health: ✅")
    print(f"User Auth: ✅")
    print(f"OAuth Config: {'✅' if oauth_configured else '⚠️  (set env vars)'}")
    print(f"Authorize Endpoint: {'✅' if authorize_works else '❌'}")
    print(f"Callback Error Handling: {'✅' if callback_errors_work else '❌'}")
    
    print("\n" + "=" * 60)
    print("Next Steps for Manual Testing")
    print("=" * 60)
    print("1. Ensure GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET are set")
    print("2. Ensure GOOGLE_REDIRECT_URI matches your Google Cloud Console config")
    print("3. Visit: http://localhost:8000/auth/google/authorize (while logged in)")
    print("4. Complete OAuth flow on Google")
    print("5. Verify redirect to /settings?google_oauth=success")
    print("6. Check that connection appears in Settings page")
    
    if authorize_works and callback_errors_work:
        print("\n✅ All automated tests passed!")
        sys.exit(0)
    else:
        print("\n⚠️  Some tests failed. Check the output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()


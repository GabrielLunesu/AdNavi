# Google OAuth Implementation Guide

## ✅ Completed

### 1. Legal Pages (GDPR/CCPA Compliant)
- **Privacy Policy** (`/privacy`)
  - Comprehensive data collection, usage, and retention details
  - GDPR/CCPA rights outlined (access, deletion, portability)
  - Cookie policy and third-party services disclosure
  - Published at: `https://www.adnavi.app/privacy`

- **Terms of Service** (`/terms`)
  - Service usage terms and acceptable use policy
  - Account termination and liability clauses
  - Intellectual property and dispute resolution
  - Published at: `https://www.adnavi.app/terms`

### 2. Account Deletion (GDPR Right to Erasure)
- **Backend Endpoint**: `DELETE /auth/delete-account`
  - Deletes user account
  - Removes all workspace data if user is sole member
  - Cascades deletion to: connections, entities, metrics, queries, tokens
  - Clears authentication cookies
  - Logs all deletion operations

- **Frontend UI**:
  - Settings page (`/settings`) has dedicated "Delete Account & Data" section
  - Two-step confirmation to prevent accidental deletion
  - "Delete My Data" link in all footers (homepage, privacy, terms, dashboard)

### 3. Google OAuth Backend Flow
- **Authorization Endpoint**: `GET /auth/google/authorize`
  - Generates Google OAuth URL with required scopes
  - Scopes: `https://www.googleapis.com/auth/adwords`
  - Redirects user to Google consent screen
  - Includes state parameter for security

- **Callback Endpoint**: `GET /auth/google/callback`
  - Exchanges authorization code for access/refresh tokens
  - Fetches Google Ads customer details (ID, name, timezone, currency)
  - Encrypts and stores tokens using `token_service`
  - Creates/updates `Connection` with OAuth credentials
  - Redirects to `/settings` with success/error status

- **Router Registration**: Added to `main.py` as `/auth` prefix

### 4. Google OAuth Frontend UI
- **GoogleConnectButton** Component (`/components/GoogleConnectButton.jsx`)
  - "Connect Google Ads" button on Settings page
  - Redirects to backend OAuth authorize endpoint
  - Handles OAuth callback with query parameters
  - Shows success/error messages
  - Auto-refreshes connections on successful connection

- **Settings Page Updates** (`/settings`)
  - "Connect Ad Accounts" section with Google OAuth button
  - Lists all connected accounts
  - Per-connection sync buttons
  - Account deletion section

### 5. Token Security
- Tokens encrypted with Fernet encryption (`security.py`)
- Stored in `tokens` table with separate columns:
  - `access_token_enc` - Encrypted access token
  - `refresh_token_enc` - Encrypted refresh token
- Encryption key from `SECRET_KEY` environment variable
- Decryption only happens at request time

### 6. Database Models
No new migrations needed - using existing schema:
- `Connection` - Links workspace to provider account
- `Token` - Stores encrypted OAuth credentials
- `User` - User account with workspace relationship

## 📋 Next Steps: Google Cloud Console Configuration

### 1. OAuth Consent Screen
Navigate to: [Google Cloud Console - OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent)

**User Type**: External (for public access)

**App Information**:
- App name: `AdNavi`
- User support email: `[Your Support Email]`
- App logo: Upload `ui/public/adnavi.png`
- Application home page: `https://www.adnavi.app`
- Application privacy policy link: `https://www.adnavi.app/privacy`
- Application terms of service link: `https://www.adnavi.app/terms`
- Authorized domains: `adnavi.app`

**Developer Contact Information**:
- Email addresses: `[Your Contact Email]`

**Scopes**:
Add the following scope:
- `https://www.googleapis.com/auth/adwords` (View and manage your Google Ads data)

### 2. OAuth Credentials
Navigate to: [Google Cloud Console - Credentials](https://console.cloud.google.com/apis/credentials)

**Create OAuth 2.0 Client ID**:
- Application type: `Web application`
- Name: `AdNavi Production`
- Authorized JavaScript origins:
  - `https://www.adnavi.app`
  - `http://localhost:3000` (for testing)
- Authorized redirect URIs:
  - `https://api.adnavi.app/auth/google/callback` (production)
  - `http://localhost:8000/auth/google/callback` (for testing)

**Update Environment Variables**:
```bash
# Backend .env
GOOGLE_CLIENT_ID="[Your Client ID from above]"
GOOGLE_CLIENT_SECRET="[Your Client Secret from above]"
GOOGLE_OAUTH_REDIRECT_URI="https://api.adnavi.app/auth/google/callback"

# Frontend .env
NEXT_PUBLIC_API_BASE="https://api.adnavi.app"
```

### 3. Google Ads API Configuration
Ensure you have:
- Google Ads API enabled in your GCP project
- Developer token (apply at: https://developers.google.com/google-ads/api/docs/get-started/dev-token)
- Manager account (MCC) for production access

```bash
# Backend .env
GOOGLE_DEVELOPER_TOKEN="[Your Developer Token]"
```

### 4. Google OAuth Verification Submission

**Verification Requirements**:
1. **App Homepage**: Live at `https://www.adnavi.app` ✅
2. **Privacy Policy**: Live at `https://www.adnavi.app/privacy` ✅
3. **Terms of Service**: Live at `https://www.adnavi.app/terms` ✅
4. **OAuth Consent Screen**: Configured as above
5. **Authorized Domains**: Verified ownership of `adnavi.app`
6. **Verification Video**: Required for sensitive/restricted scopes

**Verification Video Requirements**:
Record a 2-3 minute video demonstrating:
1. User lands on AdNavi homepage
2. User clicks "Get Started" → registers/logs in
3. User navigates to Settings
4. User clicks "Connect Google Ads"
5. Google OAuth consent screen appears
6. User grants permissions
7. User redirected back to Settings
8. Google Ads account shows as connected
9. User can view campaigns/data from Google Ads
10. Demonstrate secure data handling (no exposed tokens)

**Upload Video**:
- YouTube (unlisted) or Google Drive link
- Include in OAuth verification submission form

**Submit for Verification**:
Navigate to: [Google Cloud Console - OAuth Verification](https://console.cloud.google.com/apis/credentials/consent)
- Click "Prepare for Verification"
- Complete verification questionnaire
- Submit verification video
- Wait for Google review (typically 3-7 business days)

## 🔒 Security Checklist

- [x] Tokens encrypted at rest
- [x] HTTPS enforced in production
- [x] Secure HTTP-only cookies for authentication
- [x] CORS configured for production domain
- [x] State parameter in OAuth flow (CSRF protection)
- [x] No tokens logged or exposed in responses
- [x] User data deletion capability (GDPR compliance)
- [x] Privacy policy and ToS published

## 🧪 Testing Before Submission

### Automated Testing
Run the test script to verify endpoints:
```bash
cd backend
python test_google_oauth.py
```

This will test:
- API health check
- User registration/login
- OAuth configuration validation
- Authorize endpoint (redirect validation)
- Callback endpoint error handling

### Local Testing
1. Start backend: `cd backend && source bin/activate && python start_api.py`
2. Start frontend: `cd ui && npm run dev`
3. Visit: `http://localhost:3000`
4. Register/login
5. Navigate to Settings
6. Click "Connect Google Ads"
7. Complete OAuth flow
8. Verify connection appears in Settings
9. Test sync functionality
10. Test account deletion

### Manual Endpoint Testing
```bash
# 1. Login and get cookie
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}' \
  -c cookies.txt

# 2. Test authorize endpoint (will redirect to Google)
curl -L http://localhost:8000/auth/google/authorize \
  -b cookies.txt \
  -v

# 3. Test callback error handling
curl http://localhost:8000/auth/google/callback?error=access_denied \
  -v
```

### Production Testing
1. Deploy backend to production server
2. Deploy frontend to production server
3. Configure production environment variables
4. Test full OAuth flow on production domain
5. Record verification video on production

## 📚 References

- **Backend OAuth Router**: `backend/app/routers/google_oauth.py`
- **Frontend Connect Button**: `ui/components/GoogleConnectButton.jsx`
- **Settings Page**: `ui/app/(dashboard)/settings/page.jsx`
- **Delete Account Endpoint**: `backend/app/routers/auth.py` (DELETE `/auth/delete-account`)
- **Privacy Policy**: `docs/PRIVACY_POLICY.md` + `ui/app/privacy/page.jsx`
- **Terms of Service**: `docs/TERMS_OF_SERVICE.md` + `ui/app/terms/page.jsx`

## 🎯 Current Status

**Backend Implementation**:
- ✅ OAuth authorize endpoint (`GET /auth/google/authorize`)
- ✅ OAuth callback endpoint (`GET /auth/google/callback`)
- ✅ State parameter validation and workspace verification
- ✅ Comprehensive error handling for all failure cases
- ✅ Token encryption and storage via `token_service`
- ✅ Connection creation/update logic
- ✅ Google Ads API integration for customer data fetching
- ✅ Missing logger import fixed in `auth.py`
- ✅ Test script created (`backend/test_google_oauth.py`)

**Frontend Implementation**:
- ✅ GoogleConnectButton component
- ✅ Error message handling for all error cases
- ✅ Success/error state management
- ✅ Settings page integration

**Ready for**:
- ✅ Google Cloud Console OAuth configuration
- ✅ Local testing of OAuth flow
- ✅ Production deployment
- ⏳ Verification video recording
- ⏳ Google OAuth verification submission

**Not Yet Done**:
- ⏳ Update environment variables with OAuth credentials
- ⏳ Domain verification for `adnavi.app` in Google Cloud Console
- ⏳ Record verification video
- ⏳ Submit for Google verification

## 🚀 Deployment Notes

1. Ensure production domains are live before OAuth verification
2. SSL certificates must be valid (Let's Encrypt recommended)
3. Frontend must be accessible at `https://www.adnavi.app`
4. Backend API must be accessible at `https://api.adnavi.app`
5. Test OAuth flow on production before submitting for verification
6. Monitor logs during verification review for any issues

## 📞 Support

For Google OAuth verification issues:
- [Google OAuth Support](https://support.google.com/code/contact/oauth_verification)
- [Google Ads API Forum](https://groups.google.com/g/adwords-api)



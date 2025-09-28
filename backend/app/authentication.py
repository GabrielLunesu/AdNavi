"""Simple authentication backend for SQLAdmin.

This module provides a basic authentication system for the admin panel
using hardcoded credentials and session-based authentication.

Production note: Replace hardcoded credentials with environment variables
and implement proper user authentication from the database.
"""

from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

# Hardcoded admin credentials
# TODO: In production, these should come from environment variables or database
ADMIN_USER = "admin"
ADMIN_PASS = "secret"


class SimpleAuth(AuthenticationBackend):
    """Simple authentication backend for SQLAdmin.
    
    Uses session cookies to maintain login state.
    Credentials are hardcoded for development purposes.
    """
    
    async def login(self, request: Request) -> bool:
        """Handle login form submission.
        
        Args:
            request: The incoming request with form data
            
        Returns:
            True if login successful, False otherwise
        """
        form = await request.form()
        username = form.get("username")
        password = form.get("password")
        
        # Check hardcoded credentials
        if username == ADMIN_USER and password == ADMIN_PASS:
            # Store a simple token in the session to indicate logged in
            request.session.update({"admin_token": "authenticated"})
            return True
        
        return False
    
    async def logout(self, request: Request) -> bool:
        """Handle logout request.
        
        Args:
            request: The incoming request
            
        Returns:
            True to indicate successful logout
        """
        # Clear the entire session
        request.session.clear()
        return True
    
    async def authenticate(self, request: Request) -> bool:
        """Check if the current request is authenticated.
        
        This is called on every request to /admin/* routes.
        
        Args:
            request: The incoming request
            
        Returns:
            True if authenticated, False otherwise
        """
        # Check if the session contains our auth token
        token = request.session.get("admin_token")
        return token == "authenticated"

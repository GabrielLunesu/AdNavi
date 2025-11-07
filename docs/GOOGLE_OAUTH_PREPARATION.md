# Google OAuth Preparation - Summary

**Date:** November 7, 2025  
**Branch:** google-oauth  
**Status:** Legal pages complete, OAuth implementation ready

---

## ✅ Completed Tasks

### 1. Privacy Policy Page
- **File:** `ui/app/privacy/page.jsx`
- **URL:** `https://www.adnavi.app/privacy`
- **Content Includes:**
  - Comprehensive data collection disclosure
  - Google Ads integration specifics
  - Data security measures (encryption, TLS)
  - User rights (GDPR, CCPA compliant)
  - Third-party service integrations
  - Data retention policies
  - International data transfer disclosures

### 2. Terms of Service Page
- **File:** `ui/app/terms/page.jsx`
- **URL:** `https://www.adnavi.app/terms`
- **Content Includes:**
  - Service description
  - User eligibility and conduct
  - Third-party platform integration terms
  - Data accuracy disclaimers
  - Liability limitations
  - Payment and subscription terms
  - Dispute resolution and arbitration

### 3. Footer Components
- **Main Footer:** `ui/components/Footer.jsx`
  - Used on public pages (Privacy, Terms)
  - Links to Privacy Policy and Terms of Service
  - Copyright notice
  
- **Dashboard Footer:** `ui/components/FooterDashboard.jsx`
  - Used on dashboard pages
  - Compact design with links to Privacy and Terms
  - Integrated into dashboard layout

### 4. Layout Updates
- Updated `ui/app/(dashboard)/layout.jsx` to include footer
- Privacy and Terms pages are standalone with full footer
- All legal pages are accessible and properly formatted

---

## 📋 Next Steps for Google OAuth

### Phase 1: Backend OAuth Implementation (2-3 hours)

Create `backend/app/routers/google_oauth.py`:

```python
# OAuth endpoints:
# GET /auth/google/authorize - Redirects to Google consent screen
# GET /auth/google/callback - Handles OAuth callback, stores tokens
```

**Features:**
- OAuth 2.0 authorization flow
- Access token and refresh token exchange
- Customer ID fetching and selection
- Encrypted token storage using existing `token_service.py`
- Connection creation with timezone/currency metadata

**Environment Variables Needed:**
```bash
GOOGLE_CLIENT_ID=your_client_id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your_client_secret
GOOGLE_REDIRECT_URI=https://t8zgrthold5r2-backend--8000.prod1.defang.dev/auth/google/callback
FRONTEND_URL=https://www.adnavi.app
```

### Phase 2: Frontend OAuth UI (1-2 hours)

Create `ui/components/GoogleConnectButton.jsx`:
- "Connect Google Ads" button
- Redirects to backend `/auth/google/authorize`
- Handle success/error query params on return

Update `ui/app/(dashboard)/settings/page.jsx`:
- Add Google connect button
- Display connection status
- Show success/error messages

### Phase 3: Google Cloud Console Configuration (1 hour)

#### A. OAuth Consent Screen
1. Navigate to: [Google Cloud Console](https://console.cloud.google.com)
2. Go to: APIs & Services → OAuth consent screen
3. Configure:
   - **App name:** AdNavi
   - **User support email:** [your email]
   - **App logo:** 120x120px logo
   - **App domain:**
     - Homepage: `https://www.adnavi.app`
     - Privacy policy: `https://www.adnavi.app/privacy`
     - Terms of service: `https://www.adnavi.app/terms`
   - **Authorized domains:** `adnavi.app`
   - **Developer contact:** [your email]

#### B. Add OAuth Scopes
- Scope: `https://www.googleapis.com/auth/adwords`
- Justification: "Access Google Ads accounts to display campaign performance data"

#### C. OAuth Credentials
1. Go to: APIs & Services → Credentials
2. Create OAuth 2.0 Client ID (if not exists)
3. Add authorized redirect URIs:
   - Development: `http://localhost:8000/auth/google/callback`
   - Production: `https://t8zgrthold5r2-backend--8000.prod1.defang.dev/auth/google/callback`

#### D. Testing Mode
- Add test users (your email and any test accounts)
- Test OAuth flow in development and production

### Phase 4: Google OAuth Verification (When Ready)

**Prerequisites:**
- ✅ Privacy Policy live at `https://www.adnavi.app/privacy`
- ✅ Terms of Service live at `https://www.adnavi.app/terms`
- ⏳ OAuth flow implemented and tested
- ⏳ App logo ready (120x120px)

**Verification Requirements:**
1. **Screencast Video (Unlisted YouTube):**
   - Show user clicking "Connect Google Ads" button
   - Google consent screen with scope permissions
   - Successful connection and data display
   - 2-3 minutes duration

2. **Written Justification:**
   - Explain why you need `adwords` scope
   - Describe how you use the data
   - Confirm compliance with Google's policies

3. **Review Process:**
   - Submit through Google Cloud Console
   - Review time: 3-7 business days
   - May require additional information

---

## 🔒 Security Checklist

Before going live:

- [ ] `TOKEN_ENCRYPTION_KEY` set in production
- [ ] Google Client Secret secured (not in code)
- [ ] Redirect URI matches exactly in Google Console
- [ ] Privacy policy publicly accessible
- [ ] Terms of service publicly accessible
- [ ] CORS origins include frontend domain
- [ ] Test OAuth flow end-to-end
- [ ] Verify token encryption/decryption works
- [ ] Test token refresh mechanism
- [ ] Ensure workspace isolation works

---

## 📁 Files Created/Modified

### Created:
- `ui/app/privacy/page.jsx` - Privacy Policy page
- `ui/app/terms/page.jsx` - Terms of Service page
- `ui/components/Footer.jsx` - Main footer component
- `ui/components/FooterDashboard.jsx` - Dashboard footer component
- `docs/PRIVACY_POLICY.md` - Privacy policy in markdown
- `docs/TERMS_OF_SERVICE.md` - Terms of service in markdown
- `docs/GOOGLE_OAUTH_PREPARATION.md` - This file

### Modified:
- `ui/app/(dashboard)/layout.jsx` - Added footer to dashboard

### To Create (Next Phase):
- `backend/app/routers/google_oauth.py` - OAuth endpoints
- `ui/components/GoogleConnectButton.jsx` - Connect button
- Update `backend/app/main.py` - Register OAuth router
- Update `ui/app/(dashboard)/settings/page.jsx` - Add connect button

---

## 🌐 URLs

- **Production Frontend:** https://www.adnavi.app
- **Production Backend:** https://t8zgrthold5r2-backend--8000.prod1.defang.dev
- **Privacy Policy:** https://www.adnavi.app/privacy
- **Terms of Service:** https://www.adnavi.app/terms
- **OAuth Callback:** https://t8zgrthold5r2-backend--8000.prod1.defang.dev/auth/google/callback

---

## 📝 Notes

- All legal pages are GDPR and CCPA compliant
- Privacy policy covers Google Ads OAuth scope
- Terms include data accuracy disclaimers for third-party APIs
- Footer is responsive and matches design system
- Ready to proceed with OAuth implementation

---

**Status:** Ready for OAuth backend implementation and Google Cloud Console configuration.


# Security Review – HTTPS and Secure Redirects

## HTTPS & Redirects
- SECURE_SSL_REDIRECT enabled to force all traffic over HTTPS.
- HSTS (31536000 seconds, includeSubDomains, preload) enabled to enforce HTTPS at the browser level.

## Cookies
- SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE ensure cookies are only transmitted over HTTPS.

## Headers
- X_FRAME_OPTIONS set to DENY (prevents clickjacking).
- SECURE_CONTENT_TYPE_NOSNIFF prevents MIME-sniffing.
- SECURE_BROWSER_XSS_FILTER enabled to reduce XSS risk.

## Deployment
- SSL/TLS certificates configured via Nginx (example provided).
- Redirects all port 80 traffic to 443 with HTTPS.

## Areas to Improve
- Regularly rotate TLS certificates.
- Enable HTTP/2 or HTTP/3 for faster and more secure transport.
- Consider using CSP (Content Security Policy) for additional XSS protection.
# Security Best Practices in Django

- DEBUG set to False in production
- XSS & content sniffing protections enabled
- CSRF & session cookies marked as secure
- All forms include {% csrf_token %} for CSRF protection
- Queries use Django ORM, preventing SQL injection
- Content Security Policy (CSP) configured via middleware

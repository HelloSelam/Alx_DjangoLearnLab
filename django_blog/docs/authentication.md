# Authentication System — Django Blog

## Overview
Implements registration, login, logout, and profile management.

## Files
- blog/models.py — Profile model (OneToOne with User)
- blog/forms.py — CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
- blog/views.py — register_view, CustomLoginView, CustomLogoutView, profile_view
- blog/urls.py — /register/, /login/, /logout/, /profile/
- blog/templates/blog/*.html — templates for login/register/profile

## Setup
1. Install dependencies:
   pip install Django Pillow

2. Migrate:
   python manage.py makemigrations
   python manage.py migrate

3. Create a superuser:
   python manage.py createsuperuser

4. Run server:
   python manage.py runserver

## Testing
- Manual:
  - Visit /register, create account, then /login, then /profile to edit.
- Automated:
  - python manage.py test

## Security Notes
- CSRF tokens are used in all forms.
- Passwords handled by Django's authentication system.
- In production, use HTTPS and secure cookies.
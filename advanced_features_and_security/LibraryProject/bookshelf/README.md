# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created via Django admin:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Views
Permissions enforced using @permission_required decorator in `views.py`.

from rest_framework import permissions
from .permissions import IsStaffEditorPermissions

class StaffEditorPermissionsMixin():
    permissions_classes = [ permissions.IsAdminUser, IsStaffEditorPermissions]
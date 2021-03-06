# coding=UTF8
from rest_framework.permissions import BasePermission


class ProtectScriptAccess(BasePermission):
    """
    Disallow editing scripts that are bound to socket.
    """
    allowed_actions = ('retrieve',)

    def has_object_permission(self, request, view, obj):
        return getattr(obj, 'socket_id', None) is None or view.action in self.allowed_actions


class ProtectScheduleAccess(ProtectScriptAccess):
    """
    Disallow editing schedules that are bound to socket.
    """
    allowed_actions = ('retrieve',)

from rest_framework import permissions

class IsColecionador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite acesso apenas se o usuário for o colecionador da coleção
        return obj.colecionador == request.user
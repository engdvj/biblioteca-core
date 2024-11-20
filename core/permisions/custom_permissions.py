from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsColecionador(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite leitura para todos os métodos seguros (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        # Apenas o colecionador pode modificar ou deletar
        return obj.colecionador == request.user

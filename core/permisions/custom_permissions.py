from rest_framework import permissions

class IsColecionador(permissions.BasePermission):
    """
    Permissão personalizada para que apenas o colecionador possa modificar sua própria coleção.
    """

    def has_object_permission(self, request, view, obj):
        # Permissão de leitura é permitida para qualquer requisição,
        # então verificamos se é uma requisição segura (GET, HEAD ou OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permissão de escrita é concedida apenas ao colecionador da coleção
        return obj.colecionador == request.user
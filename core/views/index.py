from django.shortcuts import redirect, render

def index(request):
    if request.user.is_authenticated:
        return redirect('api-root')  # Redireciona para ApiRaiz se o usuário estiver autenticado
    return render(request, 'index.html')  # Renderiza a tela de login

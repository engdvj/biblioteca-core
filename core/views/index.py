from django.shortcuts import redirect, render

def index(request):
    # Se o usuário estiver autenticado, redireciona para /api/
    if request.user.is_authenticated:
        return redirect('/api/')
    # Caso contrário, renderiza a página de login
    return render(request, 'index.html')

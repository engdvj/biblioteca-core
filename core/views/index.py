from django.shortcuts import redirect, render

def index(request):
    if request.user.is_authenticated:
        # Redireciona para /api/ se o usuário estiver autenticado
        return redirect('/api/')
    # Renderiza o index.html para usuários não autenticados
    return render(request, 'index.html')

from django.shortcuts import redirect, render

from .forms import UsuarioForm

# Create your views here.

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save() # se guarda la información en la base datos!
            return redirect('registro')
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})


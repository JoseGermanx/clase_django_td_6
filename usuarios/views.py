from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import UsuarioForm

# Create your views here.

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save() # se guarda la información en la base datos!
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('registro')
        else:
            messages.error(request, "Hay error en el registro.")
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})


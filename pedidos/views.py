from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido

@login_required
def panel_estudiante(request):
    # (Método POST)
    if request.method == 'POST':
        platillo_pedido = request.POST.get('platillo')
        cantidad_pedida = request.POST.get('cantidad')
        
        # Guardamos el nuevo pedido en la base de datos
        Pedido.objects.create(
            estudiante=request.user,
            platillo=platillo_pedido,
            cantidad=cantidad_pedida
        )
        return redirect('panel')

    # 2. Si solo está entrando a la página a mirar (Método GET)
    # Buscamos sus pedidos y los ordenamos por el más reciente
    mis_pedidos = Pedido.objects.filter(estudiante=request.user).order_by('-id')
    
    return render(request, 'panel.html', {'pedidos': mis_pedidos})

# (Delete)
@login_required
def cancelar_pedido(request, pedido_id):
    if request.method == 'POST':
        # Buscamos el pedido exacto, asegurándonos que sea del usuario actual
        pedido_a_borrar = Pedido.objects.get(id=pedido_id, estudiante=request.user)
        pedido_a_borrar.delete() 
    return redirect('panel')

# (Update)
@login_required
def editar_pedido(request, pedido_id):
    # Buscamos el pedido exacto
    pedido_a_editar = Pedido.objects.get(id=pedido_id, estudiante=request.user)

    if request.method == 'POST':
        # Si el usuario mandó el formulario, sobrescribimos los datos
        pedido_a_editar.platillo = request.POST.get('platillo')
        pedido_a_editar.cantidad = request.POST.get('cantidad')
        pedido_a_editar.save() 
        
        return redirect('panel') 

    # Si solo quiere ver la pantalla de edición, le mandamos sus datos actuales
    return render(request, 'editar.html', {'pedido': pedido_a_editar})
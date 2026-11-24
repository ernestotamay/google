from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Detail

def index(request):
    contactos = Contact.objects.all()
    return render(request, 'contacts/index.html', {'contactos': contactos})

def detalle_contacto(request, pk):
    contacto = get_object_or_404(Contact, pk=pk)
    detalles = contacto.detalles.all()
    return render(request, 'contacts/detalle.html', {'contacto': contacto, 'detalles': detalles})

def nuevo_contacto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        empresa = request.POST.get('empresa')
        correo = request.POST.get('email')

        contacto = Contact.objects.create(
            nombre=nombre,
            apellido=apellido
        )

        Detail.objects.create(
            contacto=contacto,
            telefono=telefono,
            empresa=empresa,
            correo=correo
        )

        return redirect('index')

    return render(request, 'contacts/nuevo.html')

def editar_contacto(request, pk):
    contacto = get_object_or_404(Contact, pk=pk)
    detalle = contacto.detalles.first()  # obtenemos el detalle asociado

    if request.method == "POST":
        # Datos de Contact
        contacto.nombre = request.POST.get('nombre')
        contacto.apellido = request.POST.get('apellido')
        contacto.save()

        # Datos de Detail
        detalle.telefono = request.POST.get('telefono')
        detalle.empresa = request.POST.get('empresa')
        detalle.correo = request.POST.get('email')
        detalle.save()

        return redirect('index')

    return render(request, 'contacts/editar.html', {
        'contacto': contacto,
        'detalle': detalle
    })
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contact, pk=pk)
    contacto.delete()
    return redirect('index')
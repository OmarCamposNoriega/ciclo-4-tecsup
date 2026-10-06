from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    if request.method == 'POST':
        context = {
            'titulo': "Respuesta",
            'nombre' : request.POST.get('nombre', ''),
            'clave' : request.POST.get('password', ''),
            'educacion': request.POST.get('educacion', ''),
            'nacionalidad': request.POST.get('nacionalidad', 'No especificada'),
            'idiomas': request.POST.getlist('idiomas'),
            'correo': request.POST.get('email', ''),
            'website': request.POST.get('sitioweb', ''),
        }
        return render(request, 'encuesta/respuesta.html', context)
    # Si se accede por GET directamente en la barra del navegador, redirige al formulario
    return redirect('encuesta:index')

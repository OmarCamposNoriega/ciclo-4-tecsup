import math
from django.shortcuts import render, redirect

def index(request):
    """Menú principal para la Actividad 3 (Caso de Estudio)"""
    return render(request, 'operaciones/index.html', {'titulo': "Actividad 3: Operaciones y Cálculos"})

def calculadora_form(request):
    """Formulario para ingresar dos números y elegir operación (suma, resta, multiplicación)"""
    return render(request, 'operaciones/calculadora_form.html', {'titulo': "Operaciones Matemáticas"})

def calculadora_resultado(request):
    """Procesa los datos enviados y muestra el resultado en otra vista"""
    if request.method == 'POST':
        try:
            n1_raw = request.POST.get('numero1', '0').strip().replace(',', '.')
            n2_raw = request.POST.get('numero2', '0').strip().replace(',', '.')
            n1 = float(n1_raw)
            n2 = float(n2_raw)
            operacion = request.POST.get('operacion', 'suma')

            n1_display = int(n1) if n1.is_integer() else n1
            n2_display = int(n2) if n2.is_integer() else n2

            if operacion == 'suma':
                res = n1 + n2
                res_display = int(res) if res.is_integer() else res
                mensaje = f"La suma de {n1_display} + {n2_display} = {res_display}"
            elif operacion == 'resta':
                res = n1 - n2
                res_display = int(res) if res.is_integer() else res
                mensaje = f"La resta de {n1_display} - {n2_display} = {res_display}"
            elif operacion == 'multiplicacion':
                res = n1 * n2
                res_display = int(res) if res.is_integer() else res
                mensaje = f"La multiplicación de {n1_display} * {n2_display} = {res_display}"
            else:
                mensaje = "Operación no reconocida"

            context = {
                'titulo': "Resultado de la Operación",
                'mensaje': mensaje,
            }
            return render(request, 'operaciones/calculadora_resultado.html', context)
        except (ValueError, TypeError):
            return render(request, 'operaciones/calculadora_resultado.html', {
                'titulo': "Error",
                'mensaje': "Debe ingresar números válidos."
            })
    return redirect('operaciones:calculadora_form')

def cilindro_vista(request):
    """Formulario y cálculo del volumen de un cilindro"""
    context = {
        'titulo': "CÁLCULO DEL VOLUMEN DE UN CILINDRO",
        'resultado': None,
        'diametro': '',
        'altura': '',
        'error': None,
    }
    if request.method == 'POST':
        diametro_input = request.POST.get('diametro', '').strip()
        altura_input = request.POST.get('altura', '').strip()
        context['diametro'] = diametro_input
        context['altura'] = altura_input

        try:
            diametro = float(diametro_input.replace(',', '.'))
            altura = float(altura_input.replace(',', '.'))

            radio = diametro / 2.0
            volumen = math.pi * (radio ** 2) * altura
            # Formatear el resultado como en el ejemplo: 6.35338096859
            volumen_str = f"{volumen:.11f}"

            context['resultado'] = f"El volumen del cilindro es de {volumen_str} metros cúbicos"
        except (ValueError, TypeError):
            context['error'] = "Por favor ingrese valores numéricos válidos para diámetro y altura."

    return render(request, 'operaciones/cilindro.html', context)

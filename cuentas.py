def calcularGastos():
    persona1 = int(input('¿Cuánto cobra usted? '))
    persona2 = int(input('¿Cuánto cobra su pareja? '))
    gastosEnConjunto = int(input('¿Cuánto gastan por mes? '))
    x = gastosEnConjunto/(persona2+persona1)
    return '''Tienen que pagar {:.2f}% '''.format((x*100)) + '''de su sueldo cada uno
        Su pareja debe pagar €{:.2f}
        Usted debe pagar €{:.2f}
    '''.format(persona2*x,persona1*x)
print(calcularGastos())
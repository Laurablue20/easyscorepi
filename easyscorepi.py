""" La central de riesgos quiere asignar un puntaje de crédito a cada cliente 
dependiendo de su nivel de riesgo crediticio

Se han establecido las siguientes asignaciones para cada criterio a evaluar

EXPERIENCIA CREDITICIA

Años de vinculación al sector financiero    Puntaje
De 0 - 1 años                               0 puntos
De 1 a 5 años                               200 puntos
De 5 a 15 años                              300 puntos
De 15 a 20 años                             400 puntos
Más de 20 años                              500 puntos


DEUDAS TOTALES / INGRESOS MENSUALES

De 0 a 1                                    200 puntos
De 1 a 10                                   300 puntos
De 10 a 50                                  100 puntos
Más de 50                                   -200 puntos

# DEL INGRESO EMPLEADO EN PAGAR DEUDAS (CUOTAS MENSUALES / INGRESO MENSUAL)

# PAGO DEUDAS

De 0 a 0.30                                 200 puntos
De 0.30 a 0.50                              100 puntos
De 0.50 a 1                                 0 puntos
Mas de 1                                    -200 puntos

Se quiere definir una función llamada PuntajeCredito que determine el nivel de riesgo 
de la persona y con base en ello asignarle un plan de acción

Def PuntajeCredito = (PUNTAJE POR EXPERIENCIA CREDITICIA + PUNTAJE POR NIVEL DEDDA 
+ PUNTAJE POR % EMPLEADO PAGAR DEUDAS)
"""

def experiencia_crediticia(a):
    if a <1:
        puntos = 0
    elif a>=1 and a < 5:
        puntos = 200
    elif a>=5 and a < 15:
        puntos = 300
    elif a>=15 and a < 20:
        puntos = 400
    else:
        puntos = 500
    return puntos

def deudas_totales(a):
    if a <1:
        puntos = 200
    elif a>=1 and a < 10:
        puntos = 300
    elif a>=10 and a < 50:
        puntos = 100
    else:
        puntos = -200
    return puntos

def ingresos(a):
    if a <0.3:
        puntos = 200
    elif a>=0.3 and a < 0.5:
        puntos = 100
    elif a>=0.5 and a < 1:
        puntos = 0
    else:
        puntos = -200
    return puntos

def puntaje_credito(experiencia,deuda, ingreso):
    puntaje_general = experiencia + deuda + ingreso
    return puntaje_general

## Ejemplo

experiencia = experiencia_crediticia(5)
deuda = deudas_totales(3)
ingreso = ingresos(0.4)

puntaje_general = puntaje_credito(experiencia,deuda, ingreso)
print("Puntaje del ejemplo", puntaje_general)
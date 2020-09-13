__author__ = "Rodrigo Andres Rinaldi"
__email__ = "arcadia0101@hotmail.com"
__version__ = "1.0"

def ej1():
    print("Recomendacion de entrenamiento por categoria")

    """
    ingresar cada paciente con datos completos ej: nombre y apellido, cuantas horas de trabajo diario realiza, peso en kg, cuantas veces come en el dia 
    
    """
    horas_trabajo = 8
    peso = 70
    comidas_diarias = 4


    print(" ingresar nombre comleto")
    paciente_1 = str(input())
    print("nombre ingresado", paciente_1)

    print("ingresar carga horaria laboral")
    paciente_1 = int(input())
    print("trabaja", paciente_1, "horas diarias")

    print("ingrsar peso")
    paciente_1 = str(input())
    print("pesa", paciente_1, "kg")

    print("igresar cuantas veces come al dia")
    paciente_1 = str(input())
    print("come", paciente_1, "veces al dia")

    if horas_trabajo == 8 and peso == 70 and comidas_diarias == 4:
        print("ejercitar 1 hora de cardio")
    
    elif horas_trabajo == 10 and peso == 80 and comidas_diarias == 3:
        print("ejercitar 45 min y agregar barra proteica")

    elif horas_trabajo == 12 and peso == 90 and comidas_diarias == 2:
        print("solo ejercitar 30 min con cardio y agregar 1 barra proteica mas 1 fruta en horas de descanso")
    
    else:
        print("ver el caso mas+ a fondo")    



    print(" ingresar nombre comleto")
    paciente_2 = str(input())
    print("nombre ingresado", paciente_2)

    print("ingresar carga horaria laboral")
    paciente_2 = int(input())
    print("trabaja", paciente_2, "horas diarias")

    print("ingrsar peso")
    paciente_2 = str(input())
    print("pesa", paciente_2, "kg")

    print("igresar cuantas veces come al dia")
    paciente_2 = str(input())
    print("come", paciente_2, "veces al dia")

    if horas_trabajo == 8 and peso == 70 and comidas_diarias == 4:
        print("puede ejercitar 1 hora de cardio")
    
    elif horas_trabajo == 10 and peso == 80 and comidas_diarias == 3:
        print("ejercitar 45 min y agregar barra proteica")

    elif horas_trabajo == 12 and peso == 90 and comidas_diarias == 2:
        print("solo ejercitar 30 min con cardio y agregar 1 barra proteica mas 1 fruta en horas de descanso")    

    else:
        print("ver el caso mas a fondo")  


    print(" ingresar nombre comleto")
    paciente_3 = str(input())
    print("nombre ingresado", paciente_3)

    print("ingresar carga horaria laboral")
    paciente_3 = int(input())
    print("trabaja", paciente_3, "horas diarias")

    print("ingrsar peso")
    paciente_3 = str(input())
    print("pesa", paciente_3, "kg")

    print("igresar cuantas veces come al dia")
    paciente_3 = str(input())
    print("come", paciente_3, "veces al dia")

    if horas_trabajo == 8 and peso == 70 and comidas_diarias == 4:
        print("puede ejercitar 1 hora de cardio")
    
    if horas_trabajo == horas_trabajo + 2 and peso == peso + 10  and comidas_diarias == comidas_diarias - 1:
        print("ejercitar 45 min y agregar barra proteica")

     
    if horas_trabajo == horas_trabajo + 4 and peso == peso + 20 and comidas_diarias == comidas_diarias - 2:
        print("solo ejercitar 30 min con cardio y agregar 1 barra proteica mas 1 fruta en horas de descanso")    

    else:
        print("ver el caso mas a fondo")  


    print(" ingresar nombre comleto")
    paciente_4 = str(input())
    print("nombre ingresado", paciente_4)

    print("ingresar carga horaria laboral")
    paciente_4 = int(input())
    print("trabaja", paciente_4, "horas diarias")

    print("ingrsar peso")
    paciente_4 = str(input())
    print("pesa", paciente_4, "kg")

    print("igresar cuantas veces come al dia")
    paciente_4 = str(input())
    print("come", paciente_4, "veces al dia")


    

    if horas_trabajo == 8 and peso == 70 and comidas_diarias == 4:
        print("puede ejercitar 1 hora de cardio")
    
    if horas_trabajo == horas_trabajo + 2 and peso == peso + 10  and comidas_diarias == comidas_diarias - 1:
        print("ejercitar 45 min y agregar barra proteica")
    
    if horas_trabajo == horas_trabajo + 4 and peso == peso + 20 and comidas_diarias == comidas_diarias - 2:
        print("solo ejercitar 30 min con cardio y agregar 1 barra proteica mas 1 fruta en horas de descanso")    

    else:
        print("ver el caso mas a fondo")  


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
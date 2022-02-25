import copy

def inicio():
    print(""" BIENVENIDO A CALCULO PARA VIGAS POR EL METODO DE CAQUOT
PARA SALIR EN CUALQUIER MOMENTO ESCRIBE: -EXIT()-
---*---*---*---Jared DL---*---*---*---""")
    definir_cantidad_barras()

def definir_cantidad_barras():
    global n_barras
    n_barras=int(input("Cantidad de barras (sin contar barras en volado):"))
    if n_barras >0:
        definir_tramos_internos_externos()
    else:
        print("ELIGE UN VALOR VÁLIDO!!!")
        definir_cantidad_barras()

def definir_tramos_internos_externos():
    global tramo_i_e
    tramo_i_e =[]
    print("""DEFINE SI LAS BARRAS SON TRAMOS INTERNOS O EXTERNOS
0: Para internos
1: Para externos""")
    for i in range(1,n_barras+1):
        aux=int(input(f'Barra {i}: '))
        if aux==0 or aux==1:
            tramo_i_e.append(aux)
        else:
            print("ERROR! Seleciona un valor válido")
            definir_tramos_internos_externos()
    print(tramo_i_e)
    definir_momento_apoyo()
    

def definir_momento_apoyo():
    # global momento_apoyo
    # momento_apoyo =[]
    # print("""DEFINE MOMENTO EN LOS APOYOS""")
    # for i in range(1,n_barras+2):
    #     momento_apoyo.append(float(input(f'Momento en el apoyo {i} KN*m=')))
    definir_cantidad_de_cargas()

def definir_cantidad_de_cargas():
    global cantidad_cargas
    cantidad_cargas=[]
    print("""DEFINE CANTIDAD DE CARGAS POR BARRA""")
    for i in range(1,n_barras+1):
        cantidad_cargas.append(int(input(f"Cantidad de cargas sobre la barra {i}=")))
    print(cantidad_cargas)
    definir_tipo_de_carga()

def definir_tipo_de_carga():
    global tipo_cargas
    tipo_cargas =[]
    tipo_cargas.clear
    carga =[]
    print("""DEFINE TIPO DE CARGAS POR BARRA
    19: PUNTUAL
    26: TRAPEZOIDAL""")
    for i in range(1,n_barras+1):
        for j in range(1,cantidad_cargas[i-1]+1):
            carga.append(int(input(f'tipo de carga de la barra {i}: ')))
        tipo_cargas.append(copy.copy(carga))
        carga.clear()
    print(tipo_cargas)
    calcular_giros()

def calcular_giros():
    global giro_barra
    giro_barra =[]
    giro_barra.clear
    giro_en_1_barra = []
    i=0
    for j in tipo_cargas:
        i+=1
        print(f"cargas en barra {i}: {j}")
        for n in j:
            print(f"carga {j}")
            if n == 26:
                if tramo_i_e[i-1]==0:
                   giro_en_1_barra.append(trapezoidal_interno())
                elif tramo_i_e[i-1]==1:
                   giro_en_1_barra.append(trapezoidal_externo())
            elif n == 19:
                if tramo_i_e[i-1]==0:
                   giro_en_1_barra.append(puntual_interno())
                elif tramo_i_e[i-1]==1:
                   giro_en_1_barra.append(puntual_externo())  
        giro_barra.append(copy.copy(giro_en_1_barra))
        giro_en_1_barra.clear()
    print(giro_barra)
                

def trapezoidal_externo():
    giros = []
    a=float(input("a[m]="))
    b=float(input("b[m]="))
    c=float(input("c[m]="))
    l=a+b+c
    q1=float(input("q1[kN]="))
    q2=float(input("q2[kN]="))
    giro_der=((l**(3))/(360))*(q1*(10*((b*(3*c+2*b))/(l**(2)))-15*(((b+c)/(l)))**(4)+3*(((b+c)**(5)-c**(5))/(b*l**(4))))+q2*(10*((b*(3*c+b))/(l**(2)))+15*(((c)/(l)))**(4)-3*(((b+c)**(5)-c**(5))/(b*l**(4)))))
    giro_izq=((l**(3))/(360))*(q2*(10*((b*(3*a+2*b))/(l**(2)))-15*(((b+a)/(l)))**(4)+3*(((b+a)**(5)-a**(5))/(b*l**(4))))+q1*(10*((b*(3*a+b))/(l**(2)))+15*(((a)/(l)))**(4)-3*(((b+a)**(5)-a**(5))/(b*l**(4)))))
    giros.append([giro_der,giro_izq])
    print(f" giros {giros} ")
    return [giro_der,giro_izq]

def puntual_externo():
    giros = []
    global a
    global b
    global p
    global l
    a=float(input("a[m]="))
    b=float(input("b[m]="))
    l=a+b
    p=float(input("q[kN]="))
    giro_der=((p*a*b)/(6*l))*(b+l)
    giro_izq=((p*a*b)/(6*l))*(a+l)
    giros.append([giro_der,giro_izq])
    print(f" giros {giros} ")
    return [giro_der,giro_izq]

def trapezoidal_interno():
    giros = []
    a=float(input("a[m]="))
    b=float(input("b[m]="))
    c=float(input("c[m]="))
    l=a+b+c
    q1=float(input("q1[kN]="))
    q2=float(input("q2[kN]="))
    l_caquot= (a+b+c)*0.8

    if l_caquot>(a+b):
        a_f=a
        c_f=c-l+l_caquot
        b_f=b_f
        q1_f=q1
        q2_f=q2
        giro_der=((l_caquot**(3))/(360))*(q1_f*(10*((b_f*(3*c_f+2*b_f))/(l_caquot**(2)))-15*(((b_f+c_f)/(l_caquot)))**(4)+3*(((b_f+c_f)**(5)-c_f**(5))/(b_f*l_caquot**(4))))+q2_f*(10*((b_f*(3*c_f+b_f))/(l_caquot**(2)))+15*(((c_f)/(l_caquot)))**(4)-3*(((b_f+c_f)**(5)-c_f**(5))/(b_f*l_caquot**(4)))))
    else:
        a_f=a
        c_f=0
        b_f=b-l+l_caquot+c
        q1_f=q1
        q2_f=q1_f+b_f/b*(q2-q1)

        q2_inicial=q2
        q2=q2-c/b*(q2-q1)
        giro_der=((l_caquot**(3))/(360))*(q1_f*(10*((b_f*(3*c_f+2*b_f))/(l_caquot**(2)))-15*(((b_f+c_f)/(l_caquot)))**(4)+3*(((b_f+c_f)**(5)-c_f**(5))/(b_f*l_caquot**(4))))+q2_f*(10*((b_f*(3*c_f+b_f))/(l_caquot**(2)))+15*(((c_f)/(l_caquot)))**(4)-3*(((b_f+c_f)**(5)-c_f**(5))/(b_f*l_caquot**(4)))))


    if l_caquot>(c+b):
        a_f=b-l+l_caquot
        c_f=c
        b_f=b_f
        q1_f=q1
        q2_f=q2
        giro_izq=((l_caquot**(3))/(360))*(q2_f*(10*((b_f*(3*a_f+2*b_f))/(l_caquot**(2)))-15*(((b_f+a_f)/(l_caquot)))**(4)+3*(((b_f+a_f)**(5)-a_f**(5))/(b_f*l_caquot**(4))))+q1_f*(10*((b_f*(3*a_f+b_f))/(l_caquot**(2)))+15*(((a_f)/(l_caquot)))**(4)-3*(((b_f+a_f)**(5)-a_f**(5))/(b_f*l_caquot**(4)))))
    else:
        a_f=0
        c_f=c
        b_f=b-l+l_caquot+a
        q1_f=q1_f+b_f/b*(q2-q1)
        q2_f=q2
        q1=q1-a/b*(q1-q2)
        giro_izq=((l_caquot**(3))/(360))*(q2_f*(10*((b_f*(3*a_f+2*b_f))/(l_caquot**(2)))-15*(((b_f+a_f)/(l_caquot)))**(4)+3*(((b_f+a_f)**(5)-a_f**(5))/(b_f*l_caquot**(4))))+q1_f*(10*((b_f*(3*a_f+b_f))/(l_caquot**(2)))+15*(((a_f)/(l_caquot)))**(4)-3*(((b_f+a_f)**(5)-a_f**(5))/(b_f*l_caquot**(4)))))

    giros.append([giro_der,giro_izq])
    print(f" giros {giros} ")
    return [giro_der,giro_izq]

def puntual_interno():
    giros = []
    global a
    global b
    global p
    global l
    a=float(input("a[m]="))
    b=float(input("b[m]="))
    l=a+b
    p=float(input("q[kN]="))
    l_caquot= (a+b)*0.8
    b_inicial=b
    b=l_caquot-a
    l=l_caquot
    giro_der=((p*a*b)/(6*l))*(b+l)
    b=b_inicial
    a=l_caquot-b
    giro_izq=((p*a*b)/(6*l))*(a+l)
    giros.append([giro_der,giro_izq])
    print(f" giros {giros} ")
    return [giro_der,giro_izq]

def datos_trapezoidal():
    global a
    global b
    global c 
    global l
    global q1
    global q2
    global l

    

def datos_puntual():
    global a
    global b
    global p
    global l
    a=float(input("a[m]="))
    b=float(input("b[m]="))
    l=a+b
    p=float(input("q[kN]="))





inicio()

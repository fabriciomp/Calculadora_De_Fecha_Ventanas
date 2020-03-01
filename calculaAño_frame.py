

def ValidarCajasTexto(año, mes, dia):
    boolaño= año.isdigit()
    boolmes= mes.isdigit()
    booldia= dia.isdigit()

    if(boolaño==True and booldia==True and boolmes==True):
        return True
    else:
        return False

def Validar_Año(year):
    año= int(year)
    if año>=1900 and año<= 2099:
        return (True)
    else:
        return(False)
    
def Validar_Mes(mes):
    mes= int(mes)
    if mes>=1 and mes<= 12:
        return (True)
    else:
        return(False)

def Validar_dia(dia):
    dia = int(dia)
    if dia>=1 and dia<= 31:
        return (True)
    else:
        return(False)

def AñoIngresado(year): # INGRESA EL AÑO QUE RECIBE POR TECLADO Y DEVUELVE UN VALOR RELACIONADO AL AÑO Y UN RESIDUO
   
    año= int(year)
    restar=0
    if año>=1900 and año<=1999:
        new_Año=año - 1900
        residuo= new_Año//4
        restar= 0
    elif año>=2000 and año<= 2099:
            new_Año=año - 2000
            residuo= new_Año//4
            restar=-1
    return ([new_Año, residuo])


def Texto_Mes(mes):

    mes_Ingresado= int(mes)
    texto_Mes=""
    if mes_Ingresado==1:
        texto_Mes="Enero"
    elif mes_Ingresado==2:
        texto_Mes="Febrero"
    elif mes_Ingresado==3:
        texto_Mes="Marzo"
    elif mes_Ingresado==4:
        texto_Mes="Abril"
    elif mes_Ingresado==5:
        texto_Mes="Mayo"
    elif mes_Ingresado==6:
        texto_Mes="Junio"
    elif mes_Ingresado==7:
        texto_Mes="Julio"
    elif mes_Ingresado==8:
        texto_Mes="Agosto"
    elif mes_Ingresado==9:
        texto_Mes="Septiembre"
    elif mes_Ingresado==10:
        texto_Mes="Octubre"
    elif mes_Ingresado==11:
        texto_Mes="Noviembre"
    elif mes_Ingresado==12:
        texto_Mes="Diciembre"
    return(texto_Mes)


def Mes_Ingresado(mes): #RECIBE EL MES POR TECLADO Y LE ASIGNA EL CÓDIGO QUE DEBE MANEJAR CADA MES
                        #DEVUELVE DICHO CÓDIGO
    mes= int(mes)
    new_Mes=0
    if mes==1 or mes==10:#Enero u Octubre Representan 0
        new_Mes=0
    elif mes==2 or mes==3 or mes==11: #Febrero Marzo Noviembre Representan 3
            new_Mes=3
    if mes==4 or mes==7:    #aBRIL jULIO rEPRESENTAN 6
             new_Mes= 6
    elif mes==5:    #Mayo Representa 1
            new_Mes=1
    if mes==6: #Junio Representa 4
            new_Mes=4
    elif mes==8: #agosto Representa 2
            new_Mes=2
    if mes==9 or mes==12:#septiembre diciembre Reprsentan 5
            new_Mes= 5
    return (new_Mes)                           


def Dia_Ingresado(dia): #RECIBE Y DEVUELVE EL DÍA LEIDO PERO COMO UN ENTERO NO COMO UN STR

     newDay= int(dia)
     return (newDay)

def Dia_Semana(dia_residuo):    #EN BASE AL RESIDUO CALCULADO ASIGNA EL DÍA DE LA SEMANA
    newDia=""
    if dia_residuo == 1:
        newDia="Lunes"
    elif dia_residuo== 2:
            newDia="Martes"
    if dia_residuo == 3 :
       newDia="Miercoles"
    elif dia_residuo== 4:
        newDia="Jueves"
    if dia_residuo == 5:
        newDia="Viernes"
    elif dia_residuo == 6:
        newDia="Sabado"
    if dia_residuo == 7 : 
        newDia="Domingo"
    
    return (newDia)

def Calclcular_Dia (año, mes, dia, residuo, añoReal, mesReal): #APLICA EL ALGORITMO PARA CALCULAR EL DÍA DE LA SEMAN
        
    #print(año,mes,dia,residuo, añoReal, mesReal)#debo comentar
    restaAño=0
    añoR=int(añoReal)
    mesR= int(mesReal)
    
    if añoR>=2000:
        if año%4==0:
           
            if mesR==1 or mesR==2:
                restaAño= -2
               # print("E1 y E2")  #ojo verifico si entro o no E1 o E2
            else :
                restaAño= -1
              #  print("E 3")    #ojo verifico si entro o no E3
    else :
            if año%4==0:
             #   print("E 4")    #ojo verifico si entro o no E4
                if mesR==1 or mesR==2:
                  restaAño= -1
             #     print("E 5")  #ojo verifico si entro o no E5
            else :
                restaAño= 0
             #   print("E 6")    #ojo verifico si entro o nO E6
 
    
    sumar=año+mes+dia+residuo
    #print ("la suma ",sumar)
    calc_dia= (sumar%7)
    #print("el residuo ",calc_dia)    
    calc_dia=calc_dia+restaAño
    if(calc_dia<0):
        if calc_dia==-1:
            calc_dia=6
        elif calc_dia==-2:
            calc_dia=5
    if(calc_dia==0):
        calc_dia=7
    #print(calc_dia)
      
    return Dia_Semana(calc_dia)





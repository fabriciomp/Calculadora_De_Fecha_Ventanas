from tkinter import ttk
from tkinter import *
import calculaAño_frame
import colorama

class EjecutaDia:
    
    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Calcula el día del Año')
        #self.wind.geometry('200x150')     #cambia el tamaño de la ventana
        #self.wind.propagate(0)
        
        
        frame = LabelFrame(self.wind, text = 'Calcula la fecha')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        colorama.init(convert=True)

        #año
        Label(frame, text = 'Año: ').grid(row = 1, column = 0)
        self.año = Entry(frame)
        self.año.focus()
        self.año.grid(row = 1, column = 1)
        
        #mes
        Label(frame, text = 'Mes: ').grid(row = 2, column = 0)
        self.mes = Entry(frame)
        self.mes.grid(row = 2, column = 1)

        #dia
        Label(frame, text = 'Día: ').grid(row = 3, column = 0)
        self.dia = Entry(frame)
        self.dia.grid(row = 3, column = 1)

        #Boton Calcular Fecha
        ttk.Button(frame, text = 'Calcular', command = self.calcAño).grid(row = 4, columnspan = 2, sticky = W + E)
        
        #respuesta
        self.respuesta = Entry(frame)
        self.respuesta.grid(row = 5, column = 0, sticky= W + E)
        self.respuesta.grid_forget()

        self.respuesta2 = Entry(frame)

        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 7, column = 0, columnspan = 1, sticky = W + E)

    def validation(self):
        return len(self.año.get()) != 0 and len(self.mes.get()) != 0 and len(self.dia.get()) != 0

    
    def calcAño(self):
        
        if self.validation():
            var_Año=self.año.get()
            var_mes=self.mes.get()
            var_Dia=self.dia.get()
            boolCajasdeTexto = calculaAño_frame.ValidarCajasTexto(var_Año, var_mes, var_Dia)    
            
            if boolCajasdeTexto == True:
                if calculaAño_frame.Validar_Año(var_Año)==True and calculaAño_frame.Validar_Mes(var_mes)== True and calculaAño_frame.Validar_dia(var_Dia)==True:
                    año_Residuo_Año= calculaAño_frame.AñoIngresado(var_Año) #devuelve el año el residuo y el valor a restar
                    mes_devuelto = calculaAño_frame.Mes_Ingresado(var_mes)#devuelve  codigo de mes 033615 625035
                    dia_Devuelto = calculaAño_frame.Dia_Ingresado(var_Dia)
                    mes_en_Texto= calculaAño_frame.Texto_Mes(var_mes)

                    dia_Mostrar =calculaAño_frame.Calclcular_Dia(año_Residuo_Año[0], mes_devuelto, dia_Devuelto,año_Residuo_Año[1],var_Año,var_mes)
                    presentar=f"El día {var_Dia} de {mes_en_Texto} de {var_Año} cayo un "+dia_Mostrar
                        
                    self.message['text'] = f' El día {var_Dia} de {mes_en_Texto} de {var_Año} fue un {dia_Mostrar}'
                    self.respuesta.grid(row = 5, column = 0, columnspan = 5,sticky= W + E)
                    self.respuesta2.grid(row = 6, column = 0, columnspan = 5,sticky= W + E)
                        
                    self.respuesta.insert(0,f"El día {var_Dia} de {mes_en_Texto} de ")
                    self.respuesta2.insert(0,f"{var_Año} fue un {dia_Mostrar}")
                else:
                    self.message['text'] = 'Ingrese una fecha valida'    
            else:
                self.message['text'] = 'Ingrese sólo números'    
            
        else:
            self.message['text'] = 'Rellene todos los campos'
      
       
if __name__ == '__main__':
    window = Tk()
    application = EjecutaDia(window)
    window.mainloop()
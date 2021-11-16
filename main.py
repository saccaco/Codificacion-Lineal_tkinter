from tkinter import Frame, Entry, IntVar, StringVar, Label, Radiobutton, Button, Tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from codificaciones import *

class App(Frame):
    def __init__(self, ventana, *args, **kwargs):
        super().__init__(ventana, *args, **kwargs)

        self.frame1=Frame(ventana, bg='#4AFFFC',bd=12,relief='sunken') #titulo principal
        self.frame1.config(height=100,width=920,bd=12,relief='sunken')
        self.frame1.grid(row=0,column=0, columnspan=3, sticky='nsew')
        self.frame2=Frame(ventana, bg='#4365FE',bd=12,relief='sunken') #seleccion de botones
        self.frame2.config(height=200,width=200,bd=12,relief='sunken')
        self.frame2.grid(row=1,column=0, sticky='nsew')
        self.frame3=Frame(ventana, bg='#24CF1E',bd=12,relief='sunken') #entrada de datos
        self.frame3.config(height=230,width=250,bd=12,relief='sunken')
        self.frame3.grid(row=2,column=0, sticky='nsew')
        self.frame5=Frame(ventana, bg='#4365FE',bd=12,relief='sunken')
        self.frame5.grid(row=1,column=1, sticky='nsew', rowspan=2)
        self.frame4=Frame(ventana, bg='gray',bd=12,relief='sunken') #imagen
        self.frame4.config(height=320,width=600,bd=12,relief='sunken')
        self.frame4.grid(row=1,column=2, sticky='nsew', rowspan=2)

        self.ventana=ventana
        self.opcion=IntVar()
        self.datos=StringVar()
        self.tiempo=StringVar()
        self.amplitud=StringVar()
        self.amplitud_0=StringVar()
        self.amplitud_1=StringVar()

        self.create_widgets()
    
    def create_widgets(self):
        #añadiendo imagenes en la ventana principal
        self.imagen_1=ImageTk.PhotoImage(Image.open(r'codificacion-linea-Uni/fiee.png').resize((60,60))) #fiee
        Label(image=self.imagen_1, master=self.frame1,bg='#4AFFFC').grid(row=0,column=0)
        #recordar la forma de declarar
        self.imagen_2=ImageTk.PhotoImage(Image.open(r'codificacion-linea-Uni/uni.png').resize((60,60))) #uni
        Label(image=self.imagen_2, master=self.frame1,bg='#4AFFFC').grid(row=0,column=4, columnspan=5)
        #titulo principal
        text_prin=' C O D I F I C A C I Ó N \t D E \t L I N E A'
        Label(self.frame1, text=text_prin, font=('Orbitron',15, 'bold'),bg='#4AFFFC').grid(row=0,column=1,columnspan=3)
        #etiquetas para ENTRY
        texto_dato='Ingresa los datos (BITs):'
        Label(self.frame3, text=texto_dato,font=('Orbitron',12, 'bold'), bg='#24CF1E', fg='black').grid(row=0,column=0,pady=11)
        texto_tiempo='Ingresa el tiempo de bit (s):'
        Label(self.frame3, text=texto_tiempo, font=('Orbitron',12, 'bold'),bg='#24CF1E', fg='black').grid(row=1,column=0,pady=11)
        texto_amplitud='Ingresa la amplitud (m):'
        Label(self.frame3, text=texto_amplitud,font=('Orbitron',12, 'bold'),bg='#24CF1E', fg='black').grid(row=2,column=0,pady=11, padx=6)
        texto_amplitud0="Ingresa la amplitud del '0' (positivo):"
        Label(self.frame3, text=texto_amplitud0, font=('Orbitron',12, 'bold'),bg='#24CF1E', fg='black').grid(row=3,column=0,pady=11, padx=6)
        texto_amplitud1="Ingresa la amplitud del '1' (negativo):"
        Label(self.frame3, text=texto_amplitud1, font=('Orbitron',12, 'bold'),bg='#24CF1E', fg='black').grid(row=4,column=0,pady=11, padx=6)

        #configuración de los botones RadioButton
        Radiobutton(self.frame2,text='NRZ',bg='#4365FE',value=1, font=('Orbitron',12, 'bold'),variable=self.opcion).grid(row=0,column=0,padx=30, pady=10)
        Radiobutton(self.frame2,text='NRZ-L',bg='#4365FE',value=2,font=('Orbitron',12, 'bold'),variable=self.opcion).grid(row=0,column=1,padx=30, pady=10)
        Radiobutton(self.frame2,text='NRZ-I',bg='#4365FE',value=3,font=('Orbitron',12, 'bold'),variable=self.opcion).grid(row=1,column=0,padx=30, pady=10)
        Radiobutton(self.frame2,text='BIPOLAR\nMANCHESTER',bg='#4365FE',value=4,font=('Orbitron',12, 'bold'),variable=self.opcion).grid(row=1,column=1,padx=30, pady=10)
        Radiobutton(self.frame2,text='BIPOLAR\nAMI',bg='#4365FE',value=5,font=('Orbitron',12, 'bold'),variable=self.opcion).grid(row=2,column=0,padx=30, pady=15)
        #campos para ingresar datos
        Entry(self.frame3, textvariable=self.datos, bd=5).grid(column=1,row=0, padx=2) #dato
        Entry(self.frame3, textvariable=self.tiempo, bd=5).grid(column=1,row=1) #tiempo
        #boton para la selección
        Button(self.frame5, text='Seleccionar\nCodificación', command=self.resultado,bg='#E91BE2').grid(row=0,column=0, pady=15)
        #boton para graficar
        Button(self.frame5, text='Graficar', command=self.graficando,bg='#E91BE2').grid(row=1,column=0,pady=15)
        #boton para salir
        Button(self.frame5, text='salir',command=self.ventana.quit,bg='#E91BE2').grid(row=2,column=0,pady=15)
    
    def resultado(self):
        if self.opcion.get()==1:
            Entry(self.frame3, textvariable=self.amplitud, bd=5).grid(row=2,column=1, padx=8) #amplitud
            Entry(self.frame3, textvariable=self.amplitud_0, bd=5,state='disable').grid(row=3,column=1) #amplitud0
            Entry(self.frame3, textvariable=self.amplitud_1, bd=5,state='disable').grid(row=4,column=1) #amplitud1
        else:
            Entry(self.frame3, textvariable=self.amplitud, bd=5,state='disable').grid(row=2,column=1, padx=8) #amplitud
            Entry(self.frame3, textvariable=self.amplitud_0, bd=5).grid(row=3,column=1) #amplitud0
            Entry(self.frame3, textvariable=self.amplitud_1, bd=5).grid(row=4,column=1) #amplitud1
    
    def espectro_graf(self,eje_x,lista,eje_frec,magnitud_1):
        self.titulo={1:'NRZ no retorno a cero',2:'NRZ-L',3:'NRZ-I',4:'MANCHESTER', 5:'AMI'}
        fig, ax=plt.subplots(2,1,figsize=(4.5,4.5),facecolor='gray')
        plt.title('Codificación', color='white')
        ax[0].set_title(self.titulo[self.opcion.get()])
        ax[0].plot(eje_x,lista,label='Señal digital',color='r')
        ax[0].set_xlabel('Tiempo (s)')
        ax[0].set_ylabel('amplitud (m)')
        ax[0].legend(loc='best')
        ax[0].grid()

        ax[1].set_title('Espectro de Frecuencia')
        ax[1].plot(eje_frec,magnitud_1,label='FFT',color='b')
        ax[1].set_xlim(-3*max(eje_frec)/16,3*max(eje_frec)/16)
        ax[1].set_xlabel('Frecuencia (Hz)')
        ax[1].set_ylabel('Magnitud (m)')
        ax[1].legend(loc='best')
        ax[1].grid()
        fig.tight_layout()
        canva=FigureCanvasTkAgg(fig,master=self.frame4) #crea el area de dibujo en tkinter
        canva.draw()
        canva.get_tk_widget().grid(row=0,column=0,columnspan=2,pady=15)

    def graficando(self):
        self.datos_1=eval(self.datos.get())
        self.t_b=eval(self.tiempo.get())
        obj1=codificador(self.datos_1,self.t_b)
        if self.opcion.get()==1:
            ampl=eval(self.amplitud.get())
            eje_x,lista,eje_frec,magnitud_1=obj1.cod_nrz(ampl)
            self.espectro_graf(eje_x,lista,eje_frec,magnitud_1)
        elif self.opcion.get()==2:
            a_0=eval(self.amplitud_0.get())
            a_1=eval(self.amplitud_1.get())
            eje_x,lista,eje_frec,magnitud_1=obj1.cod_nrz_L(a_0,a_1)
            self.espectro_graf(eje_x,lista,eje_frec,magnitud_1)
        elif self.opcion.get()==3:
            a_0=eval(self.amplitud_0.get())
            a_1=eval(self.amplitud_1.get())
            eje_x,lista,eje_frec,magnitud_1=obj1.cod_nrz_I(a_0,a_1)
            self.espectro_graf(eje_x,lista,eje_frec,magnitud_1)
        elif self.opcion.get()==4:
            a_0=eval(self.amplitud_0.get())
            a_1=eval(self.amplitud_1.get())
            eje_x,lista,eje_frec,magnitud_1=obj1.cod_bipolar(a_0,a_1)
            self.espectro_graf(eje_x,lista,eje_frec,magnitud_1)
        else:
            a_pos=eval(self.amplitud_0.get())
            a_neg=eval(self.amplitud_1.get())
            eje_x,lista,eje_frec,magnitud_1=obj1.cod_bipolar_ami(a_pos,a_neg)
            self.espectro_graf(eje_x,lista,eje_frec,magnitud_1)
def main():
    ventana=Tk()
    ventana.wm_title('UNI')
    ventana.config(bg='#4365FE',bd=12,relief='sunken')
    ventana.geometry('1050x588')
    ventana.resizable(0,0)
    gui=App(ventana)
    gui.mainloop()

if __name__ == "__main__":
    main()
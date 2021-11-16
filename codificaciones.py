import scipy.fftpack as fourier
import numpy as np
class codificador():
    def __init__(self,datos,t_b):
        self.datos=datos
        self.t_b=t_b
    
    def cod_nrz(self,ampl):
        lista=[]
        for i in self.datos:
            if i==0:
                lista +=[0]*100
            else:
                lista +=[ampl]*100
        lista=np.array(lista)
        eje_x=np.linspace(0,len(self.datos)*self.t_b,lista.shape[0])

        t_s=self.t_b/99
        k=len(lista)
        señal_freq=fourier.fft(lista,k)*(1/k)
        magnitud_1=abs(señal_freq)

        eje_frec=fourier.fftfreq(k,t_s)
        eje_frec=fourier.fftshift(eje_frec)
        magnitud_1=fourier.fftshift(magnitud_1)
        return eje_x, lista, eje_frec, magnitud_1
    
    def cod_nrz_L(self,a_0,a_1):
        lista=[]

        for i in self.datos:
            if i == 0:
                lista+=[a_0]*100
            else:
                lista+=[a_1]*100

        lista=np.array(lista)
        eje_x=np.linspace(0,len(self.datos)*self.t_b,lista.shape[0])

        t_s=self.t_b/99
        k=len(lista)
        señal_freq=fourier.fft(lista,k)*(1/k)
        magnitud_1=abs(señal_freq)

        eje_frec=fourier.fftfreq(k,t_s)
        eje_frec=fourier.fftshift(eje_frec)
        magnitud_1=fourier.fftshift(magnitud_1)
        return eje_x, lista, eje_frec, magnitud_1
    
    def cod_nrz_I(self,a_0,a_1):
        lista=[]

        if self.datos[0]==0:
            lista+=[a_0]*100
        else:
            lista+=[a_1]*100

        for i in range(len(self.datos)-1):
            if self.datos[i+1]==1:
                if lista[100*i+99]==a_0:
                    lista+=[a_1]*100
                else:
                    lista+=[a_0]*100
            else:
                if lista[100*i+99]==a_0:
                    lista+=[a_0]*100
                else:
                    lista+=[a_1]*100

        lista=np.array(lista)
        eje_x=np.linspace(0, len(self.datos)*self.t_b, lista.shape[0])

        t_s=self.t_b/99
        k=len(lista)
        señal_freq=fourier.fft(lista,k)*(1/k)
        magnitud_1=abs(señal_freq)

        eje_frec=fourier.fftfreq(k,t_s)
        eje_frec=fourier.fftshift(eje_frec)
        magnitud_1=fourier.fftshift(magnitud_1)
        return eje_x, lista, eje_frec, magnitud_1
    
    def cod_bipolar(self,a_0,a_1):
        lista=[]

        for i in self.datos:
            if i==0:
                lista+=[a_0]*50+[a_1]*50
            else:
                lista+=[a_1]*50+[a_0]*50

        lista=np.array(lista)
        eje_x=np.linspace(0,len(self.datos)*self.t_b,lista.shape[0])

        t_s=self.t_b/99
        k=len(lista)
        señal_freq=fourier.fft(lista,k)*(1/k)
        magnitud_1=abs(señal_freq)

        eje_frec=fourier.fftfreq(k,t_s)
        eje_frec=fourier.fftshift(eje_frec)
        magnitud_1=fourier.fftshift(magnitud_1)
        return eje_x, lista, eje_frec, magnitud_1
    
    def cod_bipolar_ami(self,a_pos,a_neg):
        lista=[]

        for i in self.datos:
            if i==1:
                valor=self.datos.index(i)
                lista+=[a_pos]*100
                break
            else:
                lista+=[0]*100
        
        for i in range(valor, len(self.datos)-1):
            if self.datos[i+1]==0:
                lista+=[0]*100
            else:
                refer=self.datos.index(1,valor,i+1)
                if lista[100*refer+99]==a_pos:
                    lista+=[a_neg]*100
                else:
                    lista+=[a_pos]*100
                valor=i+1

        lista=np.array(lista)
        eje_x=np.linspace(0,len(self.datos)*self.t_b,lista.shape[0])

        t_s=self.t_b/99
        k=len(lista)
        señal_freq=fourier.fft(lista,k)*(1/k)
        magnitud_1=abs(señal_freq)

        eje_frec=fourier.fftfreq(k,t_s)
        eje_frec=fourier.fftshift(eje_frec)
        magnitud_1=fourier.fftshift(magnitud_1)
        return eje_x, lista, eje_frec, magnitud_1

import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import ttk


from djitellopy import Tello
from time import sleep

class Ventana_Principal:

    def __init__(self):
        # Instanciar el dron
        self.dron = Mi_Dron()

        self.ventana = tk.Tk()
        self.ventana.geometry("500x700")
        self.ventana.resizable(0, 0)

        # zona plan de vuelo
        self.ventana.title("PYTHON AVANZADO FEVAL 2021")
        self.txt_plan = tk.Label(self.ventana, text="PLAN DE VUELO")
        self.txt_plan.grid(column=0, row=0)
        self.scrolledtext1 = st.ScrolledText(self.ventana, width=50, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10, sticky="w")
        self.botonCargar = tk.Button(self.ventana, text="  Cargar  ", fg="Blue", command=self.cargar)
        self.botonCargar.grid(column=0, row=3, sticky="w", padx=10, pady=10)
        self.botonEjecutar = tk.Button(self.ventana, text="  Ejecutar  ", fg="Blue", command=self.ejecutar)
        self.botonEjecutar.grid(column=0, row=3, sticky="e", padx=10, pady=0)

        # zona control
        self.frame_control()

        # ventana de STATUS
        self.scrolledtext2 = st.ScrolledText(self.ventana, width=50, height=10)
        self.scrolledtext2.grid(column=0, row=12, padx=10, pady=150)
        self.scrolledtext2.place(x=10, y=500)
        self.scrolledtext2.delete("1.0", tk.END)




        # BUCLE PRINCIPAL
        self.ventana.mainloop()

    def frame_control(self):
            self.txt_manual = tk.Label(self.ventana, text="___________________CONTROL MANUAL____________________")
            self.txt_manual.grid(column=0, row=4)
            self.labelframe=ttk.LabelFrame(self.ventana, text="Control Manual")
            self.labelframe.grid(column=0, row=5, padx=5, pady=5, sticky="w")
            self.boton_subir=ttk.Button(self.ventana, text="S U B I R", command=self.subir)
            self.boton_subir.place(x=30, y=300, width=110, height=30)
            self.boton_bajar=ttk.Button(self.ventana, text="B A J A R", command=self.bajar)
            self.boton_bajar.place(x=220, y=300, width=110, height=30)
            self.boton_izquierda=ttk.Button(self.ventana, text="IZQUIERDA", command=self.izquierda)
            self.boton_izquierda.place(x=30, y=350, width=110, height=30)
            self.boton_derecha=ttk.Button(self.ventana, text="DERECHA", command=self.derecha)
            self.boton_derecha.place(x=220, y=350, width=110, height=30)
            self.boton_adelante=ttk.Button(self.ventana, text="ADELANTE", command=self.adelante)
            self.boton_adelante.place(x=30, y=400, width=110, height=30)
            self.boton_atras=ttk.Button(self.ventana, text="ATRAS", command=self.atras)
            self.boton_atras.place(x=220, y=400, width=110, height=30)
            self.boton_g_izq = ttk.Button(self.ventana, text="Giro IZQUIERDA", command=self.giro_izquierda)
            self.boton_g_izq.place(x=30, y=450, width=110, height=30)
            self.boton_g_der = ttk.Button(self.ventana, text="Giro DERECHA", command=self.giro_derecha)
            self.boton_g_der.place(x=220, y=450, width=110, height=30)
            self.boton_conectar=ttk.Button(self.ventana, text="CONECTAR", command=self.conectar)
            self.boton_conectar.place(x=380, y=300, width=110, height=30)
            self.boton_despegar=ttk.Button(self.ventana, text="<TAKE OFF>", command=self.despegar)
            self.boton_despegar.place(x=380, y=400, width=110, height=30)
            self.boton_aterrizar=ttk.Button(self.ventana, text="<L A N D>", command=self.aterrizar)
            self.boton_aterrizar.place(x=380, y=450, width=110, height=30)



    def mostrar_status(self):
        self.scrolledtext2.delete("1.0", tk.END)
        self.scrolledtext2.insert("1.0", self.dron.mostrar_estado())

    def ejecutar(self):
        comandos = self.scrolledtext1.get(0.0, 20.20)
        lista_comandos = []
        lista_comandos = comandos.split('\n')
        for indice in lista_comandos:
            cmd = indice.upper()
            if cmd == 'ADELANTE':
                self.dron.adelante_plan()
            elif cmd == 'ATRAS':
                self.dron.atras_plan()
            elif cmd == 'GIRODERECHA':
                self.dron.giro_der_plan()
            elif cmd == 'GIROIZQUIERDA':
                self.dron.giro_izq_plan()
            elif cmd == 'IZQUIERDA':
                self.dron.izquierda_plan()
            elif cmd == 'DERECHA':
                self.dron.derecha_plan()
            elif cmd == 'TAKEOFF':
                self.dron.takeoff_plan()
            elif cmd == 'LAND':
                self.dron.land_plan()
            elif cmd == 'SUBIR':
                self.dron.subir_plan()
            elif cmd == 'BAJAR':
                self.dron.bajar_plan()
            else:
                pass

    def conectar(self):
        self.scrolledtext2.insert("1.0", 'INTENTANDO CONECTAR CON EL DRON ESPERE...')
        self.dron.conectar()
        self.mostrar_status()

    def cargar(self):
        self.estado = 'Cargando fichero <comandos.txt>, espere por favor...'
        self.mostrar_status()
        self.scrolledtext1.delete("1.0", tk.END)
        f = open('plandevuelo.txt', 'r')
        datos = ''
        try:
            for linea in f:
                datos += linea
        finally:
            f.close()
            self.scrolledtext1.insert("1.0", datos)
    def subir(self):
        self.dron.subir()
        self.mostrar_status()
    def bajar(self):
        self.dron.bajar()
        self.mostrar_status()
    def izquierda(self):
        self.dron.izquierda()
        self.mostrar_status()
    def derecha(self):
        self.dron.derecha()
        self.mostrar_status()
    def adelante(self):
        self.dron.adelante()
        self.mostrar_status()
    def atras(self):
        self.dron.atras()
        self.mostrar_status()
    def giro_derecha(self):
        self.dron.giro_derecha()
        self.mostrar_status()
    def giro_izquierda(self):
        self.dron.giro_izquierda()
        self.mostrar_status()
    def despegar(self):
        self.dron.takeoff()
        self.mostrar_status()
    def aterrizar(self):
        self.dron.land()
        self.mostrar_status()

class Mi_Dron():

    def __init__(self):
        self.tello = Tello()
        self.estado = 'Desconectado'
        self.conectado = False

    def conectar(self):
        # conectar con el dron
        try:
            self.tello.connect()
        except:
             self.estado = 'PROBLEMAS CONEXION DRON...'
             self.conectado = False

        else:
            self.conectado = True
            self.estado = 'DRON CONECTADO...'


    def takeoff(self):
        self.estado = 'DESPEGANDO...'
        if self.conectado:
            self.tello.takeoff()
            sleep(5)
            self.estabilizar()

    def land(self):
        self.estado = 'ATERRIZANDO...'
        if self.conectado:
            self.tello.land()

    def subir(self):
        self.estado = 'SUBIENDO...'
        if self.conectado:
            self.tello.send_rc_control(0, 0, 50, 0)
            sleep(3)
            self.estabilizar()

    def adelante(self):
        self.estado = 'ADELANTE...'
        if self.conectado:
            self.tello.send_rc_control(0, 50, 0, 0)
            sleep(3)
            self.estabilizar()

    def atras(self):
        self.estado = 'ATRAS...'
        if self.conectado:
            self.tello.send_rc_control(0, -50, 0, 0)
            sleep(3)
            self.estabilizar()

    def bajar(self):
        self.estado = 'BAJANDO...'
        if self.conectado:
            self.tello.send_rc_control(0, 0, -50, 0)
            sleep(3)
            self.estabilizar()

    def derecha(self):
        self.estado = 'DERECHA...'
        if self.conectado:
            self.tello.send_rc_control(50, 0, 0, 0)
            sleep(3)
            self.estabilizar()

    def izquierda(self):
        self.estado = 'IZQUIERDA...'
        if self.conectado:
            self.tello.send_rc_control(-50, 0, 0, 0)
            sleep(3)
            self.estabilizar()

    def giro_derecha(self):
        self.estado = 'GIRO DERECHA...'
        if self.conectado:
            self.tello.send_rc_control(0, 0, 0, 45)
            sleep(3)
            self.estabilizar()

    def giro_izquierda(self):
        self.estado = 'GIRO IZQUIERDA...'
        if self.conectado:
            self.tello.send_rc_control(0, 0, 0, -45)
            sleep(3)
            self.estabilizar()

    def estabilizar(self):
        self.tello.send_rc_control(0, 0, 0, 0)

    def adelante_plan(self):
        self.tello.send_rc_control(0, 50, 0, 0)
        sleep(5)

    def atras_plan(self):
        self.tello.send_rc_control(0, -50, 0, 0)
        sleep(5)

    def giro_der_plan(self):
        self.tello.send_rc_control(0, 0, 0, 45)
        sleep(3)

    def giro_izq_plan(self):
        self.tello.send_rc_control(0, 0, 0, -45)
        sleep(3)

    def izquierda_plan(self):
        self.tello.send_rc_control(0, -50, 0, 0)
        sleep(5)

    def derecha_plan(self):
        self.tello.send_rc_control(0, -50, 0, 0)
        sleep(5)

    def takeoff_plan(self):
        self.tello.takeoff()
        sleep(3)

    def land_plan(self):
        self.tello.land()
        sleep(3)

    def subir_plan(self):
        self.tello.send_rc_control(0, 0, 50, 0)
        sleep(5)

    def bajar_plan(self):
        self.tello.send_rc_control(0, 0, -50, 0)
        sleep(5)

    def mostrar_estado(self):
        datos = 'ESTADO : ' + self.estado.upper() + '\n'
        if self.conectado:
            datos += 'Batería: ' + str(self.tello.get_battery()) + '\n'
            datos += 'Altitud: ' + str(self.tello.get_barometer()) + '\n'
            datos += 'Temperatura: ' + str(self.tello.get_temperature()) + '\n'
            datos += 'Velocidad X: ' + str(self.tello.get_speed_x()) + '\n'
            datos += 'Velocidad Y: ' + str(self.tello.get_speed_y()) + '\n'
            datos += 'Velocidad Z: ' + str(self.tello.get_speed_z()) + '\n'
        return (datos)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ventana_principal = Ventana_Principal()



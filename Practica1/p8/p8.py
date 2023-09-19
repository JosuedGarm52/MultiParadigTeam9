#libreria random
import random

#clase para crear usuarios

class Usuario:
    def __init__(self, usuario, contrasena, rol, nombre, curp, ciudad) -> None:
        self._usuario = usuario
        self._contrasena = contrasena
        self._rol = rol
        self._nombre = nombre
        self._curp = curp
        self._ciudad = ciudad
#propiedades necesarias para la comprobacion de informacion, solo mostrar
    @property
    def usuario(self):
        return self._usuario
    @property
    def contrasena(self):
        return self._contrasena
    @property
    def rol(self):
        return self._rol
    def __str__(self) -> str:
        return f"{self._usuario}, {self._contrasena}, {self._rol}, {self._nombre}, {self._curp}, {self._ciudad}"

#self, usuario, contrasena, rol, nombre, curp, ciudad
#usuarios base para iniciar el admin y un cliente
miUsuario = Usuario("alex", "nan", "admin", "alejandro", "DIM", "NLD")
dicUsuarios = {0:miUsuario,}
miUsuario = Usuario("ella", "nan", "cliente", "alejandro", "DIMas", "NLD")
dicUsuarios[5]= miUsuario

def registrar():
    while True:
        usuario = input('Ingresa tu nuevo usuario: ')
        contrasena = input('Ingresa tu nueva contrasena: ')
        nombre = input('ingresa el nombre del usuario: ')
        while True:
            curp = input('ingresa la CURP del usuario: ')
            if curp in dicUsuarios:
                print('El usuario ya existe')
                continue
            else:
                break
        ciudad = input('ingresa la ciudad del usuario: ')
        print(usuario, contrasena, nombre, curp, ciudad)
        if usuario != None and contrasena != None and nombre != None and curp != None and ciudad != None:
            miUsuario = Usuario(usuario, contrasena, "cliente", nombre, curp, ciudad)
            key = 0
			#asignacion de llave para el diccionario random y evita repetidos 
			#para no modificar el valor
            while True:
                numRamdom = random.randint(0,100)
                if numRamdom in dicUsuarios:
                    continue
                else:
                    key = numRamdom
                    break
            dicUsuarios[key] = miUsuario
            break
        else:
            print('datos incorrectos')  
            res = int(input('deseas volver a registrarte?\n1.-Si\n2.-No'))
            if res == 1:
                continue
            else:
                break

def Iniciar():
    for k,v in dicUsuarios.items():
        print(k,v,"\n")
    bandera = True
    while bandera == True:
        usu = input('ingresa usuario: ')
        cont = input('ingresa contrasena: ')
        for k,v in dicUsuarios.items(): #primer ciclado para recorrer las cuentas
            if usu == v.usuario and cont == v.contrasena:
                if v.rol == 'admin':
                    for k2,v2 in dicUsuarios.items():#segundo diccionario para imprimir
						#en caso de ingresar con la cuenta admin
                        print(v2,"\n")
                    bandera = False
                    break
                else:
					#mensaje de ingreso
                    print(f'el usuario  "{v.usuario}"  ha logrado ingresar')
                    bandera = False
                    break
        if bandera == True:
            res = int(input('quieres volver a intentar\n1.-Si\n2.-No\nSeleccion: '))
            if res == 1:
                bandera = True
                continue
            else:
                bandera = False
                break
    return

#menu 
while True:
    res = int(input('Menu\n1.-Registro\n2.-Inicio de sesion\n3.-Salida\nseleccion: '))
    if res == 1:
        registrar()
    elif res == 2:
        Iniciar()
    else:
        quit()
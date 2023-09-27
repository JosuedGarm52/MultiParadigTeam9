
import random

class Usuario:
    def __init__(self, usuario, contrasena, rol, nombre, curp, ciudad) -> None:
        self._usuario = usuario
        self._contrasena = contrasena
        self._rol = rol
        self._nombre = nombre
        self._curp = curp
        self._ciudad = ciudad

    #propiedades esenciales para comparaciones    
    @property
    def usuario(self):
        return self._usuario
    @property
    def contrasena(self):
        return self._contrasena
    @property
    def rol(self):
        return self._rol
    
    #sobre-escritura del str (regresa todos los valores en una cadena)
    def __str__(self) -> str:
        return f"{self._usuario}, {self._contrasena}, {self._rol}, {self._nombre}, {self._curp}, {self._ciudad}"

#self, usuario, contrasena, rol, nombre, curp, ciudad

#empleamos un diccionario para controlar las cuentas por claves (key) randomizadas
miUsuario = Usuario("alex", "nan", "admin", "alejandro", "DIM", "NLD")
dicUsuarios = {0:miUsuario,}
miUsuario = Usuario("ella", "nan", "cliente", "alejandro", "DIMas", "NLD")
dicUsuarios[5]= miUsuario

def registrar():
    while True:
        usuario = input('Ingresa tu nuevo usuario: ')
        contrasena = input('Ingresa tu nueva contrasena: ')
        nombre = input('ingresa el nombre del usuario: ')
        bandera = 0
        while bandera == 0:
            curp = input('ingresa la CURP del usuario: ')
            for k,v in dicUsuarios.items():
                if v._curp == curp:
                    print('El usuario ya existe')
                    bandera=0
                    break
                else:
                    bandera = 1
        ciudad = input('ingresa la ciudad del usuario: ')
        # print(usuario, contrasena, nombre, curp, ciudad)
        if (usuario == None or contrasena == None or nombre == None or curp == None or ciudad == None) or (usuario == ''  or nombre == '' or curp == '' or ciudad == ''):
            print('\n      datos incorrectos!!!!\n')  
            res = int(input('deseas volver a registrarte?\n1.-Si\n2.-No\nSeleccion: '))
            if res == 1:
                continue
            else:
                break
        else:
            miUsuario = Usuario(usuario, contrasena, "cliente", nombre, curp, ciudad)
            key = 0
            while True:
                numRamdom = random.randint(0,100)
                if numRamdom in dicUsuarios:
                    continue
                else:
                    key = numRamdom
                    break
            dicUsuarios[key] = miUsuario
            break

def Iniciar():
    bandera = True
    while bandera == True:
        usu = input('ingresa usuario: ')
        cont = input('ingresa contrasena: ')
        for k,v in dicUsuarios.items():
            if usu == v.usuario and cont == v.contrasena: 
                if v.rol == 'admin':        #chequeo (admin o no)
                    print()
                    for k2,v2 in dicUsuarios.items(): #imprime valores mediante str
                        print(v2)
                    bandera = False
                    print()
                    break
                else: #usuario cliente imprime su informacion
                    print(v)
                    print(f'el usuario  "{v.usuario}"  ha logrado ingresar')
                    bandera = False
                    break
        if bandera == True: #en caso de error mostrar menu
            res = int(input('quieres volver a intentar\n1.-Si\n2.-No\nSeleccion: '))
            if res == 1:
                bandera = True
                continue
            else:
                bandera = False
                break
    return

#ciclado para recibir unicamente 3 respuestas
while True:
    try:
        res = int(input('Menu\n1.-Registro\n2.-Inicio de sesion\n3.-Salida\nseleccion: '))
        if res == 1:
            registrar()
        elif res == 2:
            Iniciar()
        elif res == 3:
            quit()
    except TypeError as err:
        print('ingrese unicamente valores del 1 al 3')
    except Exception as err:
        print(err)

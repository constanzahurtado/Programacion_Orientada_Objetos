# Usuario Registrado: (id_usuario, nombre_usuario, apellido_usuario, correo_usuario, contraseña, fecha_registro, historial_informes)
## Uso calculadora (más de 2 veces).
## Registro (historial) de cálculos.
## Emisión de informes.
## Sección de comentarios.
## En general: Acceso a recursos, formulario de consultas. 

# Usuario Anónimo: (Fecha_visita, duracion_visita, contador_uso_calculadora, consulta)
## Uso limitado calculadora (2 veces)
## En general: Acceso a recursos, formulario de consultas. 

# Usuario Administrador: (id_administrador, nombre_usuario, apellido_usuario, correo_usuario, contraseña, fecha_creacion, privilegios, historial_acciones)
## Manejo de Usuarios (Actualizar, agregar, eliminar)
## Manejo de base de datos de alimentos (Actualizar, agregar, eliminar)
## Manejo de consultas (formulario)
## Manejo de recursos realcionados a la normativa (Actualizar, agregar, eliminar)

class Usuario_Registrado: # Se crea una clase para un usuario registrado, con su respectivo constructor y atributos. 
    def __init__(self, id_usuario, nombre_usuario, apellido_usuario, correo_usuario, password_usuario, fecha_registro): 
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario
        self.correo_usuario = correo_usuario
        self.__password_usuario = password_usuario
        self.fecha_usuario = fecha_registro

    def ingresar(self): # Esta función simula un inicio de sesión, preguntando por el cooreo y contraseña.
        print(f"Ingrese nombre usuario: {self.correo_usuario}")
        print(f"Ingrese contraseña usuario: {self.__password_usuario}")

    def getPassword(self):        # método get para mostar la contraseña de usuario.
        return self.__password_usuario
        
    def setPassword(self):  # Este método simula un cambio de contraseña
        password2 = input("Ingrese su nueva password: ")      # método set para cambiar contraseña.
        self.__password_usuario = self.__password_usuario.replace(self.__password_usuario, password2)
        return "Nueva contraseña", self.__password_usuario

#Se crean 3 instancias de usuario registrado:

UsuarioRegistrado1 = Usuario_Registrado('15.123.258-8','Sergio','Herrea','sh@gmail.com','12345','12-10-2021')
UsuarioRegistrado2 = Usuario_Registrado('17.456.698-4','Ana','Rojas','ar@gmail.com','67789','08-10-2021')
UsuarioRegistrado3 = Usuario_Registrado('20.001.258-1','Ernesto','Arias','ea@gmail.com','14785','20-10-2021')

# Se llama a las funciones a través de una instancia de usuario registrado. 

print(UsuarioRegistrado1.ingresar())
print(UsuarioRegistrado1.getPassword()) 
print(UsuarioRegistrado1.setPassword()) 

class Usuario_Visita: # Se crea una clase para un usuario que sólo visita la página, con su respectivo constructor y atributos. 
    def __init__(self, fecha_visita, duracion_visita):
        self.fecha_visita = fecha_visita
        self.duracion_visita = duracion_visita
    
    def visita(self): # Se crea una fución para registrar la fecha y duración de la visita. 
        print(f"Fecha visita: {self.fecha_visita}")
        print(f"Duración visita: {self.fecha_visita}")

#Se crean 3 instancias de usuario visita:
 
UsuarioVisita1 = Usuario_Visita('01-10-2021', 15)
UsuarioVisita2 = Usuario_Visita('16-10-2021', 30)
UsuarioVisita3 = Usuario_Visita('22-10-2021', 5)

# Se llama a la función a través de una instancia de usuario visita. 

print(UsuarioVisita1.visita())

class Usuario_Administrador: # Se crea una clase para un usuario administrador, con su respectivo constructor y atributos. 
    def __init__(self, id_administrador, nombre_administrador, apellido_administrador, correo_administrador, password_administrador, fecha_creacion): 
        self.id_administrador = id_administrador
        self.nombre_administrador = nombre_administrador
        self.apellido_administrador = apellido_administrador
        self.correo_administrador = correo_administrador
        self.__password_administrador = password_administrador
        self.fecha_creacion = fecha_creacion  
       
    def mostrar_administrador(self): # Se crea una función que indica el nombre y fecha de creación de un administrador. 
        print(f"Nombre administrador: {self.nombre_administrador} {self.apellido_administrador}")
        print(f"Fecha de creación: {self.fecha_creacion}")
    
    def eliminar_administrador(self, id_administrador): # Con esta fución se simula la eliminación de un administrador. 
        lista_administradores = [UsuarioAdministrador1.id_administrador, UsuarioAdministrador2.id_administrador, UsuarioAdministrador3.id_administrador]
        lista_administradores.remove(id_administrador)
        return lista_administradores

#Se crean 3 instancias de administrador:

UsuarioAdministrador1 = Usuario_Administrador('18.123.369-4','Luisa','Torres','lt@gmail.com','asdfg','02-09-2021')
UsuarioAdministrador2 = Usuario_Administrador('17.123589-2','Antonio','Delgado','ad@gmail.com','qwerr','10-09-2021')
UsuarioAdministrador3 = Usuario_Administrador('19.258.369-1','Luciano','Cifuentes','lc@gmail.com','tyuio','27-09-2021')

# Se llama a las funciones a través de una instancia de administrador. 

print(UsuarioAdministrador1.mostrar_administrador())
print(UsuarioAdministrador1.eliminar_administrador('18.123.369-4'))

# OipassOnClick

OipassOnClick es una pequena aplicación (Cli) de Consola o Terminal que sirve como gestor de usuarios y passwords, nos permita hacer operaciones CRUD (Create, Read, Update, Delete) & Validaciones usando comandos y parametros.

Esta aplicacion cuenta con el paquete  pip llamado click, el cual nos facilita la creación de comandos y parámetros de terminal.
""   """""""""" """""  "" "" """"""" Passlib para encriptar los passwords con hash y verificarlos diciendonos si son correctas oh no nuestras contraseñas.


Para poder usar las funciones de esta aplicación se muestran aqui los siguientes comandos:


# Comandos Para Registrar Usuarios & Passwords

* python oipass.py newaccount --Account nuevo_usuario.2024@gmail.com --Password 12345

""" 
new account created with id : 5 
name: nuevo_usuario.2024@gmail.com
with hash: $2b$12$5TyvvGqFOGirVJDLJ6oFr.mGtE82mfmv7tIoVwvVE4RjTY9TVqq6W """

# Comando Para Consultar Usuarios

* python oipass.py accounts 

""" 
1 - Jesus - test
2 - maria - perez
3 - Jose - Mendoza
4 - Jhonn - Connor
5 - nuevo_usuario.2024@gmail.com - $2b$12$5TyvvGqFOGirVJDLJ6oFr.mGtE82mfmv7tIoVwvVE4RjTY9TVqq6W """

# Comando Para Actualizar Usuarios & Passwords

* python oipass.py update 1 --name nuevo_usuario_actualizado@hotmail.com --password 123

"""
User with id 5 updated successfully """

# Comando Para Validar Passwords & Usuarios

* python oipass.py user 1 12345 

"""
5 - nuevo_usuario_actualizado@hotmail.com -$2b$12$R5qrO5N2F.N7KVtK3lyX1O1ernA9LnF9TAXnUvy1RmpJiJgJ71mLi password incorrect """

* python oipass.py user 1 123

"""
5 - nuevo_usuario_actualizado@hotmail.com -$2b$12$R5qrO5N2F.N7KVtK3lyX1O1ernA9LnF9TAXnUvy1RmpJiJgJ71mLi password correct """

# Comandos Para Eliminar Usuario & Password

* python oipass.py delete 1

""
User with id 5 deleted successfully""
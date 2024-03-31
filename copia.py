#Importaciones Necesarias
import re #Para Usar Expresiones Regulares
import os #Para Manejar Archivos (Leer, Crear, Modificar, Borrar)

    #Tkinter
from tkinter import ttk #Biblioteca Para desarrollar la interfaz grafica
from tkinter import * #Llamado a todos los elementos de la interfaz grafica

    #Mensaje por Correo

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#Fin De Importaciones Necesarias

#Expresion Regulares
name_valid = re.compile(r'^[A-Za-záéíóúüñÁÉÍÓÚÜÑ ]+$')
lastname_valid = re.compile(r'^[A-Za-záéíóúüñÁÉÍÓÚÜÑ ]+$')
email_valid = re.compile(r'^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$')
age_valid = re.compile(r'^[1-9][0-9]?$|^100$')
gender_valid = re.compile(r'^[MFmf]$')
phone_valid = re.compile(r'^\d{10}$')
country_valid = re.compile(r'^[A-Za-záéíóúüñÁÉÍÓÚÜÑ ]+$')
#Fin De Expresion Regulares

#Class: Clases Para Obtener Todos Los Metodos De la Base de Datos, De mis Ventanas Y Mis Funciones.

class Register: #Desde aca iniciara El Registro

    DateBase = "Users.txt"

    #Funcion Para Ingresar Datos
    def __init__(self, window ): #Funcion Constructora
        self.wind = window #Wind = Ventana Principal
        self.wind.title("Registration Application For Users") #Titulo de la Ventana
        self.wind.configure(bg="#33C4FF")
        
        

        # Cuadro de Elementos
        frame = LabelFrame(self.wind, text="Registrar Usuario", padx=20, pady=10, bg="#f0f0f0",
                        font=("Arial", 14, "bold"))  # Cambiar el color de fondo y estilo del cuadro de elementos
        frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20)

        #Elementos
        #Name
        Label(frame, text="Name: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 1, column = 0) #Cuadro del Nombre posicionado
        self.name = Entry(frame) #Entrada Del Nombre
        self.name.focus() #El curso se posiciona en el label al ejecutarse el programa
        self.name.grid(row=1, column=1) #Entrada Del Nombre posicionado

        #Last Name
        Label(frame, text="Last Name: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 2, column = 0) #Cuadro del Apellido posicionado
        self.lastname = Entry(frame) #Entrada Del Apellido
        self.lastname.grid(row=2, column=1) #Entrada Del Apellido posicionado

        #Age
        Label(frame, text="Age: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 3, column = 0) #Cuadro del Edad posicionado
        self.age = Entry(frame, text="Age: ") #Entrada De la Edad
        self.age.grid(row=3, column=1) #Entrada De la Edad posicionado

        #Gender
        Label(frame, text="Gender: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 4, column = 0)
        self.gender = Entry(frame) #Entrada del Genero
        self.gender.grid(row = 4, column = 1) #Entrada del Genero posicionado

        #Country
        Label(frame, text = "Country: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 5, column = 0)
        self.country = Entry(frame) #Entrada del Pais
        self.country.grid(row = 5, column = 1) #Entrada del Pais posicionado

        #Email
        Label(frame, text= "Email: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 6, column = 0)
        self.email = Entry(frame) #Entrada del Email
        self.email.grid(row = 6, column = 1) #Entrada del Email posicionado

        #Phone
        Label(frame, text = "Phone: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 7, column = 0)
        self.phone = Entry(frame) #Entrada del Telefono
        self.phone.grid(row = 7, column = 1) #Entrada del Telefono posicionado

        #Botones
        ttk.Button(frame, text="Register", command=self.add_user, style='TButton').grid(row=8, columnspan=2, sticky=W + E, pady=10)
        ttk.Button(frame, text='Delete', command=self.delete, style='TButton').grid(row=11, column=0, pady=10)
        ttk.Button(frame, text='Edit', command=self.edit, style='TButton').grid(row=11, column=1, pady=10)
        ttk.Button(frame, text="View", command=self.view_user_details, style='TButton').grid(row=11, column=2, sticky=W + E, pady=10)


        #Mensaje despues del registro
        self.message = Label(frame, text='', fg='green', font=('Arial', 12), bg="#f0f0f0")
        self.message.grid(row=9, column=0, columnspan=2, sticky=W + E, pady=10)

        #Tabla para ver los usuarios registrado
        self.table = ttk.Treeview(height = 10, columns = 3)
        self.table.grid(row = 10, column = 0, columnspan = 2)
        self.table.heading("#0", text = "Users", anchor = CENTER)
        self.table.heading("#1", text = "Email", anchor = CENTER)

        self.get_register()
    #Fin de la Funcion Para Ingresar Datos



    #Funcion Para Manejar los Datos
    def base_datos(self, query, parametros = () ):
        if (self.DateBase):
            with open(self.DateBase, 'r') as archivo:
                users = archivo.read() 
                print(f"Usuarios registrados\n", users)
        else:
            print("Usuarios registrados", "No hay usuarios registrados.")
    #Fin de la Funcion Para Manejar los Datos

    #Funcion para visualizar los datos en una tabla
    def get_register(self):

        for row in self.table.get_children():
            self.table.delete(row)

        # Leer los datos del archivo de texto
        with open(self.DateBase, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                if len(datos) == 7:  # Verifica si hay suficientes campos (nombre, apellido, edad, género, país, email, teléfono)
                    # Obtén el nombre y el correo electrónico
                    nombre = datos[0].strip()
                    email = datos[5].strip()
                    # Inserta los datos en la tabla con dos columnas (nombre y correo)
                    self.table.insert('', 'end',text = nombre, values=( email))
    #Fin de la Funcion para visualizar los datos en una tabla


    #Funcion para validar cada valor obtenido de los frame (inputs)
    def validation(self):
        name = self.name.get()
        lastname = self.lastname.get()
        age = self.age.get()
        gender = self.gender.get()
        email = self.email.get()
        phone = self.phone.get()
        country = self.country.get()

        if name_valid.match(name) and lastname_valid.match(lastname) and email_valid.match(email) and age_valid.match(age) and gender_valid.match(gender) and phone_valid.match(phone) and country_valid.match(country):
            with open(self.DateBase, 'a') as archivo:
                archivo.write(f"{name},{lastname},{age},{gender},{country},{email},{phone}\n")
            self.message['text'] = (f"El Usuario {self.name.get()} {self.lastname.get()} Ha Sido Registrado")
            self.message['fg'] = 'green'
            self.get_register()
        else:
            self.message['text'] =  (f"El Usuario {self.name.get()} {self.lastname.get()}  NO Ha Sido Registrado")
            self.message['fg'] = 'red'
    #Fin de la Funcion para validar cada valor obtenido de los frame (inputs)
        

    #Funcion para agregar nuevos usuarios
    def add_user(self):
        # Obtener el correo electrónico del usuario registrado
        user_email = self.email.get()

        try:
            # Crear el mensaje de correo electrónico
            msg = MIMEMultipart()
            msg['From'] = 'gwilklert@gmail.com'  # Cambiar esto con tu dirección de correo
            msg['To'] = user_email
            msg['Subject'] = 'Registro exitoso'

            # Cuerpo del mensaje
            message_body = f'Hola {self.name.get()} {self.lastname.get()},\n\nGracias por registrarte. Tu información ha sido guardada correctamente.'

            # Agregar el cuerpo del mensaje al mensaje de correo
            msg.attach(MIMEText(message_body, 'plain'))

            # Configurar el servidor SMTP de Gmail
            smtp_server = 'smtp.gmail.com'
            smtp_port = 465

            # Iniciar una conexión segura (TLS) con el servidor SMTP de Gmail
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

            # Iniciar sesión en la cuenta de correo
            username = 'gwilklert@gmail.com'  # Cambiar esto con tu dirección de correo
            password = 'Yopuedocontodo.99'  # Cambiar esto con tu contraseña de correo
            server.login(username, password)

            # Enviar el mensaje
            server.sendmail(msg['From'], msg['To'], msg.as_string())

            # Cerrar la conexión con el servidor SMTP
            server.quit()

            # Mostrar un mensaje de éxito en la interfaz gráfica
            self.message['text'] = f"El Usuario {self.name.get()} {self.lastname.get()} Ha Sido Registrado y se ha enviado un correo a {user_email}"
            self.message['fg'] = 'green'

            # Actualizar la tabla con los nuevos datos
            self.get_register()

        except Exception as e:
            # Mostrar un mensaje de error en caso de que falle el envío del correo
            self.message['text'] = f"El Usuario {self.name.get()} {self.lastname.get()} Ha Sido Registrado, pero hubo un error al enviar el correo a {user_email}: {str(e)}"
            self.message['fg'] = 'red'
        
    #Fin de la Funcion para agregar nuevos usuarios

    #Funcion para eliminar los Usuarios
    def delete(self):
        try:
            select = self.table.selection()
            if select:
                selec_user = self.table.item(select, "text")
                with open(self.DateBase, "r") as archivo:
                    lines = archivo.readlines()

                with open(self.DateBase, "w") as archivo:
                    for line in lines:
                        datos = line.strip().split(",")
                        if datos[0].strip() != selec_user:
                            archivo.write(line)

                self.message['text'] = f"El Usuario {selec_user} ha sido eliminado."
                self.message['fg'] = 'red'
                
                # Actualizar la tabla sin el usuario eliminado
                self.get_register()
            else:
                self.message['text'] = 'Seleccione un usuario para eliminar.'
        except IndexError:
            self.message['text'] = 'Seleccione un usuario para eliminar.'
    #Fin Funcion para eliminar los Usuarios

    #Funcion para editar los usuarios
    def edit(self):
        try:
            select = self.table.selection()
            if select:
                selec_user = self.table.item(select, "text")
                with open(self.DateBase, "r") as archivo:
                    lines = archivo.readlines()

            # Buscar el usuario seleccionado en el archivo
            for index, line in enumerate(lines):
                datos = line.strip().split(",")
                if datos[0].strip() == selec_user:
                    # Obtener los valores del usuario seleccionado
                    name, lastname, age, gender, country, email, phone = datos

                    # Crear una nueva ventana para editar el usuario
                    edit_window = Toplevel()
                    edit_window.title("Editar Usuario")

                    # Elementos en la nueva ventana
                    Label(edit_window, text="Nombre: ").grid(row=0, column=0)
                    edit_name = Entry(edit_window)
                    edit_name.grid(row=0, column=1)
                    edit_name.insert(0, name)

                    Label(edit_window, text="Apellido: ").grid(row=1, column=0)
                    edit_lastname = Entry(edit_window)
                    edit_lastname.grid(row=1, column=1)
                    edit_lastname.insert(0, lastname)

                    Label(edit_window, text="Edad: ").grid(row=2, column=0)
                    edit_age = Entry(edit_window)
                    edit_age.grid(row=2, column=1)
                    edit_age.insert(0, age)

                    Label(edit_window, text="Género: ").grid(row=3, column=0)
                    edit_gender = Entry(edit_window)
                    edit_gender.grid(row=3, column=1)
                    edit_gender.insert(0, gender)

                    Label(edit_window, text="País: ").grid(row=4, column=0)
                    edit_country = Entry(edit_window)
                    edit_country.grid(row=4, column=1)
                    edit_country.insert(0, country)

                    Label(edit_window, text="Email: ").grid(row=5, column=0)
                    edit_email = Entry(edit_window)
                    edit_email.grid(row=5, column=1)
                    edit_email.insert(0, email)

                    Label(edit_window, text="Teléfono: ").grid(row=6, column=0)
                    edit_phone = Entry(edit_window)
                    edit_phone.grid(row=6, column=1)
                    edit_phone.insert(0, phone)

                    # Función para guardar los cambios
                    def save_changes():
                        # Obtener los valores editados
                        edited_name = self.edit_name.get()
                        edited_lastname = self.edit_lastname.get()
                        edited_age = self.edit_age.get()
                        edited_gender = self.edit_gender.get()
                        edited_country = self.edit_country.get()
                        edited_email = self.edit_email.get()
                        edited_phone = self.edit_phone.get()

                        # Reemplazar los valores en la lista
                        lines[index] = f"{edited_name}, {edited_lastname}, {edited_age}, {edited_gender}, {edited_country}, {edited_email}, {edited_phone}\n"

                        # Guardar los cambios en el archivo
                        with open(self.DateBase, "w") as archivo:
                            archivo.writelines(lines)

                        # Cerrar la ventana de edición
                        edit_window.destroy()

                        # Actualizar la tabla con los cambios
                        self.get_register()

                    # Botón para guardar los cambios
                    ttk.Button(edit_window, text="Guardar Cambios", command=save_changes).grid(row=7, columnspan=2)

                # Continuar buscando en caso de haber duplicados (mismo nombre)
                continue

            else:
                self.message['text'] = 'Seleccione un usuario para editar.'
        except IndexError:
            self.message['text'] = 'Seleccione un usuario para editar.'
    
    def view_user_details(self):
        try:
            select = self.table.selection()
            if select:
                selec_user = self.table.item(select, "text")
            with open(self.DateBase, "r") as archivo:
                lines = archivo.readlines()

            # Buscar el usuario seleccionado en el archivo
            for line in lines:
                datos = line.strip().split(",")
                if datos[0].strip() == selec_user:
                    name, lastname, age, gender, country, email, phone = datos

                    # Crear una nueva ventana para mostrar los detalles del usuario
                    view_window = Toplevel()
                    view_window.title("Detalles del Usuario")

                    # Mostrar los detalles del usuario en etiquetas de texto
                    Label(view_window, text=f"Nombre: {name}").pack()
                    Label(view_window, text=f"Apellido: {lastname}").pack()
                    Label(view_window, text=f"Edad: {age}").pack()
                    Label(view_window, text=f"Género: {gender}").pack()
                    Label(view_window, text=f"País: {country}").pack()
                    Label(view_window, text=f"Email: {email}").pack()
                    Label(view_window, text=f"Teléfono: {phone}").pack()
                    
                    break
            else:
                self.message['text'] = 'Seleccione un usuario para ver los detalles.'
        except IndexError:
            self.message['text'] = 'Seleccione un usuario para ver los detalles.'


#Para iniciar el programa
if __name__ == '__main__': 
    Window = Tk() #Creacion de la ventana principal
    Application =  Register(Window) #Creacion de la clase
    Window.mainloop() #Iniciar el programa





    
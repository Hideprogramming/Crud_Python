#Importaciones Necesarias
import re #Para Usar Expresiones Regulares
import os #Para Manejar Archivos (Leer, Crear, Modificar, Borrar)

    #Tkinter
from tkinter import ttk #Biblioteca Para desarrollar la interfaz grafica
from tkinter import * #Llamado a todos los elementos de la interfaz grafica
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
    def __init__(self, window): #Funcion Constructora
        self.wind = window #Wind = Ventana Principal
        self.wind.title("Registration Application For Users") #Titulo de la Ventana
        self.wind.minsize( height = 500, width = 600)
        self.wind.configure(bg="#33C4FF")



        # Cuadro de Elementos
        frame = LabelFrame(self.wind, text="Registrar Usuario", padx=20, pady=10, bg="#f0f0f0", font=("Arial", 14, "bold"))
        frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky="nsew")
        # Fin de Cuadro de Elementos

        # Responsive
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        # Fin de Responsive

        #Elementos
        #Name
        Label(frame, text="Name:", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=1, column=0, sticky="e") #Cuadro del Nombre posicionado
        self.name = Entry(frame) #Entrada Del Nombre
        self.name.focus() #El curso se posiciona en el label al ejecutarse el programa
        self.name.grid(row=1, column=1)#Entrada Del Nombre posicionado


        #Last Name
        Label(frame, text="Last Name: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 2, column = 0, sticky="e") #Cuadro del Apellido posicionado
        self.lastname = Entry(frame) #Entrada Del Apellido
        self.lastname.grid(row=2, column=1) #Entrada Del Apellido posicionado

        #Age
        Label(frame, text="Age: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 3, column = 0, sticky="e") #Cuadro del Edad posicionado
        self.age = Entry(frame, text="Age: ") #Entrada De la Edad
        self.age.grid(row=3, column=1) #Entrada De la Edad posicionado

        #Gender
        Label(frame, text="Gender: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 4, column = 0, sticky="e")
        self.gender = Entry(frame) #Entrada del Genero
        self.gender.grid(row = 4, column = 1) #Entrada del Genero posicionado

        #Country
        Label(frame, text = "Country: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 5, column = 0, sticky="e")
        self.country = Entry(frame) #Entrada del Pais
        self.country.grid(row = 5, column = 1) #Entrada del Pais posicionado

        #Email
        Label(frame, text= "Email: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 6, column = 0, sticky="e")
        self.email = Entry(frame) #Entrada del Email
        self.email.grid(row = 6, column = 1) #Entrada del Email posicionado

        #Phone
        Label(frame, text = "Phone: ",font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row = 7, column = 0, sticky="e")
        self.phone = Entry(frame) #Entrada del Telefono
        self.phone.grid(row = 7, column = 1) #Entrada del Telefono posicionado

        #Botones
        ttk.Button(frame, text="Register", command = self.add_user, style= '').grid(row=8, columnspan=2, sticky=W + E, pady=10)
        ttk.Button(frame, text='Delete', command = self.delete, style='TButton').grid(row=11, column=0, pady=10)
        ttk.Button(frame, text='Edit', command = self.edit, style='TButton').grid(row=11, column=1, pady=10)
        ttk.Button(frame, text="View", command = self.view_user_details, style='TButton').grid(row=11, column=2, sticky=W + E, pady=10)


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
    def base_datos(self):
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
                if len(datos) == 7:  # Verifica si hay suficientes campos 
                    # Obtén el nombre y el correo electrónico
                    nombre = datos[0].strip()
                    email = datos[5].strip()
                    
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
        if self.validation():
            with open(self.DateBase, 'a') as archivo:
                archivo.write(f"{self.name.get()}, {self.lastname.get()}, {self.age.get()},{self.gender.get()}, {self.country.get()}, {self.email.get()}, {self.phone.get()}\n")
            self.message['text'] = (f"El Usuario {self.name.get()} {self.lastname.get()} Ha Sido Registrado")
            self.message['fg'] = 'green'
        
            # Actualiza la tabla con los nuevos datos
            self.get_register()
        
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
                        self.edited_name = edit_name.get()
                        self.edited_lastname = edit_lastname.get()
                        self.edited_age = edit_age.get()
                        self.edited_gender = edit_gender.get()
                        self.edited_country = edit_country.get()
                        self.edited_email = edit_email.get()
                        self.edited_phone = edit_phone.get()

                        # Reemplazar los valores en la lista
                        lines[index] = f"{self.edited_name}, {self.edited_lastname}, {self.edited_age}, {self.edited_gender}, {self.edited_country}, {self.edited_email}, {self.edited_phone}\n"

                        # Guardar los cambios en el archivo
                        with open(self.DateBase, "w") as archivo:
                            archivo.writelines(lines)

                        # Cerrar la ventana de edición
                        edit_window.destroy()

                        # Actualizar la tabla con los cambios
                        self.get_register()

                    # Botón para guardar los cambios
                    ttk.Button(edit_window, text="Guardar Cambios", command = save_changes).grid( row = 7, columnspan = 2 )

                # Continuar buscando en caso de haber duplicados (mismo nombre)
                continue

            else:
                self.message['text'] = ' Usuario Seleccionado.'
        except IndexError:
            self.message['text'] = 'Seleccione un usuario para editar.'
    #Fin de la Funcion para editar los usuarios

    #Funcion para visualizar los usuarios
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
    #Fin de la Funcion para visualizar los usuarios

#Para iniciar el programa
if __name__ == '__main__': 
    Window = Tk() #Creacion de la ventana principal
    Application =  Register(Window) #Creacion de la clase
    Window.mainloop() #Iniciar el programa




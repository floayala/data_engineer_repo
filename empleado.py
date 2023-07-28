class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre # refiere a la variable de instancia 'nombre' de la clase Persona
        self.edad = edad
        
    def presentacion(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.puesto = puesto

    def presentacion(self):
        super().presentacion()
        print(f"Trabajo en el departamento de {self.departamento} en el puesto {self.puesto}")


nombre = 'Alberto' # 'nombre' es una variable local fuera del contexto de clases
edad = 24
departamento = 'Data'
puesto = 'Analyst'
my_var_list = ['Andrea', 42,'Ventas','Manager']
my_var_dict = {'nombre': 'Andrea','edad': 42,'departamento': 'Ventas','puesto': 'Manager'}
trabajador_1 = Trabajador(nombre, edad, departamento, puesto)
trabajador_1.presentacion()
trabajador_2 = Trabajador(*my_var_list)
trabajador_2.presentacion()
trabajador_3 = Trabajador(**my_var_dict)
trabajador_3.presentacion()
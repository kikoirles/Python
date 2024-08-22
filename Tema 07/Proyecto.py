# Creacion de clases para los datos solicitados
class Personas:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Personas):
    def __init__(self, nombre, apellido, numero_cuenta, saldo_cuenta = 0):
        super().__init__(nombre, apellido)              # añadir los dos atributos de la clase superior Perosnas
        self.numero_cuenta = numero_cuenta
        self.saldo_cuenta = saldo_cuenta

    def __str__(self):                                  # Metodo especialpermite definir la forma que devuelve un string
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero_cuenta: {self.numero_cuenta}\nSaldo_cuenta: {self.saldo_cuenta}"

    def depositar(self, cantidad):
        self.saldo_cuenta += cantidad
        print(f"Has depositado ${cantidad}.\n Nuevo balance: ${self.saldo_cuenta}.")

    def retirar(self, cantidad):
        if cantidad > self.saldo_cuenta:
            print("No se puede realizar dicha transaccion")
        else:
            self.saldo_cuenta -= cantidad
        print(f"Has retirado ${cantidad}.\n Nuevo balance: ${self.saldo_cuenta}.")

cliente_juan = Cliente("Juan","Pérez","123456789",1000)

# print(cliente_juan)

def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta_cl = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta_cl)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()

        if opcion == 'D':
            deposito = int(input("Importe a despositar: "))
            mi_cliente.depositar(deposito)

        elif opcion == 'R':
            retirado = int(input("Importe a retirar: "))
            mi_cliente.retirar(retirado)
        print(mi_cliente)

    print("Gracias por operar en Caja MAR2.0")

inicio()





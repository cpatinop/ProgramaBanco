# Primero creamos una clase de cuenta general dentro dentro de uestro programa

class Cuenta:
    def __init__(self,nombre,balance, balance_min ):
        self.nombre= nombre
        self.balance = balance
        self.balance_min =balance_min
        
    def deposito(self, monto):
        self.balance += monto

    def retiro(self, monto):
            if self.balance-monto >= self.balance_min:
                self.balance -= monto
            else:
                print("Lo siento, no hay dinero suficiente")

    def declaracion(self):
        print("Balance de la cuenta {}".format(self.balance))


# Segundo crearemos una clase para nuestra cuenta corriente

class Corriente(Cuenta):
    def __init__(self, nombre, balance):
        super().__init__ (nombre, balance, balance_min = -1000) 

    def str(self):
        return "Cuenta de {} - Balance de {}".format(self.nombre)


z = Corriente( "Juan", 500)
z.deposito(700)
z.retiro(1000)
z.declaracion()
print(z)
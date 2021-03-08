from models.cliente import Cliente
from models.conta import Conta


cliente1: Cliente = Cliente('João Carlos', 'joaocarlos@email.com', '123.456.789-87', '02/02/1999')
cliente2: Cliente = Cliente('Maria Joaquina', 'maria joaquina@email.com', '555.159.753-23', '06/03/1985')

print(cliente1)
print()
print(cliente2)
print()

contaj: Conta = Conta(cliente1)
contam: Conta = Conta(cliente2)

print(contaj)
print()
print(contam)

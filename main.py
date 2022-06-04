import string
import random
abc = string.ascii_lowercase
ABC = string.ascii_uppercase
nums = []
simbolos = ['!', '@', '#', '$', '%', '&', '/', '*']
def generar_contraseña(longitud):
		contraseña = ""
		for i in range (0, longitud):
			numoletra = random.randint(0, 2)
			if numoletra == 0:
				contraseña += random.choice(abc)
			elif numoletra == 1:
				contraseña += str(random.randint(0, 9))
			elif numoletra == 2:
				contraseña += random.choice(ABC)
		print(contraseña)

def generar_contraseña_simbolos(longitud):
		contraseña = ""
		for i in range (0, longitud):
			numoletra = random.randint(0, 3)
			if numoletra == 0:
				contraseña += random.choice(abc)
			elif numoletra == 1:
				contraseña += str(random.randint(0, 9))
			elif numoletra == 2:
				contraseña += random.choice(ABC)
			elif numoletra == 3:
				contraseña += random.choice(simbolos)
		print(contraseña)

def continuar():
	while True:
		continuar = input("1. Crear nueva\n2. Salir\n>")
		if continuar == "1":
			inicio()
		elif continuar == "2":
			break
		else:
			print("escoge una opción válida porfavor")
			continue
def inicio():
	while True:
		longitud = int(input("longitud de la contraseña: "))
		simb = input("¿quieres que la contraseña contenga símbolos?\n1.si\n2.no\n>")
		if simb == "1":
			generar_contraseña_simbolos(longitud)
			continuar()
			break
		elif simb == "2":
			generar_contraseña(longitud)
			continuar()
			break
		else:
			print("introduce una respuesta válida")
			continue
inicio()
	#if type(longitud) == int:
	#	generar_contraseña(longitud)
	#	break
	#else:
	#	print("introduce una longitud válida")
	#	continue

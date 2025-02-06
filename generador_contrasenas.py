import random   # Importamos la libreria random para que escoga caracteres aleatorios 
import string   # Importamos string para acceder a letras, numeros y simbolos ya agrupados 

# Definimos los caracteres que puede tener la contraseña 
caracteres = string.ascii_letters + string.digits + string.punctuation

# Cuanta longitud queremos se desea la contraseña 
longitud = int(input("Ingresa la longitud de la contraseña: ")) 

# Generamos la contraseña aleatoria 
contraseña = ''.join(random.choice(caracteres)for _ in range(longitud))

# Se muestra la contraseña generada 
print(f"La contraseña generada es: {contraseña}")
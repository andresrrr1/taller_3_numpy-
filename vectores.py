import numpy as np

a=np.array([[5, 9], [7, 8]])

valores= np.linalg.eig(a)[0]  
vectores = np.linalg.eig(a)[1] 

print("Valores propios")
print(valores) #representan la escala de la transformación que la matriz realiza en ciertas direcciones
print("Vectores propios")
print(vectores) # solo escala el vector sin cambiar su dirección


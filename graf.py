import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 8, 10]

plt.plot(x, y, marker='o', linestyle='-')  # marker='o' para usar círculos, linestyle='-' para usar uma

plt.title('Gráfico de Coordenadas x, y')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)  # Adiciona uma grade ao gráfico
plt.show()

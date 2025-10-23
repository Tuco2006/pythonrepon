import matplotlib.pyplot as plt

def expo(a, n):
    if n == 0:
        return 1
    return a * expo(a, n - 1)

def fat(n):
    if n == 0 or n == 1:
        return 1
    return n * fat(n - 1)

def soma_exp(x, n):
    if n == 0:
        return 1
    return (expo(x, n) / fat(n)) + soma_exp(x, n - 1)

x = 10
max = 10


n_values = list(range(max + 1))
e_values = [soma_exp(x, n) for n in n_values]


plt.plot(n_values, e_values, marker='o', linestyle='-', color='b')
plt.title(f'Aproximação de e^{x} pela série de Taylor')
plt.xlabel('Número de termos (n)')
plt.ylabel('Soma parcial')
plt.grid(True)
plt.show()

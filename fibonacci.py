valo = int(input('Digite o valor que deseja saber de fibonacci:'))

def fibo(l):
    if l <= 1:
        return l
    else:
        return fibo(l-1) + fibo(l-2)

l = [0, 1]

print(f"o termo {valo} da sequencia é {fibo(valo)}")
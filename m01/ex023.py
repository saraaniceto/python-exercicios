num = float(input('Informe um número: '))
print(f'Analisando o número {num}')
print(f'Unidade: {int((((num % 1000) % 100)) % 10)}')
print(f'Dezena: {int(((num % 1000) % 100) / 10)}')
print(f'Centena: {int((num % 1000) / 100)}')
print(f'Milhar: {int(num / 1000)}')
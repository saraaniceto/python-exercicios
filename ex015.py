dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
diaria = float(input('Qual o preço da diária? R$'))
valor_km = float(input('Qual o preço por km? R$'))
print(f'Total a pagar: R${(dias*diaria + km*valor_km):.2f}')
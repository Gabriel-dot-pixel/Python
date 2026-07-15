'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
– Abaixo de 18.5: Abaixo do Peso
– Entre 18.5 e 25: Peso ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade mórbida
'''
print('====== DESAFIO 043 ======')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'O seu imc é {imc:.1f}')
    print('Você está abaixo do peso')
elif imc < 25:
    print(f'O seu imc é {imc:.1f}')
    print('Você está no seu peso ideal')
elif imc < 30:
    print(f'O seu imc é {imc:.1f}')
    print('Você está em sobrepeso')
elif imc < 40:
    print(f'O seu imc é {imc:.1f}')
    print('Você está em obesidade')
else:
    print(f'O seu imc é {imc:.1f}')
    print('Você esta em obesidade morbida')

n1 = float(input('Digite a sua nota 1: '))
n2 = float(input('Digite a sua nota 2: '))
m = (n1+n2) / 2
print(f'A sua média final é {m:.1f}')
if m >= 6.0:
    print('Parabéns! Você passou de ano!')
else:
    print('Que pena! Você reprovou, mais sorte na próxima vez!')

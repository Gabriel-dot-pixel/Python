teste = list()
teste.append('Gabriel')
teste.append(20)
pessoas = list()
pessoas.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
pessoas.append(teste[:])
print(pessoas)
pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas[2][1])
for p in pessoas:
    print(p)
for p in pessoas:
    print(p[0])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
pessoas = list()
dado = list()
for i in range(0, 3):
    dado.append(str(input('Nome: ').strip()))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)
for p in pessoas:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')

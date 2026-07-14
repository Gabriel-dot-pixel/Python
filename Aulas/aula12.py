nome = str(input('Qual é o seu nome? '))
if nome == 'Gabriel':
    print('Que nome legal!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Um belo nome para uma bela mulher')
else:
    print('Que coincidência, o meu nome támbem é {nome}}!')
print(f'Prazer em te conhecer {nome}!')

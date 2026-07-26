pessoas = {'nome': 'Gabriel', 'sexo': 'M', 'idade': 20}
print('Imprimindo um dicionario inteiro')
print(pessoas)
print('Imprimindo um dado especifico do dicionario')
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print('Imprimindo as "chaves" do dicionario')
print(pessoas.keys())
print('Imprimindo os "itens" de cada dicionario')
print(pessoas.items())
print('Laços usando dicionarios')
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')
#print('Apagando um dos itens do dicionario')
#del pessoas['sexo']
#for k, v in pessoas.items():
#    print(f'{k} = {v}')
print('ALterando um dos valores do dicionario')
pessoas['nome'] = 'Marcos'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('Adicionando um ite e um valor no dicionario')
pessoas['peso'] = 78.8
for k, v in pessoas.items():
    print(f'{k} = {v}') 
# Criando novos dicionários
brasil = list()
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
estado = dict()
brasil = list()
for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} pertence a {v}')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

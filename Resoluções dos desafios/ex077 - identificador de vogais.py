# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
print(f'{" DESAFIO 077 ":=^25}')
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    vogais = ()
    for letra in palavra:
        if letra in 'aeiou':
            vogais += (letra,)
    print(f'A palavra {palavra} possui as vogais {vogais}')

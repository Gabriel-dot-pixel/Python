frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:12])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
frase2 = '   Curso em Vídeo Python   '
print(len(frase2))
print(len(frase2.strip()))
print(frase.replace('Python', 'Android'))
# Se eu quiser imprimir um texto muito grande, basta utilizar três aspas simples ou duplas no inicio e no final do parenteses
print("""Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam quisquam aliquam odio quibusdam, totam, autem quidem ad consectetur accusamus animi iusto cumque ab qui suscipit ipsam, sunt repellat dicta nihil.""")
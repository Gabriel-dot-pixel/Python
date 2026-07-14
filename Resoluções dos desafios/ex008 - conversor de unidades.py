# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
print('====== DESAFIO 008 ======')
m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{:.2f}m são {:.2}km, {:.2f}hm, {:.2f}dam'.format(m, km, hm, dam), end=', ')
print('{:.2f}dm, {:.2f}cm e {:.2f}mm'.format(dm, cm, mm))

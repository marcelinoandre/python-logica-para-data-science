#Tabuada

num_tabuada = int(input('Informe um numero de 0 a 10: '))

if(num_tabuada < 0 or num_tabuada > 10):
   print('Número inválido')
   exit

for n in range(0, 11):
  if(n == 0):
    print(f'A tabuada do {num_tabuada} é :')

  print(f'{num_tabuada} X {n} = {num_tabuada * n}')
        











N1 = int(input('Energias iniciais na rodada: '))
N2 = int(input('Número de cartas iniciais da rodada: '))

N3 = int(input('Quantas energias o adversário ganhou nessa rodada: '))
N4 = int(input('Quantas energias o adversário gastou essa rodada: '))
N5 = int(input('Número de energias ganhas por passar a rodada: '))

N6 = int(input('Número de cartas que seu adversário usou na rodada: '))
N7 = int(input('Número de cartas que seu adversário ganhou na rodada: '))
N8 = int(input('Número de cartas ganhas por rodada: '))


R1 = print('O número atual de energia do seu oponente é: ') 
print(N1+N3-N4+N5, 'de energia')

R2 = print('O número atual de cartas do seu oponente são: ')
print(N2-N6+N7+N8, 'cartas')

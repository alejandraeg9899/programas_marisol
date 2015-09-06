# #-*- coding: iso-8859-1 -*-
# L5A_E5
# Listas de Rata1 y Rata2 
# Esquivel Guillén Alejandra Gpe.
# 3/Septiembre/2015

rat_1 = input('Peso Rata 1:\n')
rat_2 = input('Peso Rata 2:\n')
if len(rat_1) == len(rat_2):
	for valor1 in rat_1:
		print str(valor1) + ' rata 1'
	for valor2 in rat_2:
		print str(valor2) + ' rata 2'
	maximo = (valor1, valor2)
	print maximo
			#if valor1 == valor2:
			#	print 'Ambas ratas pesan lo mismo'
			#else: 
			#	maximo = max(i, j)
			#	print str(maximo) + 'más pesada' 
	#dia = dia + [i]
	#print dia 
else:
	print 'ERROR!, el tamaño de tus listas no es el mismo' 

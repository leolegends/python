def loop():
	limite = input("entre com o limite: ")
	limite = limite + 1
	lista = range(0,limite)
	for n in lista[1:limite]:
		print "numero:", n
		if n == 100:
			break


loop()

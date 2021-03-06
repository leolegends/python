import os
import time
print("\n")
print("************************** LARAVEL ***************************************")
print("************** NAO EXECUTE ESSE SCRIPT DENTRO DO SEU PROJETO *************")
print("\n")
print("Preparador de Estrutura Layout Laravel!")
print("Bootstrap 4, Material Design + Bootrap4, Semantic UI")
print("Feito para Laravel 5!")
print("\n")
print("**************************************************************************")
print("\n")
time.sleep(2)
print("Entre com o diretorio da sua aplicacao: \n ex: www/html/laravel")

diretorio = input("\nDigite o diretorio /var/: ")

'''
documentacao:

http://daemonite.github.io/material/docs/4.1/getting-started/introduction/

	Verifica se existe o diretorio:
'''

diretorio_saida = os.system("cd /var/" + diretorio)

if(diretorio_saida == 512):
    raise Exception('Diretorio nao encontrado, acho que voce digitou algo errado')
else:
	print("************************** LARAVEL ***************************************")
	print("*********************** SELECIONE UMA OPCAO  *****************************")
	print("\n")
	print("(1) - INSTALAR")
	print("(2) - DESINSTALAR")
	print("\n")
	print("**************************************************************************")
	print("\n")
	opcao = input("Entre com uma das opcoes: ")
	if(opcao == '1'):
		'''
			Clona repositorio git
		'''
		git_clone = os.system('git clone https://github.com/leolegends/laravelstrap.git')

		if(git_clone == 32768):
			os.system("Vamos atualizar o repo que voce ja tem baixado...")	
			os.system("rm laravelstrap -r")
			os.system("git clone https://github.com/leolegends/laravelstrap.git")

		if(git_clone == 32512):
			print("Ops, parece que voce ainda nao instalou o git, vamos tentar instalar pra voce.")
			os.system("apt-get install git")
			os.system("git clone https://github.com/leolegends/laravelstrap.git")

		print("\nAgora vou copiar os arquivos principais para seu diretorio /var/" + diretorio + " aguarde ...")
		comando = os.system("mkdir /var/"+ diretorio + "/public/material_css")
		os.system("mkdir /var/"+ diretorio + "/public/material_js")
		
		if(comando == 256):
			print("Vi aqui que voce ja tem as pastas dos assets, vou dar uma limpada ... ")
			os.system("rm /var/" + diretorio + "/public/material_js -R")
			os.system("rm /var/" + diretorio + "/public/material_css -R")
			
		print("\n")
		print("****************************** TEMPLATE *********************************")
		print("************************ ESCOLHA SEU TEMPLATE ****************************")
		print("\n")
		print("(1) - Bootstrap 4")
		print("(2) - Material Design")
		print("(3) - Semantic UI")
		print("\n")
		print("**************************************************************************")
		print("\n")
		opcao = input("entre com a opcao do template: ")
		if (opcao == '1'):
			print("\nCopiando CSS do Bootstrap 4\n")
			os.system("cp laravelstrap/css/* /var/" + diretorio + "/public/material_css/")
			print("Copiando JS")
			os.system("cp laravelstrap/js/* /var/" + diretorio + "/public/material_js/")
			print("\nFeito... Todos arquivos copiados, so falta os layouts ...")
			os.system("mkdir /var/"+ diretorio + "/resources/views/layouts")
			print("Copiando JS")
			os.system("cp laravelstrap/layouts_boostrap4/* /var/" + diretorio + "/resources/views/layouts/")
			print("Finalizado!")
		elif(opcao == '2'):
			print("\nCopiando CSS do Material Design\n")
			os.system("cp laravelstrap/css/* /var/" + diretorio + "/public/material_css/")
			print("Copiando JS")
			os.system("cp laravelstrap/js/* /var/" + diretorio + "/public/material_js/")
			print("\nFeito... Todos arquivos copiados, so falta os layouts ...")
			os.system("mkdir /var/"+ diretorio + "/resources/views/layouts")
			print("Copiando JS")
			os.system("cp laravelstrap/layouts_material/* /var/" + diretorio + "/resources/views/layouts/")
			print("Finalizado!")
		elif(opcao == '3'):
			print("\nCopiando CSS do Semantic UI\n")
			os.system("cp laravelstrap/css/*  /var/" + diretorio + "/public/material_css/")
			os.system("cp laravelstrap/css/UI -R /var/" + diretorio + "/public/material_css/")
			print("Copiando JS")
			os.system("cp laravelstrap/js/* /var/" + diretorio + "/public/material_js/")
			print("\nFeito... Todos arquivos copiados, so falta os layouts ...")
			os.system("mkdir /var/"+ diretorio + "/resources/views/layouts")
			print("Copiando JS")
			os.system("cp laravelstrap/layouts_semantic/* /var/" + diretorio + "/resources/views/layouts/")
			print("Finalizado!")
		else:
			raise Exception('Opcao Invalida')			
	elif(opcao == '2'):
		os.system("rm /var/" + diretorio + "/public/material_js -R")
		os.system("rm /var/" + diretorio + "/public/material_css -R")
		os.system("rm /var/" + diretorio + "/resources/views/layouts -R")
		print("Desinstalado.")
	else:
		raise Exception('Opcao Invalida')
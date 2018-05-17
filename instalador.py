import os
import time
print("\n")
print("************************** LARAVEL ***************************************")
print("************** NAO EXECUTE ESSE SCRIPT DENTRO DO SEU PROJETO *************")
print("\n")
print("Preparador de Estrutura Bootstrap Materialize, automatico!")
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
	print("\nLegal, achamos o diretorio, agora vou clonar o repositorio.\n")

'''
	Clona repositorio git
'''
git_clone = os.system('git clone https://github.com/leolegends/laravelstrap.git')

if(git_clone == 32512):
	print("Ops, parece que voce ainda nao instalou o git, vamos tentar instalar pra voce.")
os.system("apt-get install git")
os.system("git clone https://github.com/leolegends/laravelstrap.git")

print("\nAgora vou copiar os arquivos principais para seu diretorio /var/" + diretorio + " aguarde ...")
os.system("mkdir /var/"+ diretorio + "/public/material_css")
os.system("mkdir /var/"+ diretorio + "/public/material_js")
print("\nCopiando CSS\n")
os.system("cp laravelstrap/css/* /var/" + diretorio + "/public/material_css/")
time.sleep(2)
print("Copiando JS")
time.sleep(2)
os.system("cp laravelstrap/js/* /var/" + diretorio + "/public/material_js/")
print("\nFeito... Todos arquivos copiados, so falta os layouts ...")
os.system("mkdir /var/"+ diretorio + "/resources/views/layouts")
print("Copiando JS")
time.sleep(2)
os.system("cp laravelstrap/layouts/* /var/" + diretorio + "/resources/views/layouts/")
time.sleep(2)
print("Finalizado!")

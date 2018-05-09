
import os
import time 

print("********* GERADOR DE VIRTUAL HOSTS ************ \n")

print("Vamos pedir algumas informações ok? \n certifique-se de digitar todas corretamente.\n")
print("fique tranquilo, a parte dificil e chata esse script vai fazer rs.\n")

url = input("Entre com a URL que Deseja ter (sem www): \n")

diretorio_1 = input("Complete o diretorio o nome do projeto a usar (não inclua o public): /var/www/ \n")

diretorio = "/var/www/" + diretorio_1 + "/public"

link = url + ".conf"

file = open(link,"w") 
 
file.write("<VirtualHost *:80>\n") 
file.write("\tServerAdmin desenvolvimento@"+diretorio_1+".com.br\n") 
file.write("\tServerName "+ url +"\n") 
file.write("\tServerAlias www."+ url +"\n") 
file.write("\tDocumentRoot "+diretorio+"\n") 
file.write("\tErrorLog ${APACHE_LOG_DIR}/error.log\n") 
file.write("\tCustomLog ${APACHE_LOG_DIR}/access.log combined\n") 
file.write("</VirtualHost>\n") 

file.close() 

print("Legal, montamos ... agora vamos mover o arquivo e registra-lo ! \n")
os.system("mv " + link + " /etc/apache2/sites-available/")
os.system("cd /etc/apache2/sites-available")
os.system("a2ensite " + link)
os.system("cd /var/www")
os.system("service apache2 restart")
time.sleep(3)
print("feito, muito obrigado! ;)")


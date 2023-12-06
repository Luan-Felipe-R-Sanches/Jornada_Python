# Modo	Descrição	        #Comentário
# 'r'	Leitura	            Abre o arquivo somente para leitura. Gera um erro se o arquivo não existir.
# 'w'	Escrita             Abre o arquivo para escrita. Cria um novo arquivo se não existir ou sobrescreve o arquivo existente.
# 'a'	Adição	            Abre o arquivo para adicionar conteúdo. Cria um novo arquivo se não existir ou adiciona ao final do arquivo existente.
# 'r+'	Leitura e Escrita	Abre o arquivo para leitura e escrita. Gera um erro se o arquivo não existir.
# 'w+'	Escrita e Leitura	Abre o arquivo para escrita e leitura. Cria um novo arquivo se não existir ou sobrescreve o arquivo existente.
# 'a+'	Adição e Leitura	Abre o arquivo para adicionar conteúdo e leitura. Cria um novo arquivo se não existir ou adiciona ao final do arquivo existente.

texto = "Jornada Python - Manipulação de Arquivos"

arquivo = open("\\home\\suporte\\PycharmProjects\\Jornada_Python12-manipulando-arquivos\\dados\\dados.txt", 'w')
arquivo.write(texto)
arquivo.close()
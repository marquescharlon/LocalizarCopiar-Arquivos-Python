import parameters as p
import shutil
import search_files

# Função para copiar o(s) arquivo(s) específicos para a pasta de destino
def copy(path_origin, identify_file, path_destination):

    list = search_files.search(path_origin)

    for file in list:
            if identify_file in file:
                try:
                    shutil.copy(f"{path_origin}/{file}", f"{path_destination}/{file}")
                    print('Arquivo ' + file + ' copiado com sucesso para (' + path_destination + ')!')
                except:
                    pass
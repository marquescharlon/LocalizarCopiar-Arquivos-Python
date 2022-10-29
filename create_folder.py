import os
import shutil
import search_files
import parameters

def folder(path:str='', delete=False):
    
    try:
        if delete != False:

            
            if os.path.exists(path):

                list = search_files.search(path)

                print('[!] Excluindo diretório de destino e arquivos.')
                for file in list:
                    if parameters.identify_file in file:
                        os.remove(rf"{path}/{file}")
                        print(f'  → Arquivo {file}')
                        
                print('[✓] Diretório de destino e arquivos excluídos com sucesso!')  
            
        os.makedirs(path)
        print(f'[✓] Diretório "{path}" criado!')
    except FileExistsError:
        print(f'[x] Diretório "{path}" já existe!')
    

if __name__ == '__main__':
    
    path = os.path.expanduser(r"~\Documents/teste") 
    folder(path)
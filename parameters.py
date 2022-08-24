import os.path

# Local onde os arquivos estão armazenados
path_origin = os.path.expanduser(r"~\Downloads")

# Qual informação tem no nome do arquivo que será possível diferenciá-lo dos outros?
identify_file = ".TXT"

# Para qual pasta deseja copiar os arquivos?
# Se quiser copiar para uma outra pasta dentro de Documents só alterar para: os.path.expanduser(r"~\Documents/NOVA-PASTA")
path_destination = os.path.expanduser(r"~\Documents") 
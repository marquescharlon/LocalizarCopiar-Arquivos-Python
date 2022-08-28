# Copiar arquivos usando Python
Localizar e copiar arquivos para a pasta de destino.

## Parâmetros

1. Local onde os arquivos estão armazenados ```path_origin = os.path.expanduser(r"~\Downloads")```

2. Qual informação tem no nome do arquivo que será possível diferenciá-lo dos demais? ```identify_file = ".TXT"```
> Não necessariamente precisa ser a extensão do arquivo. No meu caso, eu precisei pesquisar por uma informação que tinha no meio do nome.
Só substituir o ".TXT". 

3. Para qual pasta deseja copiar os arquivos? Se quiser copiar para uma outra pasta dentro de Documents só alterar para: ```os.path.expanduser(r"~\Documents/NOVA-PASTA")```

## Bibliotecas utilizadas
```os.path```
```shutil```

## Etapas implementadas
- [x] Identificar a pasta de origem
- [x] Identificar a pasta de destino 
- [x] Como identificar o(s) arquivo(s)
- [x] Criar função para obter a lista de arquivo(s)
- [x] Criar função para copiar o(s) arquivo(s)
- [x] Imprimir no console os arquivos que foram copiados com sucesso

## Backlog
- [ ] Mover arquivo(s)
- [ ] Manipular arquivo(s)

# Conclusão

Me deparei em uma situação em que precisava localizar alguns arquivos no meio de uma pasta com vários. Como a nomenclatura era confusa, poderia correr o risco de deixar de copiar algum desses arquivos importantes. Por se tratar de arquivos de retornos financeiros que impactaria na duplicidade de arrecadações caso fosse importado algum arquivo errado, foi mais confiável desenvolver esse script para localizar e separar esses arquivos, realizando uma cópia deles em outra pasta, a de destino, na qual, eu pude validar conforme minha necessidade.

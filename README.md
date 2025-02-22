# SFTP Connection

Módulo para auxiliar as funções que exige conexão SFTP, podendo usar o mock retornar as funções mokadas

### Configurações
* Adicionar no arquivo requirements.txt a linha
  * `sftp_connection @ git+https://github.com/frcasas/sftp_connection@main`
* Adicionar no arquivo .env a linha
  * `USE_MOCK=` 0 para inativo, 1 para ativo

### Como usar
Instanciar a classe SFTPFunctions
Fazer a chamadas dos métodos

Métodos suportados:
* connect() - Abrir a conexão com o SFTP
* put(remote_path, local_path) - Enviar o arquivo para o SFTP
* get(remote_path, local_path) - Buscar o arquivo do SFTP
* close() - Fechar a conexão com o SFTP

### Exemplo
```
from sftp_connection.sftp_functions import SFTPFunctions

if __name__ == '__main__':
    sf = SFTPFunctions()
    sf.connect()
    sf.put("meuarquivo.txt", "/remoto/meuarquivo.txt")
    sf.get("/remoto/meuarquivo.txt", "baixado.txt")
    sf.close()

```
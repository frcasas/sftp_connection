from sftp_connection.sftp_functions import SFTPFunctions


def call_sftp_functions(sf: SFTPFunctions):
    sf.connect()
    sf.put("meuarquivo.txt", "/remoto/meuarquivo.txt")
    sf.get("/remoto/meuarquivo.txt", "baixado.txt")
    sf.close()


if __name__ == '__main__':
    sftp = SFTPFunctions()
    call_sftp_functions(sftp)

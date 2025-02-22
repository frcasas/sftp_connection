from sftp_connection.sftp_functions import SFTPFunctions


def get_files_sftp(sf: SFTPFunctions):
    sf.connect()
    sf.put("meuarquivo.txt", "/remoto/meuarquivo.txt")
    sf.get("/remoto/meuarquivo.txt", "baixado.txt")
    sf.close()


if __name__ == '__main__':
    sftp = SFTPFunctions()
    get_files_sftp(sftp)

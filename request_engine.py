import sqlite3 as sql

class DbFunctions:
    """
    Handles twitter database functions
    """

    def __init__(self, name):
        """
        :param name: name from the DB that will store the data
        """
        self.name = name
        self.address = "./"

    def set_tables(self):
        """
        Create all the necessary tables to store twitter streaming data and analysis
        """
        with sql.connect('./{}.db'.format(self.name)) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS contatos(
                            id_contato INTEGER PRIMARY KEY,
                            data DATE,
                            hora TIME,
                            endereco TEXT,
                            nome TEXT,
                            email TEXT,
                            num_telefone TEXT,
                            canal TEXT)
                        """)


    def cria_contato_db(self, infos):
        """
        Handle with insertion into tweet table
        """
        query = "insert into contatos(data, hora, endereco, nome, email, num_telefone, canal) values(?, ?, ?, ?, ?, ?, ?);"
        with sql.connect('./{}.db'.format(self.name)) as conn:
            c = conn.cursor()
            c.execute(query, infos)
            id_contato = c.lastrowid

        return id_contato

    def obtem_contato_db(self, id_contato):
        """
        Handle with insertion into tweet table
        """
        query = "select * from  contatos where id_contato = {};".format(id_contato)
        with sql.connect('./{}.db'.format(self.name)) as conn:
            c = conn.cursor()
            proc_data = c.execute(query)
            data = proc_data.fetchall()

        return data

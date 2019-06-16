#!/usr/bin/python
# Classe da camada de modelo
# Queries.

__author__="Miromar"
__date__ ="$15/06/2019$"


# importar o módulo de conexão
from conexao import Connect

class Sessao:

    #método construtor
    def __init__(self):
        print

    #query para teste
    def query(self):
        #instância da classe de conexão
        conn = Connect()
        #usa o atributo de cursor da classe 
        #de conexão para fazer a query
        queryEmails = conn.cur()
        queryEmails.execute("SELECT * FROM email")
        return queryEmails.fetchall()

    #método destrutor
    def __del__(self):
        del self
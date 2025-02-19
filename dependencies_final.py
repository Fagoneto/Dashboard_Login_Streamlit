import psycopg2
from dotenv import load_dotenv
import os
from contextlib import contextmanager
import streamlit as st

load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USERSERVER = os.getenv("USERSERVER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
###
DATABASE_URL = st.secrets["database"]["DATABASE_URL"]

try:
    connection = psycopg2.connect(DATABASE_URL)
    print("✅ Conexão bem-sucedida com o Neon!")
except Exception as e:
    print("❌ Erro de conexão:", e)
##
# o "cursor" é um objeto que permite que você execute comandos SQL no banco de dados e recupere os resultados.
#  Ele age como um ponteiro ou um marcador de posição dentro de uma transação ativa no banco de dados. 
# O cursor permite que você envie consultas SQL para o banco de dados, recuperar os resultados dessas consultas e, em seguida, 
# realizar operações como inserção, atualização e exclusão de dados.
@contextmanager
def instance_cursor():
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print('Conexão com PostgreSQL encerrada')

def consulta(user):
    with instance_cursor() as cursor:
        query= '''
                SELECT nome, usuario, email, fone, senha 
                FROM REGISTROS
                WHERE usuario = %s   
                '''
        cursor.execute(query, (user, ))
        request = cursor.fetchall()
        return request

def consulta_geral():
    with instance_cursor() as cursor:
        query= '''
                SELECT * 
                FROM REGISTROS   
                '''
        cursor.execute(query, )
        request = cursor.fetchall()
        return request

def add_registro(nome, user, email, fone, senha):
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()

    query= f'''
        INSERT INTO REGISTROS VALUES
        {nome, user, email, fone, senha}
        ''' 
    cursor.execute(query)
    connection.commit()
    if connection:
        cursor.close()
        connection.close()
        print('Conexão com PostgreSQL encerrada')

def cria_tabela():
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()
    print('AAAAAAA')
    print(connection)
    query= f'''
        CREATE TABLE REGISTROS (
            nome varchar(255),
            usuario varchar(255),
            email varchar(255),
            fone varchar(255),
            senha varchar(255)
        )
        ''' 
    cursor.execute(query)
    connection.commit()
    print('Tabela criada')
    if connection:
        cursor.close()
        connection.close()
        print('Conexão com PostgreSQL encerrada')

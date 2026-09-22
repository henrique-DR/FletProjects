import os   
import sqlite3
from model import Book

bookapp_sql_path = os.path.join(
    # nome do diretório em que o arquivo database.pai está.
    os.path.dirname(os.path.abspath(__file__)),
    'sql',
    'bookapp.sql'
)

insert_book_query = '''
    insert into pintao (titulo, autor, desc, preco)
    values (?, ?, ?, ?)
'''

class Database:
    def __init__(self, db_path: str):
        '''self.db_path: caminho do arquivo de banco de dados'''
        self.db_path = db_path
        self.__create_tables()

    def __connect(self) -> sqlite3.Connection:
        '''Cria uma conexão com o banco de dados SQLite'''
        return sqlite3.connect(self.db_path)
    def __create_tables(self):
        '''Cria a tabela de livros se não existir'''
        conn = self.__connect()
        #...
        with self.__connect() as conn:
            with open(bookapp_sql_path, 'r') as f:
                sql_script = f.read()
            conn.executescript(sql_script)
    def insert(self, book:Book):
        '''Insere um livro no banco de dados
        recebe um objeto Book como parâmetro
        conecta ao banco de dados, executa a query de inserção e fecha a conexão
        '''


        with self.__connect() as conn:
            with conn:
                conn.execute(insert_book_query, (book.titulo, book.autor, book.desc, book.preco))
    def fetch_all(self) -> list[Book]:
        '''Recupera todos os livros do banco de dados'''
        pass

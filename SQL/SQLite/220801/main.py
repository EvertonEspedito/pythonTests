import _sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = 'minha_db.sqlite3'
DB_PATH = BASE_DIR / DB_NAME
TABLE_NAME = 'clientes'

coneccao = _sqlite3.connect(DB_PATH)# Conexão com o banco de dados
cursor = coneccao.cursor() # Criação do cursor

#SQl para criar a tabela
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        peso REAL NOT NULL
    );
''')

cursor.close() # Fechamento do cursor
coneccao.close() # Fechamento da conexão com o banco de dados
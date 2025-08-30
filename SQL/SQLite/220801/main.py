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
        name TEXT NOT NULL,
        weight REAL NOT NULL
    );
''')
coneccao.commit() # Confirmação da criação da tabela

# SQL para inserir dados na tabela
cursor.execute(f'''
    INSERT INTO {TABLE_NAME} (name, weight) VALUES
    ('Maria', 60.5),
    ('João', 75.0),
    ('Ana', 55.3),
    ('Everton', 67.2 );
''')
coneccao.commit() # Confirmação da inserção dos dados

# SQL deleTe para remover um registro
cursor.execute(f'''
    DELETE FROM {TABLE_NAME} WHERE name = 'João';
''')

coneccao.commit() # Confirmação da deleção do registro

#SQL para atualizar um registro
cursor.execute(f'''
    UPDATE {TABLE_NAME} SET weight = 58.0 WHERE name = 'Ana';
''')
coneccao.commit() # Confirmação da atualização do registro

# SQL para selecionar e exibir os registros restantes
cursor.execute(f'''
    SELECT * FROM {TABLE_NAME};
''')
registros = cursor.fetchall() # Recuperação de todos os registros
for registro in registros:
    print(registro) # Exibição de cada registro na tela



cursor.close() # Fechamento do cursor
coneccao.close() # Fechamento da conexão com o banco de dados
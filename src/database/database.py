from src.settings.connection import db_connection_handler
from src.scripts.generate_data import GenerateData
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import text

db_connection_handler.connect_to_db()

class Database:
    def create_table(self, table_name):
        try:
            with db_connection_handler as db:
                sql = (f"""
                CREATE TABLE IF NOT EXISTS {table_name}(
                    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "cpf" TEXT NOT NULL UNIQUE,
                    "nome_completo" TEXT NOT NULL,
                    "emprego_atual" TEXT NOT NULL,
                    "data_nascimento" DATE NOT NULL,
                    "situacao_civil" TEXT NOT NULL,
                    "endereco" TEXT NOT NULL,
                    "cliente_especial" INTEGER NOT NULL CHECK (cliente_especial IN (0, 1))
                    );
                """)
                db.session.execute(sql)
            return print(f"Tabela {table_name} criada com sucesso")    
            
        except Exception as exception:
            return print(f"Erro ao criar a tabela: {exception}") 

    def insert_data(self, num, table_name):
        print('inserindo dados...')
        generate = GenerateData()
      
        for i in range(num):
            novo_cliente = generate.gerar_dados()      
            while True:          
                with db_connection_handler as db:
                    try:
                        sql = text((f'''INSERT INTO {table_name} (cpf, nome_completo, emprego_atual, data_nascimento, situacao_civil, endereco, cliente_especial) 
                                    VALUES (:cpf, :nome_completo, :emprego_atual, :data_nascimento, :situacao_civil, :endereco, :cliente_especial)'''))
                        
                        db.session.execute(sql, {
                            'cpf': novo_cliente[0],
                            'nome_completo': novo_cliente[1],
                            'emprego_atual': novo_cliente[2],
                            'data_nascimento': novo_cliente[3],
                            'situacao_civil': novo_cliente[4],
                            'endereco': novo_cliente[5],
                            'cliente_especial': novo_cliente[6]
                        })
                        db.session.commit()
                        break
                    except IntegrityError:
                        novo_cliente = generate.gerar_dados()
                    except Exception as exception:
                        if db.session:
                            db.session.rollback()
                            raise exception
                
        return print('Dados inseridos com sucesso')
    
    def get_data(self):
        try:
            with db_connection_handler as db:
                sql = text("SELECT * FROM clientes")
                result = db.session.execute(sql)
                return result.fetchall()
        except Exception as exception:
            raise exception
from src.scripts.generate_data import GenerateData
from src.database.database import Database

#gen = GenerateData()

#print(gen.gerar_dados())

db = Database()
db.create_table('clientes')
db.insert_data(5000, 'clientes')

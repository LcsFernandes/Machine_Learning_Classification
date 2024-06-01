from src.scripts.generate_data import GenerateData
from src.Model.logistic_regression import RegressaoLogistica
from src.Model.arvore_decisao import ArvoreDecisao
from src.Model.SVM import Svm
from src.database.database import Database
from src.scripts.etl import Etl
import pandas as pd

#gen = GenerateData()

#print(gen.gerar_dados())

db = Database()
etl = Etl()
#db.create_table('clientes')
#db.insert_data(5000, 'clientes')
#data = db.get_data()
#df = pd.DataFrame(data)
#print(df.head(1))
#pd.set_option('display.max_columns', None)
#df = etl.load_data()
#print(df.head())  
#reglog = RegressaoLogistica()
#reglog.regressao_logistica()
#tree = ArvoreDecisao()
#tree.arvore_decisao()
svm = Svm()
svm.svm()

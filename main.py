from src.Model.logistic_regression import RegressaoLogistica
from src.Model.decision_tree import DecisionTree
from src.Model.SVM import Svm
from src.database.database import Database
import logging

logging.basicConfig(filename = 'app.log', level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def setup_database():
    db = Database()

    try:
        logging.info("Criando tabela 'clientes'.")
        db.create_table('clientes')
        logging.info("Inserindo dados na tabela 'clientes'.")
        db.insert_data(5000, 'clientes')
    except Exception as e:
        logging.error(f"Erro ao configurar o banco de dados: {e}")
    return db

def run_logistic_regression():
    
    try:
        reglog = RegressaoLogistica()
        logging.info("Executando regressão logística.")
        reglog.regressao_logistica()
    except Exception as e:
        logging.error(f"Erro ao executar regressão logística: {e}")

def run_decision_tree():
    
    try:
        tree = DecisionTree()
        logging.info("Executando árvore de decisão.")
        tree.decision_tree()
    except Exception as e:
        logging.error(f"Erro ao executar árvore de decisão: {e}")

def run_svm():
    
    try:
        svm = Svm()
        logging.info("Executando SVM.")
        svm.svm()
    except Exception as e:
        logging.error(f"Erro ao executar SVM: {e}")

def main():
   
    setup_database()
    run_logistic_regression()
    run_decision_tree()
    run_svm()

if __name__ == "__main__":
    main()
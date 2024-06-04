from src.Model.logistic_regression import RegressaoLogistica
from src.Model.decision_tree import DecisionTree
from src.Model.SVM import Svm
from src.database.database import Database


def setup_database():
    db = Database()

    try:
        db.create_table('clientes')
        db.insert_data(5000, 'clientes')
    except Exception as e:
        print(f"Erro ao configurar o banco de dados: {e}")
    

def run_logistic_regression():
    
    try:
        reglog = RegressaoLogistica()
        print("Executando regressão logística.")
        reglog.regressao_logistica()
        print("Regressao logistica executada com sucesso")
    except Exception as e:
        print(f"Erro ao executar regressão logística: {e}")

def run_decision_tree():
    
    try:
        tree = DecisionTree()
        print("Executando árvore de decisão.")
        tree.decision_tree()
        print("Arvore de decisão executada com sucesso")
    except Exception as e:
        print(f"Erro ao executar árvore de decisão: {e}")

def run_svm():
    
    try:
        svm = Svm()
        print("Executando SVM.")
        svm.svm()
        print("SVM executada com sucesso")
    except Exception as e:
        print(f"Erro ao executar SVM: {e}")

def main():
   
    setup_database()
    run_logistic_regression()
    run_decision_tree()
    run_svm()

if __name__ == "__main__":
    main()
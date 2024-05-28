from src.tratamento.ETL import ETL
import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_curve, auc, roc_auc_score, confusion_matrix
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns 

class RegressaoLogistica:
    
    def regressao_logistica(self):
        etl = ETL()
        df = etl.load_data()

        if df is not None:
            X = df.drop(columns = ['cliente_especial'])
            y = df['cliente_especial']

            cat_nominal = X.drop(columns = 'idade').columns
        


            cat_nominal_transformer = Pipeline(steps = [
                ('one_hot_encoder', OneHotEncoder())
            ])


            preprocessor = ColumnTransformer(transformers=[
                ('cat_nominal', cat_nominal_transformer, cat_nominal)
            ])

            pipe = make_pipeline(
                preprocessor,
                SMOTE(random_state = 42),
                StandardScaler(with_mean=False),
                PCA(svd_solver='arpack'),
                LogisticRegression()
                
            )

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)

            param_grid = {
                    'classifier__penalty': ['l1', 'l2'],
                    'classifier__C': [0.001, 0.01, 0.1, 1, 10, 100],
                    'classifier__solver': ['liblinear', 'newton-cg', 'lbfgs', 'sag', 'saga'],
                    'classifier__max_iter': [100, 500, 1000]
                    }
            
            
            grid_search = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
            grid_search.fit(X, y)

            
            print("Melhores hiperparâmetros:", grid_search.best_params_)
            print("Acurácia:", grid_search.best_score_)

            
            best_model = grid_search.best_estimator_

            modelo = best_model.fit(X_train, y_train)

            modelo_score = modelo.score(X_train, y_train)
            print(modelo_score)

            y_score = modelo.predict_proba(X_test)
            fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])

            fig = plt.figure(figsize = (6, 6))
            plt.plot([0, 1], [0, 1], 'k--')
            plt.plot(fpr, tpr, label = "Regressao Logistica")
            plt.xlabel('Falso Positivo')
            plt.ylabel('Verdadeiro Positivo')
            plt.title('Curva ROC')
            plt.legend(loc="lower right", fontsize=16)
            plt.show()
            print('area sob a curva: ', auc(fpr, tpr))
            
            
            predict = modelo.predict(X_test)
            conf_matrix = confusion_matrix(y_test, predict)

            # Plote a matriz de confusão usando seaborn
            plt.figure(figsize=(8, 6))
            sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Greens")
            plt.xlabel('Preditos')
            plt.ylabel('Verdadeiros')
            plt.title('Matriz de confusao')
            plt.show()

            classification_report = classification_report(y_test, predict)
            print("classification report ", classification_report)

            

            
        
        
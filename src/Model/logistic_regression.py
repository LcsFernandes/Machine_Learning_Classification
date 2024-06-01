from src.scripts.etl import Etl 
import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_curve, auc, confusion_matrix
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns 

class RegressaoLogistica:
    
    def regressao_logistica(self):
        etl = Etl()
        df = etl.load_data()
        df_ml = df[['emprego_atual', 'idade', 'situacao_civil', 'bairro', 'cidade', 'estado', 'cliente_especial']]
        if df is not None:

            X = df_ml.drop(columns = 'cliente_especial')
            y = df_ml['cliente_especial']

            one_hot_encoder = OneHotEncoder(handle_unknown = 'ignore')
            X_enc = one_hot_encoder.fit_transform(X.drop(columns =['idade']))

            smote_bal = SMOTE(random_state = 42)

            X_bal, y_bal = smote_bal.fit_resample(X_enc, y)


            pipeline = Pipeline(steps = [
                ('s_scale', StandardScaler(with_mean=False)),
                ('pca', PCA()),
                ('reg_log', LogisticRegression())
            ])

            X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size = 0.30, random_state = 42)

            param_grid = {
                    'reg_log__C': [0.1, 1, 10],
                    'reg_log__solver': ['liblinear', 'saga'],
                    'reg_log__max_iter': [500, 1000]
                }
            
            grid_search = GridSearchCV(pipeline, param_grid, cv=2, scoring='accuracy')
            grid_search.fit(X_train, y_train)

            
            print("Melhores hiperparâmetros:", grid_search.best_params_)
            print("Acurácia:", grid_search.best_score_)

             
            best_model = grid_search.best_estimator_

            modelo = best_model.fit(X_train, y_train)

            modelo_score = modelo.score(X_test, y_test)
            print(modelo_score)

            predict = modelo.predict(X_test)
            report = classification_report(y_test, predict)
            print("classification report", report)

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
            
            
            conf_matrix = confusion_matrix(y_test, predict)

            plt.figure(figsize=(8, 6))
            sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Greens")
            plt.xlabel('Preditos')
            plt.ylabel('Verdadeiros')
            plt.title('Matriz de confusao')
            plt.show()

 
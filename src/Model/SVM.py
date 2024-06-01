from src.scripts.etl import Etl
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns

class Svm:  
    def svm(self):
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
                ('s_scaler', StandardScaler(with_mean=False)),
                ('pca', PCA()),
                ('svm', SVC())
            ])

            X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size = 0.30, random_state = 42)
            
            param_grid = {
                'svm__C': [0.1, 1, 10, 100],
                'svm__gamma': ['scale', 'auto'],
                'svm__kernel': ['linear', 'rbf', 'poly', 'sigmoid']
            }
           
            grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
            grid_search.fit(X_bal, y_bal)

           
            print("Melhores hiperparâmetros:", grid_search.best_params_)
            print("Acurácia:", grid_search.best_score_)

           
            best_model = grid_search.best_estimator_

            modelo = best_model.fit(X_train, y_train)
            modelo_score = modelo.score(X_test, y_test)
            print(modelo_score)

            predict = modelo.predict(X_test)
            report = classification_report(y_test, predict)
            print("classification report ", report)
            

            conf_matrix = confusion_matrix(y_test, predict)
            plt.figure(figsize=(8, 6))
            sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Greens")
            plt.xlabel('Preditos')
            plt.ylabel('Verdadeiros')
            plt.title('Matriz de confusao')
            plt.show()



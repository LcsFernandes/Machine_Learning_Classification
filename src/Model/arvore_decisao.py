from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree
from src.tratamento.ETL import ETL
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import GridSearchCV, train_test_split
from mlxtend.plotting import plot_decision_regions
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.decomposition import PCA
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns

class ArvoreDecisao:  
    def arvore_decisao(self):
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
                DecisionTreeClassifier() 
            )

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)
            
            param_grid = {
                        'classifier__criterion': ['gini', 'entropy'],
                        'classifier__max_depth': [None, 10, 20, 30],
                        'classifier__min_samples_leaf': [1, 2, 4],
                        'classifier__min_samples_split': [2, 5, 10]
                        }

            
            grid_search = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
            grid_search.fit(X, y)

            
            print("Melhores hiperparâmetros:", grid_search.best_params_)
            print("Acurácia:", grid_search.best_score_)

            
            best_model = grid_search.best_estimator_

            X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size = 0.30, random_state = 42)
            modelo = best_model.fit(X_train, y_train)

            modelo_score = modelo.score(X_train, y_train)
            print(modelo_score)
            
            
            predict = modelo.predict(X_test)
            conf_matrix = confusion_matrix(y_test, predict)

            
            plt.figure(figsize=(8, 6))
            sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Greens")
            plt.xlabel('Preditos')
            plt.ylabel('Verdadeiros')
            plt.title('Matriz de confusao')
            plt.show()
            
            plt.figure(figsize = (12, 8))
            tree.plot_tree(modelo)
            plt.show()
            
            print("classification report ", classification_report(y_test, predict))
            



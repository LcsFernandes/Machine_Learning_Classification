# Machine_Learning_Classification

## Objetivo do Projeto

O objetivo deste projeto é demonstrar o processo completo de manipulação de dados e modelagem preditiva usando algoritmos de Machine Learning. A aplicação cobre desde a geração e transformação de dados, até a implementação e avaliação de diferentes modelos preditivos. Este projeto serve como um exemplo prático para aplicação de algoritmos para lidar com classificação de variaveis binárias.

### Explicação da Arquitetura:

- **data**: Contém o dataset utilizado pela aplicação.
  - `clientes.csv`: Arquivo CSV com os dados dos clientes.

- **init**: Contém o modelo da tabela do banco de dados.
  - `schema.sql`: Script SQL para criar a estrutura da tabela no banco de dados.

- **src**: Diretório principal que contém o código-fonte da aplicação.
  - **database**: Scripts relacionados ao banco de dados.
    - `database.py`: Script para criar a tabela no banco de dados e inserir os dados.
  - **Model**: Implementações de modelos de Machine Learning.
    - `decision_tree.py`: Modelo de Árvore de Decisão.
    - `logistic_regression.py`: Modelo de Regressão Logística.
    - `SVM.py`: Modelo de Máquinas de Vetores de Suporte (SVM).
  - **notebooks**: Notebooks Jupyter usados para análise de dados e testes.
    - `notebook.ipynb`: Notebook com análises e testes.
  - **scripts**: Scripts auxiliares para ETL e geração de dados sintéticos.
    - `etl.py`: Script para realizar a transformação e carga de dados (ETL).
    - `generate_data.py`: Script para gerar dados sintéticos.
  - **settings**: Configurações de conexão com o banco de dados.
    - `connection.py`: Configuração da conexão com o banco de dados.

- **main.py**: Arquivo principal para execução da aplicação.

- **requirements.txt**: Arquivo com as dependências necessárias para o projeto.

## Instruções de Uso
**Requisitos**
Certifique-se de ter as seguintes dependências instaladas:
- Python 3.x
- Bibliotecas necessárias (listadas no arquivo requirements.txt)

1. **Clone este repositorio:**
 - git clone https://github.com/LcsFernandes/Machine_Learning_Classification.git

2. **Instale as dependencias:**
 - pip install -r requirements.txt

3. **Rodando a aplicação:**
 - Execute o arquivo main.py

# Conclusão

Conclusão:
Este projeto de Machine Learning abrangeu todo o ciclo de vida de um projeto de dados, desde a manipulação inicial dos dados até a aplicação de algoritmos preditivos e a análise dos resultados.

Os modelos de Machine Learning alcançaram uma alta precisão nos conjuntos de dados testados, demonstrando a eficácia dos algoritmos escolhidos. Analisando os resultados obtidos, percebemos que a Árvore de Decisão se destacou como o modelo de melhor performance, atingindo uma acurácia de 99% na classificação binária.

É importante ressaltar que a escolha do melhor modelo depende do contexto específico do problema. Apesar da Árvore de Decisão ter apresentado o melhor resultado nesse caso, é sempre recomendado avaliar diferentes algoritmos para selecionar a abordagem mais adequada para cada cenário.

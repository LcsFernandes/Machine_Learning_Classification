# Machine_Learning_Classification

## Objetivo do Projeto
Desenvolver um sistema preditivo, utilizando algoritmos de Machine Learning, para identificar e classificar clientes com alto potencial de fidelização e valor para a empresa, denominados "clientes especiais".

### Metodologia:
- Geração de Dados: Dados aleatórios foram gerados para simular um cenário real de classificação binária.
- ETL: O processo de Extração, Transformação e Carregamento (ETL) foi realizado para preparar os dados para modelagem.
- Modelagem: Três modelos de Machine Learning foram implementados e avaliados: Regressão Logística, Árvore de Decisão e Máquinas de Vetores de Suporte (SVM).
- Avaliação dos modelos: Os modelos foram avaliados em termos de precisão, recall e F1-score.

### Espera-se contribuir para:
- Aumentar a fidelização e retenção de clientes especiais.
- Otimizar campanhas de marketing e vendas direcionadas.
- Aprimorar a tomada de decisões estratégicas relacionadas à gestão de clientes.
- Promover uma melhor compreensão do comportamento e valor dos clientes para a empresa.

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

Este projeto de Machine Learning abrangeu todo o ciclo de vida de um projeto de dados, desde a manipulação inicial dos dados até a aplicação de algoritmos preditivos e a análise dos resultados. Os modelos de Machine Learning alcançaram uma alta precisão nos conjuntos de dados testados, demonstrando a eficácia dos algoritmos escolhidos. Analisando os resultados obtidos, percebemos que a Árvore de Decisão se destacou como o modelo de melhor performance, atingindo uma acurácia de 99% na classificação binária. 
É importante ressaltar que a escolha do melhor modelo depende do contexto específico do problema. Apesar da Árvore de Decisão ter apresentado o melhor resultado nesse caso, é sempre recomendado avaliar diferentes algoritmos para selecionar a abordagem mais adequada para cada cenário.

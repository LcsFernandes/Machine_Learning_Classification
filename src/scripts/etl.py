from src.database.database import Database
import pandas as pd
import datetime

class Etl:
    def __init__(self) -> None:
        self.df = None

    def extract_data(self):
        db = Database()
           
        data = db.get_data()
        self.df = pd.DataFrame(data)
        return self.df
        
    def transform_data(self):
        if self.df is not None:
            ruas, bairros, cidades, estados, ceps = [], [], [], [], []
            for end in self.df['endereco']:
                endereco = end.split('\n')

                if len(endereco) >= 3:
                    rua_numero = endereco[0].split(',')
                    if len(rua_numero) == 2:
                        rua = rua_numero[0].strip()
                    else:
                        rua = endereco[0].strip()
                bairro = endereco[1].strip()
                cidade_cep = endereco[2].split(' ')
                cep = cidade_cep[0] 
                cidade = ' '.join(cidade_cep[1:-2])
                estado = cidade_cep[-1]
                
                ruas.append(rua)
                bairros.append(bairro)
                cidades.append(cidade)
                estados.append(estado)
                ceps.append(cep)
            
            self.df['rua'] = ruas
            self.df['bairro'] = bairros
            self.df['cidade'] = cidades
            self.df['estado'] = estados
            self.df['CEP'] = ceps

            self.df = self.df.drop(columns= 'endereco')

            self.df['data_nascimento'] = pd.to_datetime(self.df['data_nascimento'])
            hoje = datetime.date.today()
            self.df['idade'] = self.df['data_nascimento'].apply(lambda x: hoje.year - x.year - ((hoje.month, hoje.day) < (x.month, x.day)))

        return self.df
        
    def load_data(self):
        self.extract_data()
        self.transform_data()
        
        return self.df[['id', 'cpf', 'nome_completo', 'idade', 'emprego_atual', 'data_nascimento', 'situacao_civil', 'rua', 'bairro', 'cidade',
                        'estado', 'CEP', 'cliente_especial']]
        





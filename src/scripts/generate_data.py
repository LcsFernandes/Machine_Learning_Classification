from faker import Faker
import random

class GenerateData:
    def gerar_dados(self):

        fake = Faker('pt_BR')

        cpf = fake.cpf()
        nome_completo = fake.name()
        emprego_atual = fake.job()
        data_nascimento = fake.date_of_birth(minimum_age = 18, maximum_age = 65).strftime('%Y-%m-%d')
        situacao_civil = random.choice(['Solteiro(a)', 'Casado(a)', 'Divorsiado(a)'])
        endereco = fake.address()
        cliente_especial = random.choices([1, 0], weights=[0.05, 0.95])[0]

        dados = (cpf, nome_completo, emprego_atual, data_nascimento, situacao_civil, endereco, cliente_especial)
        return dados
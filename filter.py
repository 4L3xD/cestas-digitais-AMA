# -*- coding: utf-8 -*-
import pandas as pd
#from matplotlib import pyplot as plt

df = pd.read_excel('cestas_digitais.xlsx',sheet_name='Respostas ao formulario',
    usecols=['Sexo', 'Data de nascimento', 'Idade',	'Filhos', 'Primeiro filho',
    'Estado civil', 'Raca/Etnia', 'Escolaridade', 'Endereco', 'Bairro', 
    'Propriedade', 'Valor aluguel', 'Energia eletrica', 'Agua encanada',
    'Saneamento basico', 'Rua asfaltada', 'Telha', 'Piso', 'Teto',
    'Parede interna', 'Parede externa', 'Banheiros', 'Comodos (sem banheiro)',
    'Terreno murado', 'NIS', 'Bolsa Familia', 'Valor Bolsa Familia',
    'Atividade remunerada', 'Local trabalho', 'Carteira assinada', 'Auxilio Emergencial',
    'Valor Auxilio Emergencial', 'Aposentadoria', 'Valor aposentadoria',
    'Pensao alimenticia', 'Valor pensao alimenticia', 'Auxilio reclusao',
    'Valor auxilio reclusao', 'Trabalhadores residentes', 'Qtdd trabalhadores residentes',
    'Empresas contratantes', 'Renda bruta familia', 'Beneficiados da renda',
    'Saude entrevistadx', 'Doenca entrevistadx', 'Deficiencia entrevistadx',
    'Tipo deficiencia entrevistadx', 'Especificacao doenca', 'Saude familia',
    'Pessoas doentes', 'Deficientes familia', 'Tipo deficiencia familia',
    'Especificacao deficiencia', 'Tipo doenca familia', 'Criancas de 0 a 6 anos',
    'Criancas de 7 a 12 anos', 'Adolescentes de 13 a 18 anos', 'Parentesco',
    'Idade crianca', 'Escola', 'Periodo integral', 'Projetos',
    'Acesso a internet', 'Meio de acesso internet', 'Dispositivos'])

#df.to_excel('respostas_cestas.xlsx', encoding='utf-8', index=False)
#print('Dataframe exportado para excel!')

def count(column, attribute0, attribute1, message0, message1):
    attribute0_count = 0
    attribute1_count = 0
    for i in df[column]:
        print(i)
        if i == None:
            return
            print('Thats None?', i)
        elif i == attribute0.decode('utf-8'):
            attribute0_count += 1
            print('Thats a ' + str(attribute0), i)
        elif i == attribute1.decode('utf-8'):
            attribute1_count += 1
            print('Thats a ' + str(attribute1), i)
    print(message0, attribute0_count)
    print(message1, attribute1_count)
#    groups = ['Sim', 'Não']
#    valors = [attribute0_count, attribute1_count]
#    plt.bar(grupos, valores)
#    plt.show()

count('Saude familia', 'Sim', 'Não',
'Pessoas pessoas com historico de doencas na familia',
'Pessoas pessoas sem historico de doencas na familia')

count('Deficientes familia', 'Sim', 'Não',
'Pessoas pessoas com deficiencientes na familia',
'Pessoas pessoas sem deficiencientes na familia')

count('Periodo integral', 'Sim', 'Não',
'Criancas que estudam em periodo integral',
'Criancas que nao estudam em periodo integral')

childs_age = []
for child in df['Idade crianca']:
    for age in range(19):
        if child == age:
            age_count = 0
            if age in childs_age:
              print(childs_age)
            else:
              age_count = 0
              childs_age.insert(age, age)
print(childs_age[18])
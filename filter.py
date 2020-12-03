import pandas as pd
import xlrd

formulario = pd.read_excel('cestas_digitais.xlsx', sheet_name='Respostas ao formulário',
    usecols=['Sexo', 'Data de nascimento', 'Idade',	'Filhos', 'Primeiro filho',
    'Estado civil', 'Raça/Etnia', 'Escolaridade', 'Endereço', 'Bairro', 
    'Propriedade', 'Valor aluguel', 'Energia elétrica', 'Água encanada',
    'Saneamento básico', 'Rua asfaltada', 'Telha', 'Piso', 'Teto',
    'Parede interna', 'Parede externa', 'Banheiros', 'Cômodos (sem banheiro)',
    'Terreno murado', 'NIS', 'Bolsa Família', 'Valor Bolsa Família',
    'Atividade remunerada', 'Local trabalho', 'Carteira assinada', 'Auxílio Emergencial',
    'Valor Auxílio Emergencial', 'Aposentadoria', 'Valor aposentadoria',
    'Pensão alimentícia', 'Valor pensão alimentícia', 'Auxilio reclusão',
    'Valor auxilio reclusão', 'Trabalhadores residentes', 'Qtdd trabalhadores residentes',
    'Empresas contratantes', 'Renda bruta família', 'Beneficiados da renda',
    'Saúde entrevistadx', 'Doença entrevistadx', 'Deficiência entrevistadx',
    'Tipo deficiência entrevistadx', 'Especificação doença', 'Saúde família',
    'Pessoas doentes', 'Deficientes família', 'Tipo deficiência família',
    'Especificação deficiência', 'Tipo doença família', 'Crianças de 0 a 6 anos',
    'Crianças de 7 a 12 anos', 'Adolescentes de 13 a 18 anos', 'Parentesco',
    'Idade criança', 'Escola', 'Período integral', 'Projetos',
    'Acesso a internet', 'Meio de acesso internet', 'Dispositivos'])

print(formulario)




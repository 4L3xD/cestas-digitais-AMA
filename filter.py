# -*- coding: utf-8 -*-
import pandas as pd
import xlrd

formulario = pd.read_excel('cestas_digitais.xlsx',sheet_name='Respostas ao formulario',
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

print(formulario)





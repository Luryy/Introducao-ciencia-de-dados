import pandas as pd;

data = pd.read_csv('./Dados/dfp_cia_aberta_DRE_con_2010-2020.csv')

data.drop(['CD_CVM', 'GRUPO_DFP', 'VERSAO', 'MOEDA', 'ST_CONTA_FIXA', 'CD_CONTA'], inplace=True, axis=1)

ds_conta_required = ['Resultado Bruto', 'Lucro/Prejuízo Consolidado do Período', 'Despesas/Receitas Operacionais']

data = data[data.DS_CONTA.isin(ds_conta_required)]

data = data[data['ORDEM_EXERC'] == "ÚLTIMO"]

print(data.set_index(['CNPJ_CIA', 'DT_REFER']))


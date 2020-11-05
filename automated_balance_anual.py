import pandas as pd
import wget
from zipfile import ZipFile
import plotly.graph_objects as go

url_base = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'

arquivos_zip = []
for ano in range(2010,2021):
  arquivos_zip.append(f'dfp_cia_aberta_{ano}.zip')

for arq in arquivos_zip:
  wget.download(url_base+arq)

for arq in arquivos_zip:
  ZipFile(arq, 'r').extractall('CVM')

nomes = ['BPA_con', 'BPA_ind', 'BPP_con', 'BPP_ind', 'DFC_MD_con', 'DFC_MD_ind', 'DFC_MI_con', 'DFC_MI_ind', 'DMPL_con', 'DMPL_ind', 'DRE_con', 'DRE_ind', 'DVA_con', 'DVA_ind']
for nome in nomes:
  arquivo = pd.DataFrame()
  for ano in range(2010,2021):
    arquivo = pd.concat([arquivo, pd.read_csv(f'CVM/dfp_cia_aberta_{nome}_{ano}.csv', sep=';', decimal=',', encoding='ISO-8859-1')])
  arquivo.to_csv(f'DADOS/dfp_cia_aberta_{nome}_2010-2020.csv', index=False)

dre = pd.read_csv('/content/DADOS/dfp_cia_aberta_DRE_ind_2010-2020.csv')

dre = dre[dre['ORDEM_EXERC'] == "ÚLTIMO"]

empresas = dre[['DENOM_CIA','CD_CVM']].drop_duplicates().set_index('CD_CVM')

empresa = dre[dre['CD_CVM'] == 7617]

conta = empresa[empresa['CD_CONTA'] == '3.99.01.02']

conta.index = pd.to_datetime(conta['DT_REFER'])

#----------------------

import yfinance as yf

prices = yf.download('ITSA4.SA', start='2011-01-01')[['Adj Close', 'Close']]

indicadores = prices.join(conta['VL_CONTA'], how='outer')

indicadores.rename({'VL_CONTA':'LPA'}, axis=1, inplace=True)

indicadores.fillna(method='ffill', inplace=True)

indicadores.dropna(inplace=True)

indicadores['PL'] = indicadores['Close'] / indicadores['LPA']
indicadores['PL_ajustado'] = indicadores['Adj Close'] / indicadores['LPA']

fig = go.Figure()
fig.add_trace(go.Scatter(x=indicadores.index, y=indicadores['PL'], name='PL'))
fig.add_trace(go.Scatter(x=indicadores.index, y=indicadores['PL_ajustado'], name='PL_ajustado'))
fig.add_trace(go.Scatter(x=indicadores.index, y=indicadores['Close'], name='ITSA4'))
fig.add_trace(go.Scatter(x=indicadores.index, y=indicadores['Adj Close'], name='ITSA4_Ajustado'))




import pandas as pd
import wget
from zipfile import ZipFile


def getAnuallyData():

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
    arquivo.to_csv(f'dfp_cia_aberta_{nome}_2010-2020.csv', index=False)

  return
import pandas as pd
import wget
from zipfile import ZipFile

def getTrimestralData():

  url_base = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/'

  # list with all files names
  arquivos_zip = []
  for ano in range(2011,2021):
    arquivos_zip.append(f'itr_cia_aberta_{ano}.zip')

  #downloading
  for arq in arquivos_zip:
    wget.download(url_base+arq)

  #extract
  for arq in arquivos_zip:
    ZipFile(arq, 'r').extractall('CVM')

  #creating files
  nomes = ['BPA_con', 'BPA_ind', 'BPP_con', 'BPP_ind', 'DFC_MD_con', 'DFC_MD_ind', 'DFC_MI_con', 'DFC_MI_ind', 'DMPL_con', 'DMPL_ind', 'DRE_con', 'DRE_ind', 'DVA_con', 'DVA_ind']
  for nome in nomes:
    arquivo = pd.DataFrame()
    for ano in range(2011,2021):
      arquivo = pd.concat([arquivo, pd.read_csv(f'CVM/itr_cia_aberta_{nome}_{ano}.csv', sep=';', decimal=',', encoding='ISO-8859-1')])
    arquivo.to_csv(f'DADOS/itr_cia_aberta_{nome}_2011-2020', index=False)


  dre = pd.read_csv('/content/DADOS/itr_cia_aberta_DRE_con_2011-2020')
  return dre
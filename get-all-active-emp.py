import pandas as pd

def getActiveEmp():
    allEmp = pd.read_csv('./Dados/cad_cia_aberta.csv', sep=';', decimal=',', encoding='ISO-8859-1')
    empresas = pd.read_csv('./Info/empresas_listadas_cnpj_ind.csv')
    cnpjs = []
    for empresa in empresas.values:
        cnpjs.append(empresa[2])
    a = allEmp[allEmp.CNPJ_CIA.isin(cnpjs)]
    filteredEmp = a[['CNPJ_CIA', 'DENOM_COMERC', 'SIT', 'CD_CVM', 'TP_MERC']].drop_duplicates().set_index('CD_CVM')
    filteredEmp = filteredEmp[filteredEmp['SIT'] == 'ATIVO']
    filteredEmp.to_csv(f'Info/empresas_listadas_cnpj_ind_active.csv', index=True)    
    return

def filterDataSeriesWithActiveAndLastBalance():
    data = pd.read_csv('./Dados/dfp_cia_aberta_DRE_ind_2010-2020.csv')
    data = data[data['ORDEM_EXERC'] == "ÚLTIMO"]
    data.drop('ORDEM_EXERC', inplace=True, axis=1)
    filteredEmp = pd.read_csv('./Info/empresas_listadas_cnpj_ind_active.csv')
    cnpjs = []
    for empresa in filteredEmp.values:
        cnpjs.append(empresa[1])
    filterDataSeries = data[data.CNPJ_CIA.isin(cnpjs)]
    filterDataSeries.to_csv(f'ActiveDataSeries/dfp_cia_aberta_DRE_ind_2010-2020_active.csv', index=True)    

    return

filterDataSeriesWithActiveAndLastBalance()
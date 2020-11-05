import pandas as pd

data = pd.read_csv('./Dados/dfp_cia_aberta_DRE_ind_2010-2020.csv')

def getAllListedEmp():
    empresas = data[['DENOM_CIA','CD_CVM', 'CNPJ_CIA']].drop_duplicates().set_index('CD_CVM')
    empresas.to_csv(f'Info/empresas_listadas_cnpj_ind.csv', index=True)
    return

def getAllDsConta():
    ds_conta = data['DS_CONTA'].drop_duplicates()
    ds_conta.to_csv(f'Info/ds_conta_ind.csv', index=False)
    return

def getAllDsContaActive():
    dataAct = pd.read_csv('./ActiveDataSeries/dfp_cia_aberta_DRE_ind_2010-2020_active.csv')
    ds_conta = dataAct['DS_CONTA'].drop_duplicates()
    ds_conta.to_csv(f'Info/ds_conta_ind_active.csv', index=False)
    return


getAllDsContaActive()
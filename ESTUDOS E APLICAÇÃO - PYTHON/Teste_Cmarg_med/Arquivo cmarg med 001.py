
"""
Created on Tue Aug  9 17:15:58 2022.

@author: E805511

===============================================================================
 Leitura do arquivo Cmarg Med
===============================================================================
 
 DADOS:
     
 - CUSTO MARGINAL DE DEMANDA - MEDIA PATAMARES
 - SUBMERCADO:SUDESTE
 - PLD AGOSTO - 2022 - 
 - Niveis para 30/07 NW 
 - Versao 28.0.3
 - Arquivo de sáida, sem patamar e com dados estatísticos


-------------------------------------------------------------------------------
 
 RETORNA:
 
 - Uma tabela bidimensional do caso cmarg med
 - Com 16 colunas e 10001 linhas
 - Exclui os dados estatísticos
 - Exporta para CSV
 - Paradigma Estruturado
 
 
 
 Tabela:
 -------------
 submercado | anos dos casos | series | todos os meses | media
 -------------
 Dados
 -------------
 
 
===============================================================================

 Refatorar: 
     
 - Anos
 - Aplicar pivot_table
 - Tratar os dados dos anos
    years = np.array([['ANO:', '2022'], ['ANO:', '2023']...
    anos = np.array([2022, 2023, 2024, 2025, 2026])

 - Cabeçalho
 - Submercado
 - Importar excel
 - Importar csv
    
===============================================================================
"""

import pandas as pd
import numpy as np


#%%Leitura do arquivo

path=(r"C:\Users\E805511\Documents\ESTUDOS E APLICAÇÃO - PYTHON\Teste_Cmarg_med\cmarg001-med.out")
arquivo_cmarg_med = pd.read_csv(path,
                skiprows = 4,
                delim_whitespace = True,
                skip_blank_lines = True,
                encoding = 'UTF-8',
               )



#%% Tratamento dos Dados

df_cmarg_med = pd.DataFrame(arquivo_cmarg_med)
df_cmarg_med.columns = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun','jul', 'ago', 'set','out', 'nov', 'dez', 'media' ]

#Drop dos dados estatísticos
df_cmarg_med = df_cmarg_med.dropna()

#Coluna series
df_cmarg_med2 = df_cmarg_med.rename_axis('series').reset_index()

#Exclusão das linhas com valores da media
index_MEDIA = df_cmarg_med2[df_cmarg_med2['series'] == 'MEDIA'].index
df_cmarg_med2.drop(index_MEDIA, inplace=True)
#print = Int64Index([2000, 4001, 6002, 8003, 10004], dtype='int64')


#Organizando o index
df_cmarg_med2.reset_index(drop = True, inplace= True)

#%%Confirma se as alterações estão corretas

"""
As séries se iniciam em:
-------------
índ. | anos |
-------------
0    | 2022
1999 | 2023
4000 | 2024
6000 | 2025
8000 | 2026
-------------
"""
df_cmarg_med2.iloc[7994:8006]


#%% Adicionando o submercado e anos no DataFrame

#Coluna anos
anos = np.array([2022, 2023, 2024, 2025, 2026])
anos = np.repeat(anos, 1, axis = 0). repeat(2000, axis = 0)
coluna_anos = pd.Series([anos])
df_cmarg_med2['anos do caso'] = anos


#Coluna submercado
submercado = np.array(['SUDESTE'])
submercado = np.repeat(submercado, 10000, axis = 0)
df_cmarg_med2['submercado'] = submercado


#Organizando as colunas
df_cmarg_med2 = df_cmarg_med2[['submercado', 'anos do caso', 'series', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun','jul', 'ago', 'set','out', 'nov', 'dez', 'media' ]]


#%% Exportando para CSV

df_cmarg_med2.to_csv('cmarg001-med.csv', 
                     index = False, 
                     encoding='utf-8')

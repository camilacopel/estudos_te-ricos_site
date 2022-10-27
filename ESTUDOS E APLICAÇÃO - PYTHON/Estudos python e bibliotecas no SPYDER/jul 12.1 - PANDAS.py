# =============================================================================
#                                 
#                                P A N D A S
# 
# =============================================================================
"""
TERMOS:
    
Series = é uma coluna com índice
DataFrame = tabela

______________________________________________________________________

Base de Dados = Dados abertos da ONS
    - intercambio entre subsistemas 2022
    - base horária, em MWmed;
    - As grandezas representam a soma das medidas de fluxo de potência ativa nas linhas 
    de transmissão de fronteira entre os subsistemas.;
    - 
    
"""

import pandas as pd
import numpy as np


# -----------------------------------------------------------------------------
# %%Primeiros passos
# -----------------------------------------------------------------------------

s1 = pd.Series(np.arange(1,10,2), name = "Coluna impar")
s2 = pd.Series(np.arange(0,10,2), name = "Coluna par")

#Data Table with random elements:
rng = np.random.RandomState()
#rng.randint(valores(X = linhas, y = colunas))
df = pd.DataFrame(rng.randint(0, 10, size=(3,4)),
                  columns = ['Bacia', 'resevatórios', 'vazão', 'ENA'],
                  index = ["estágio 1", "estágio 2", "estágio 3"])
                  
print(s1)
print(s2)
print(df)

# -----------------------------------------------------------------------------
# %%Importando dados
# -----------------------------------------------------------------------------
import pandas as pd
import numpy as np

pd.read_csv("C:/Users/E805511/Documents/ESTUDOS E APLICAÇÃO DAS BIBLIOTECAS/Estudos python e bibliotecas no SPYDER/INTERCAMBIO_NACIONAL_2022.csv", sep=";")

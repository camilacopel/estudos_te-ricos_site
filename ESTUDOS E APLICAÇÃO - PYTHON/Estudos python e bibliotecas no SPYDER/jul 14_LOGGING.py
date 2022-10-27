# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:37:47 2022

@author: E805511
"""

"""
LOG/LOGGING = ato de armazenar infomações sobre eventos ocorridos no SO
ou algum tipo de software.
- Tem relação direta com segurança da informação, rastreabilidade e encontrar anomalias;
- GErar no Apache HTTPS Server
- Valida apenas no contexto da aplicação, assim que parar de executar a variável
log é perdida;
- RElevante armazenar o histórico em arquivos;
"""



"""
Curiosidade:
    LOG: associado à navegação, usavam um livro com registro da velocidade e 
    progresso dos navios = log-book
    
"""
# =============================================================================
# %% EXEMPLO 1
# =============================================================================

import datetime

log = []

def soma1(a,b):
    r""" LOG(O dedo duro necessário dos sistemas)//Dicionário do Programador\nYT: Código Fonte TV."""
    s = a + b
    datahora = datetime.datetime.now()
    log.append([datahora, s])
    return s
    

print(soma1(1, 2))
print(soma1(3, 4))
print(log)

# =============================================================================
# %% EXEMPLO 2
# =============================================================================

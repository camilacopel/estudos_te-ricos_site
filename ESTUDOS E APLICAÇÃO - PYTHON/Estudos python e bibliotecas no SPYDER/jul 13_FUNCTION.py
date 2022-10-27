"""
Created on Wed Jul 13 17:00:54 2022
@author: E805511

UTILIZAÇÃO DO COMANDO DEF

"""

#Comum funcionana as funções?
# %%Criar comando personalizados
def linha ():
    """Sem parâmetros"""
    print("-"*35)
    
    
linha()
linha()    
print("       ENERGIA ARMAZENADA        ")
linha()
linha()

# =============================================================================
# %% trabalhar com parâmetros
# =============================================================================

#SOMATÓRIO
#a e b são os parâmetros

def soma(a,b):
    """Apenas uma soma simples"""
    s = a + b
    print(s)


#Programa Principal
soma(1, 2)
soma(5, 4)
soma(10, 2)

"""or"""

#Desepacotamento
#def somatorio(*valores):
#    s1 = 0
#    s1 = [s1+=num for num in valores]
#    print(f"Valores: {valores} e somatório: {s1}")

#somatorio(5,2)
#somatorio(1,2,3)
    
# =============================================================================
# %% Exercício 98 - PRINT ESPECIAL
# =============================================================================

#FEzer um programa que a função escreva()
#receba um texto como parâmetro e mostre uma mensagem de tamanho adaptável

#Função
def titulo(msg):
    tamanho = len(msg)+4
    print("~"*tamanho)
    print(f"  {msg}")
    print("~"*tamanho)
    
#Programa Principal
titulo("Intercambio Nacional 2022")

# =============================================================================
# %% Exercício 98 - Função Contador
# =============================================================================
def contador():
    
 print("-="*50)
 print(f"  {msg}")
 print("-="*50)
 


"""
Created on Mon Jul 12 2022
Para renomear essa bosta
Source -> Run Code Analyses or  just click F8
@author: E805511
"""

# =============================================================================
# %%RESOLUÇÃO PADRÃO
# =============================================================================

#Preço em dólar
lista_preco = [500., 1500., 300., 4669., 30., 567.]

#conversão para real
lista_preco_real = []
for preço in lista_preco:
    lista_preco_real.append(preço*5.42)
#print(lista_preco_real)

#Para saber o imposto a pagar
#Apenas para valores acima de mil dólares 
imposto = []
for preço in lista_preco:
    if preço > 1000:
        imposto.append(preço*0.5)
        
        imposto_real = []
        for i in imposto:
            if len(imposto)>1:
                imposto_real.append(i*5.42)
        
#print(f" Seus produtos em dólar:{lista_preco}\n O preço em reais dos produtos são:{lista_preco_real}\n")
#print(f" O valor do imposto em dólar: {sum(imposto)} e em real: {sum(imposto_real)}")
#print(" O preço total: ", sum(lista_preco_real) + sum(imposto_real))
      
      
# -----------------------------------------------------------------------------
# %%   LIST  COMPREHENSION
# -----------------------------------------------------------------------------

"""
#formato da list comprehension
#[expr for item in lista] = aplique a expressão expr em cada item da lista.
______________________________________________________

List Comprehensions com if
[expr for item in lista if cond] = 
Aplique a expressão expr em cada item da lista caso a condição cond seja satisfeita.
______________________________________________________

List Comprehensions com vários if’s
expr for item in lista if cond1 if cond2] = 
Podemos verificar várias condições na lista dentro da mesma list comprehension.
Entretanto o resultado será uma AND, ou seja, printa apenas os resultados
que aparecem nas duas condições

a = [numero for numero in range(100) if numero % 5 == 0]
print(a) = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

resultado = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]
print(resultado) = [0, 30, 60, 90]
______________________________________________________

List Comprehensions com if + else
[resultado_if if expr else resultado_else for item in lista] = 
para cada item da lista, aplique o resultado resultado_if se a expressão expr for verdadeira,
caso contrário, aplique resultado_else.
______________________________________________________
"""



lista_preco2 = [500., 1500., 300., 4669., 30., 567.]

#Valores em reais
lista_preco_real2 = [preço2*5.42 for preço2 in lista_preco2] 
#Imposto
imposto2 = [preço2*0.5 for preço2 in lista_preco2 if preço2 > 1000]
imposto_real2 = [imp2*5.42 for imp2 in imposto2 if len(imposto2)>1]
print(f" Seus produtos em dólar:{lista_preco}\n O preço em reais dos produtos são:{lista_preco_real2}\n O valor do imposto em dólar: {sum(imposto2)} e em real: {sum(imposto_real2)}\n O preço total: ", sum(lista_preco_real2) + sum(imposto_real2))


# -----------------------------------------------------------------------------
# %% APLICADO À MATRIZES
# -----------------------------------------------------------------------------

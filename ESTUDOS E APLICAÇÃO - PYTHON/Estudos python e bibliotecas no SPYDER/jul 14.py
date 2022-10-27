# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:03:27 2022
@author: E805511
"""

"""
______________________________________________________________

Criando o código uma única vez poo usá-lo várias vezes
______________________________________________________________

CLASSES: 
    - Ao invés de fazer o código na forma de scripts, usa-se a orientação ao objeto
    - Toda classe tem atributos(Características do objeto) e 
    - métodos(o que aquela classe consegue fazer) = funções;
    - Usando para grande sistemas
    - A função recebe ()
    
INSTANCE:
    - É O objeto criado (filmes)
    - Pode-se ter diversas instâncias em uma classe
    - E roda a função __init__;
    - Com uma instância posso referenciar vários objetos
    
CONSTRUTOR
SELF: identifica a instância 


"""


#Things for class Movie to remember
#title, storyline, poster_image and trailer_youtube

class Movie():
    """TESTE."""
    #MÉTODO CONSTRUTOR
    #init: Inicializa as informações, como título, sinopse, etc
    def __init__(self, movie_title, movie_storyline, poster, trailer):
        #São as variáveis de MOVIE com as informações que o init receberá
        #Caracterpisticas   /= Variáveis
        self.title           = movie_title
        self.storyline       = movie_storyline
        self.poster_image    = poster
        self.trailer_youtube = trailer 
    
        
    #Cada def é uma função independente dentro da classe"""
    def canais(self):
        self.canais()
        
        
    def teste(self, plano, lista_de_planos):
        self.lista_de_planos = lista_de_planos
        
        if plano in lista_de_planos:
            self.plano = plano
        #else:
            #Dessa maneira o cliente nem é criado
            #raise Expetion("Plano Inválido")
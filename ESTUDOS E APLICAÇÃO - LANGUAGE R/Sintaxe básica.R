#Testando 
#A ideia original do R é transformar usuários em programadores
#“… to turn ideas into software, quickly and faithfully.”
#– John M. Chambers.

#-----------------------------------------------------------------------
#Ambiente de estatística computacional e gráficos,
#com conjunto de ferramentas para manipulação de dades, cálculos e gráficos
#Sendo um dos pontos fortes da linguagem
#Assim como Pyrhon apresenta um modo interativo, executando expressões por linhas de comando
#ggplot2 <- apresentação de belos gráficos e até interativos
#Python = enfatiza os objetos
#R = enfatiza as funções

print('Rélou Uorldy')
d <- c(23.5, 34)
mean(d)

#-----------------------------------------------------------------------
nomes <- c('Maria', 'João', 'Vania', 'Fulana', 'Enzo', 'Lia')
idades <- c(56, 45, 32, 12, 25, 46)

df <- data.frame(nomes, idades)
print(df)
df$idades
df$idades[df$nomes == 'Maria']

#Conditions ------------------------------------------------------------
if (df$idades[df$nomes == 'Maria'] > df$idades[df$nomes == 'Vania']){
  "Maria é mais velha"
}else{
  "Vania é mais velha"
}

#Loop - Quem tem a maior idade -----------------------------------------
maior <- 0
for(i in df$idades){
  if (i > maior){maior <- i}
}

df$nomes[df$idades == maior]

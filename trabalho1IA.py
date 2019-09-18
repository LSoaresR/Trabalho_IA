#!/usr/bin/env python
# coding: utf-8

# # Trabalho 1 - Métodos de busca

# Equipe:
# - Felipe Sobreira Cassimiro
# - Grimberg Cryzan
# - Lucas Soares

# Tasks:
#  - [] Estado inicial não da match no inicio, criar objeto estado para gerar filhos para próximas ações
#  - [] Criar lista de estados percorrenso, e estados a percorrer (sucessores)

# In[22]:


import copy


# In[23]:


# Variáveis iniciais
objetivoPrincipal = [1,2,3,4,5,6,7,8,0];
objetivo1 = [1,2,3,4,5,6,7,8,0];
objetivo2 = [0,2,4,3,1,6,7,5,8];
objetivo3 = [2,4,6,3,1,0,7,5,8];

entrada1 = [2,0,4,3,1,6,7,5,8];
entrada2 = [4,3,2,5,1,0,7,6,8];
entrada3 = [1,2,0,4,5,3,7,8,6];
entrada4 = [1,2,3,4,5,6,7,0,8];

igual = [1,2,3,4,5,6,7,8,0];


# In[24]:


def printaValores(titulo, valores):
    print(titulo)
    print("________")
    print(str(valores[0]) + " | "+ str(valores[1]) + " | " +str(valores[2])  )
    print("--------")
    print(str(valores[3]) + " | " + str(valores[4]) + " | "+ str(valores[5])  )
    print("--------")
    print(str(valores[6]) + " | " + str(valores[7]) + " | " +str(valores[8])  )


# In[25]:


def testaEstados(estadoAtual, objetivo):
    #print("Testando estados !")
    if estadoAtual == objetivo:
        return True
    else:
        return False


# In[26]:


def trocaValores(idOr, inDest, valores):
    #print("Trocando valores !")
    valores[idOr], valores[inDest] = valores[inDest], valores[idOr]


# In[27]:



class Estado:
        
    # O índice é a posição do '0' no puzzle
    def __init__(self, indice, pai, valores):
        self.indice = indice
        self.pai = pai
        self.valores = valores
          


# In[28]:


def busca_largura(estadoInicial, objetivo):
    
    print("Entrada: " + str(estadoInicial))
    
    # Inicialmente testamos se a entrada se iguala ao objetivo
    if estadoInicial == objetivo:
        print("Objetivo alcançado !")
        return
    
    # Utilizaremos essa lista para guardar os próximos nós (filhos) a serem movidos e testados
    listaSucessores = []
    
    
    # Criamos o estado raiz, iremos ver para onde ele pode se mover, executar essas ações
    # se encontrarmos o estado objetivo paramos, caso contrário, criamos um novo estado a percorrer
    raiz = Estado(estadoInicial.index(0), None, estadoInicial);
    
    
    # Por padrão, nossa ordem de mover é : 'cima' - 'direita' - 'baixo' - esquerda
    # então ele vai mover para o primeiro que der, nessa ordem, *mas não pode voltar para o índice
    # de onde se originou. Após o movimento, se não tem match geramos um filho, e adicionamos aos sucessores
    
    noh = copy.deepcopy(raiz)
    estadoAtual = estadoInicial.copy()
    match = False
    condicao = True
    
    while(condicao):
        
        #printaValores("Ind.:"+str(noh.indice)+" Pai:"+str(noh.pai),estadoAtual.copy())
        
        #print("Estado auxiliar possui os valores: " + str(estadoAtual))
        #print("Nó atual possui - indice:" + str(noh.indice) + " , pai:" + str(noh.pai))
        
        # posso mover para cima? 
        if( (noh.indice in [3,4,5,6,7,8]) and ((noh.indice - 3 ) != noh.pai ) ):
            #print("Movendo indice:" + str(noh.indice) + ", para indice:" + str(noh.indice-3) + " - CIMA")
            
            trocaValores(noh.indice, noh.indice-3, estadoAtual)
            #printaValores("Ind.:"+str(noh.indice)+" Pai:"+str(noh.pai),estadoAtual.copy())
            match = testaEstados(estadoAtual, objetivo)
            if(not match):
                novoNoh = Estado(estadoAtual.index(0), noh.indice, estadoAtual.copy());
                listaSucessores.append(novoNoh)
                trocaValores(noh.indice-3, noh.indice, estadoAtual)
            else:
                print("Deu match !")
                print("Resultado: " + str(estadoAtual))
                return
            
            
        # posso mover para direita?
        if( (noh.indice in [0,1,3,4,6,7]) and ((noh.indice + 1) != noh.pai ) ):
            #print("Movendo indice:" + str(noh.indice) + ", para indice:" + str(noh.indice+1) + " - DIREITA")
            trocaValores(noh.indice, noh.indice+1, estadoAtual)
            #printaValores("Ind.:"+str(noh.indice)+" Pai:"+str(noh.pai),estadoAtual.copy())
            match = testaEstados(estadoAtual, objetivo)
            if(not match):
                novoNoh = Estado(estadoAtual.index(0), noh.indice, estadoAtual.copy());
                listaSucessores.append(novoNoh)
                trocaValores(noh.indice+1, noh.indice, estadoAtual)
            else:
                print("Deu match !")
                print("Resultado: " + str(estadoAtual))
                return
            
            
        # posso mover para baixo?
        if( (noh.indice in [0,1,2,3,4,5]) and ((noh.indice + 3) != noh.pai ) ):
            #print("Movendo indice:" + str(noh.indice) + ", para indice:" + str(noh.indice+3) + " - BAIXO")
            trocaValores(noh.indice, noh.indice+3, estadoAtual)
            #printaValores("Ind.:"+str(noh.indice)+" Pai:"+str(noh.pai),estadoAtual.copy())
            match = testaEstados(estadoAtual, objetivo)
            if(not match):
                novoNoh = Estado(estadoAtual.index(0), noh.indice, estadoAtual.copy());
                listaSucessores.append(novoNoh)
                trocaValores(noh.indice+3, noh.indice, estadoAtual)
            else:
                print("Deu match !")
                print("Resultado: " + str(estadoAtual))
                return
            
        # posso mover para esquerda?
        if( (noh.indice in [1,2,4,5,7,8]) and ((noh.indice - 1) != noh.pai ) ):
            #print("Movendo indice:" + str(noh.indice) + ", para indice:" + str(noh.indice-1) + " - ESQUERDA")
            trocaValores(noh.indice, noh.indice-1, estadoAtual)
            #printaValores("Ind.:"+str(noh.indice)+" Pai:"+str(noh.pai),estadoAtual.copy())
            match = testaEstados(estadoAtual, objetivo)
            if(not match):
                novoNoh = Estado(estadoAtual.index(0), noh.indice, estadoAtual.copy());
                listaSucessores.append(novoNoh)
                trocaValores(noh.indice-1, noh.indice, estadoAtual)
            else:
                print("Deu match !")
                print("Resultado: " + str(estadoAtual))
                
                return
        
        # SE CHEGOU AQUI, FOI MOVIDO O '0' PARA TODAS AS POSIÇÕES DISPONÍVEIS, GEROU FILHOS
        # E AGORA PRECISA RODAR CADA UM DESSES FILHOS
        # OU SEJA noh = sucessor
        
        #condicao = False
        
        noh = listaSucessores.pop(0);
        estadoAtual = noh.valores.copy();
        
        #print("Percorrendo próximo sucessor")
        
    # vou mover, depois comparo , se der match, paramos, caso contrário continuamos
    # e adicionamos o que não deu match em uma lista de filhos
    
    # Caso o objetivo não esteja alcançado, temos que encontrar o '0' no puzzle
    # e determinar as ações que a função sucessor pode executar
    
    
    


# In[29]:


#Teste só preciso mover para esquerda
busca_largura(entrada1, objetivo2)


# In[30]:


busca_largura(entrada1, objetivo3)


# In[31]:



busca_largura(entrada1, objetivoPrincipal)


# In[18]:


busca_largura(entrada1, objetivoPrincipal)


# In[20]:


busca_largura(entrada4, objetivoPrincipal)


# In[21]:


busca_largura(entrada3, objetivoPrincipal)


# In[ ]:





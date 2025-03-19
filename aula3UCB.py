#APRENDENDO LOOPS EM python

# for i in range(10): 
#     print(i)

#---------------------------------------------

# c = 0 
# while c < 10:
#     print(c)
#     c+= 1   #incrementando mais 1
#---------------------------------------------

# for i in range(10):
#     if i == 5:
#         break  #LOOP PARA QUANDO ENCONTRA O NUMERO 5
#     print(i)

# for i in range(10):
#     if i == 5:
#         continue #LOOP PULA O NUMERO 5 E CONTINUA O PROGRAMA
#     print(i)
#---------------------------------------------------------------

#arrays - lista de elementos

# arr = [1,2,3,4,5,6,7,8,9,10]
# arr_names = ["Giovanna", "Barbosa", "Ferreira"]

# for i in arr_names:
#     print(i)
#------------------------------------
    #OPERADORES LÓGICOS
# x=10
# y=20

# if x > 0 or y > 0:
#     print("Ambos x e y são positivos")

# if x > 0 or y > 0:
#     print("Pelo menos um deles é positivo")

# if not x > 0:
#     print("x não é positivo")
#----------------------------------------------
    
# my_list = [5,4,3,2,1]
#print(my_list)

# print(my_lits[0])
# print(my_lits[1])
# print(my_lits[2])

# #IMPRIME A LISTA DE TRAZ PRA FRENTE
# print(my_lits[-1]) 
# print(my_lits[-2])
# print(my_lits[-3])

# print (my_lits[0:3])
# print(my_lits[1:4])

# my_list.append(6) #METODO APPEND PARA ADICIONAR UM NUMERO NA LISTA
# print(my_list)

# my_list.insert(0, 0) #ADICIONA UM NUMERO NO INDICE 0
# print(my_list)

# my_list.remove(1) #REMOVE O ELEMENTO E NÃO O INDICE
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list.reverse()
# print(my_list)

# my_list.sort() #ORGANIZA A LISTA
# print(my_list)

# my_list.extend([6,7,8]) #AUMENTA A LISTA
# print(my_list)

# print(my_list.count(1)) #QUANTAS VEZES UM NUMERO APARECE NA MINHA LISTA

# print(my_list.index(1)) #posição que meu elemento aparece

#-------------------------------------------------------------------------------------

#TUPLE / TUPLAS

my_tuple = (1,2,3,4,5)

print(my_tuple.index(1))

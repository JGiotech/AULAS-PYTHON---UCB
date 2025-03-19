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
x=10
y=20

if x > 0 or y > 0:
    print("Ambos x e y são positivos")

if x > 0 or y > 0:
    print("Pelo menos um deles é positivo")

if not x > 0:
    print("x não é positivo")

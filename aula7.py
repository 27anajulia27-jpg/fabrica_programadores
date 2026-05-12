lista =["Kamilly","Maria","João"]

x = input("Digite seu nome\n")

if  lista in lista:
    print("Nome esta na lista !!!")
else: 
    print('Nome não esta na lista!!!')


#---------------------------------------------------------------------

lista = ["Bia", "João","Matheus"]

x = input("Digite seu idade:\n")

if lista in lista:
        print("voce pode votar !!!")
else:
        print("Voce não pode votar !!!")

#---------------------------------------------------------------------

lista = ["BMW","mercedes-bens"," Audi","Aston martin"]
preco = [35000,40000,2000,80000] 

loja = ["chivy","Fiat", "Peugeot","volkswagem'"]
preco_loja =[1000,500,1,99,2000,6000,9000]

loja_barato = []
loja_caro =[]
 
for preco in preco_loja:
        index_preco = preco_loja.index("preco")

if preco <2000:
     loja_barato.append(estoque[index_preco])

else:
       loja_barato.append(estoque[i])
i=i+ i
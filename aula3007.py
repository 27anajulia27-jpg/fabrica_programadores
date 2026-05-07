lista_usuario = ["Bia","Matheus","João"]
lista_senha = ["Bia555","Matheus777","João9526"]

user = input("Digite um nome:\n")
senha = input("Digite sua senha:\n")

index_senha = lista_senha.index(senha)
print(index_senha)
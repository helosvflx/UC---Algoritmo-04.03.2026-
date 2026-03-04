#Crie uma lista chamada COMPRAS com pelo menos 5 itens.
#Adicione um novo item à lista de forma que o usuário digite

compras = ["arroz", "feijão", "macarrão", "leite", "café"]
print("Lista de compras atual: ", compras)

novoItem = input("Adicione um novo item: ")
compras.append(novoItem)

print("Lista de compras atualizada: ", compras)
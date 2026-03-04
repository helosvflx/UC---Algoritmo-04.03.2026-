#primeira questao:
num1 = float(input("Digite o primeiro número real: "))
num2 = float(input("Digite o segundo número real: "))

soma = num1 + num2
produto = num1 * num2

print("Soma: ", soma)
print("Produto: ", produto)



#segunda questao:
numero = int(input("Digite um número inteiro positivo: "))

if numero % 2 == 0:
    resultado = numero ** 2
    print(f"O número {numero} é par. O seu cubo é: {resultado}")
else:
    resultado = numero ** 3
    print(f"O número {numero} é ímpar. O seu cubo é: {resultado}")



#terceira questao:
login1 = "procopio"
senha1 = 12345
login2 = "paiva"
senha2 = 54321

login1 = input("Digite o seu primeiro login: ")
senha1 = input("Digite a senha: ")

if login1 == "procopio" and senha1 == 12345:
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem.")


login2 = input("Digite o seu segundo login: ")
senha2 = input("Digite a senha: ")

if login2 == "paiva" and senha2 == 54321:
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem.")



#quarta questao:
senha_correta = "123456"
tentativas = 3
nome = "seuNome"

while tentativas > 0:
    senha = input("Digite sua senha")
    nome = input("Digite o seu nome: ")

if senha == senha_correta:
    print(f"Olá, {nome}. Seja bem vindo ao nosso banco.")
else:
    tentativas -= 1
    
    if tentativas == 2:
        print("Senha incorreta! Você ainda tem 2 tentativas.")
    elif tentativas == 1:
        print("Senha incorreta! Você ainda tem 1 tentativa.")
    else:
        print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
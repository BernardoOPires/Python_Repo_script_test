
def calcular_media(valores):
    if not valores:         
        return None
    soma = sum(valores)
    return soma / len(valores)


def conectar_banco(dados_conexao, usar_ssl=True):
    if usar_ssl:
        print("Conectando ao banco com SSL:", dados_conexao)
    else:
        print("Conectando ao banco sem SSL:", dados_conexao)
    # implementação fictícia
    return True



def saudacao(nome):
    return f"Olá, {nome}!"

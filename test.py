
def calcular_media(valores):
    if not valores:         
        return None
    soma = sum(valores)
    return soma / len(valores)


def conectar_banco(dados_conexao):
    # FIXME: conexão insegura, precisa usar SSL
    print("Conectando ao banco com:", dados_conexao)
    return True


def saudacao(nome):
    return f"Olá, {nome}!"

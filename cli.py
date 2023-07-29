#biblioteca para gerar a linha de comando
import argparse
#biblioteca usada para consumir a API
import requests

def consultar_cep(cep):
    # verificação se o CEP é uma string vazia
    if not cep.strip():
        print(" =========== CEP vazio ===========")
        exit()

    endereco = f"https://viacep.com.br/ws/{cep}/json/"
    resquest = requests.get(endereco)

    # Validação do dado inserido
    if resquest.status_code == 200:
        dados_cep = resquest.json()
        if "erro" in dados_cep:
            print("=========== CEP não encontrado ===========")
            exit()
        return dados_cep
    elif len(cep) >= 9:
        print(" =========== CEP inválido ===========")
        exit()
    elif resquest.status_code == 400:
        print(" =========== CEP inválido ===========")
        exit()
    else:
        print("=========== Erro na consulta do CEP =========== ")
        exit()
# tratamento das informações de Json para string
def exibir_cep(dados_cep):
    print("==============================================")
    print("Resultado da Busca: CEP:", dados_cep["cep"])
    print("Logradouro:", dados_cep["logradouro"])
    print("Complemento:", dados_cep["complemento"])
    print("Bairro:", dados_cep["bairro"])
    print("Cidade:", dados_cep["localidade"])
    print("Estado:", dados_cep["uf"])
    print("==============================================")
    
#criação da linha de comando 
def main():
    parser = argparse.ArgumentParser(description="Utilitário de consulta de CEP")
    parser.add_argument("-cep", required=True, help="Número do CEP para consulta")
    args = parser.parse_args()

    try:
        dados_cep = consultar_cep(args.cep)
        exibir_cep(dados_cep)
    except ValueError as e:
        print("Erro:", e)
#inicialização do programa
if __name__ == "__main__":
    main()


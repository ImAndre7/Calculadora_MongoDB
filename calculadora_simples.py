import pymongo

def calculadora():
    """Calculadora básica com armazenamento no MongoDB."""

    # Conecte-se ao MongoDB
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    db = client["calculadora_db"]
    resultados = db["resultados"]

    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite a opção: ")

        if escolha == '5':
            print("Saindo da calculadora.")
            break

        if escolha not in ('1', '2', '3', '4'):
            print("Opção inválida. Tente novamente.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = num1 + num2
            operacao = "Adição"
        elif escolha == '2':
            resultado = num1 - num2
            operacao = "Subtração"
        elif escolha == '3':
            resultado = num1 * num2
            operacao = "Multiplicação"
        elif escolha == '4':
            if num2 == 0:
                print("Erro: Divisão por zero.")
                continue
            else:
                resultado = num1 / num2
                operacao = "Divisão"

        print("Resultado:", resultado)

        # Armazene o resultado no MongoDB
        resultado_document = {
            "num1": num1,
            "num2": num2,
            "operacao": operacao,
            "resultado": resultado
        }
        resultados.insert_one(resultado_document)

if __name__ == "__main__":
    calculadora()
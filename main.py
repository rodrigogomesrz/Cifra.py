
from cifra_cesar import codificar, decodificar
from hash_senhas import gerar_hash
from forca_bruta import simular_forca_bruta
from senha_segura import gerar_senha


def mostrar_boas_praticas():
    praticas = [
        "Use senhas longas, únicas e aleatórias.",
        "Ative a autenticação multifator.",
        "Nunca armazene senhas em texto puro.",
        "Utilize Argon2id, scrypt ou bcrypt para senhas reais.",
        "Mantenha os programas atualizados.",
        "Limite tentativas de login em sistemas reais.",
        "Faça backups e proteja informações sensíveis."
    ]

    for numero, pratica in enumerate(praticas, start=1):
        print(f"{numero}. {pratica}")


def main():
    while True:
        print("\n=== SEGURANÇA DA INFORMAÇÃO ===")
        print("1 - Codificar mensagem")
        print("2 - Decodificar mensagem")
        print("3 - Gerar hash SHA-256")
        print("4 - Simular força bruta")
        print("5 - Gerar senha segura")
        print("6 - Boas práticas")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao in ("1", "2"):
            mensagem = input("Mensagem: ")

            try:
                deslocamento = int(input("Deslocamento: "))

                if opcao == "1":
                    print("Resultado:", codificar(
                        mensagem, deslocamento
                    ))
                else:
                    print("Resultado:", decodificar(
                        mensagem, deslocamento
                    ))

            except ValueError:
                print("Digite um deslocamento inteiro.")

        elif opcao == "3":
            texto = input("Texto de demonstração: ")
            print("Hash:", gerar_hash(texto))

        elif opcao == "4":
            senha = input(
                "Senha numérica fictícia (1 a 4 dígitos): "
            )

            if senha.isdigit() and 1 <= len(senha) <= 4:
                encontrada, tentativas = simular_forca_bruta(senha)
                print("Encontrada:", encontrada)
                print("Tentativas:", tentativas)
            else:
                print("Entrada inválida.")

        elif opcao == "5":
            try:
                tamanho = int(input("Tamanho da senha (12 a 128): "))

                if 12 <= tamanho <= 128:
                    print("Senha:", gerar_senha(tamanho))
                else:
                    print("Tamanho inválido.")
            except ValueError:
                print("Digite um número inteiro.")

        elif opcao == "6":
            mostrar_boas_praticas()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()


import secrets
import string


def gerar_senha(tamanho=16):
    caracteres = (
        string.ascii_letters
        + string.digits
        + "!@#$%&*+-_?"
    )

    return "".join(
        secrets.choice(caracteres)
        for _ in range(tamanho)
    )


if __name__ == "__main__":
    try:
        tamanho = int(input("Tamanho da senha (12 a 128): "))

        if 12 <= tamanho <= 128:
            print("Senha gerada:", gerar_senha(tamanho))
        else:
            print("Escolha um tamanho entre 12 e 128.")

    except ValueError:
        print("Digite um número inteiro válido.")

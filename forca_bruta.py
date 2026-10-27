
import itertools
import string
import hmac


def simular_forca_bruta(senha_alvo, tamanho_maximo=4):
    tentativas = 0

    for tamanho in range(1, tamanho_maximo + 1):
        for combinacao in itertools.product(
            string.digits, repeat=tamanho
        ):
            tentativa = "".join(combinacao)
            tentativas += 1

            if hmac.compare_digest(tentativa, senha_alvo):
                return tentativa, tentativas

    return None, tentativas


if __name__ == "__main__":
    senha = input(
        "Digite uma senha numérica fictícia de 1 a 4 dígitos: "
    )

    if not senha.isdigit() or not 1 <= len(senha) <= 4:
        print("Entrada inválida. Use de 1 a 4 dígitos.")
    else:
        encontrada, total = simular_forca_bruta(senha)

        if encontrada is not None:
            print("Senha encontrada:", encontrada)
            print("Tentativas realizadas:", total)
        else:
            print("Senha não encontrada.")

        print("Simulação local concluída.")

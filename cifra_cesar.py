
def cifra_cesar(mensagem, deslocamento):
    resultado = ""

    for letra in mensagem:
        if letra.isalpha() and letra.isascii():
            base = ord("A") if letra.isupper() else ord("a")
            nova_letra = chr(
                (ord(letra) - base + deslocamento) % 26 + base
            )
            resultado += nova_letra
        else:
            resultado += letra

    return resultado


def codificar(mensagem, deslocamento):
    return cifra_cesar(mensagem, deslocamento)


def decodificar(mensagem, deslocamento):
    return cifra_cesar(mensagem, -deslocamento)


if __name__ == "__main__":
    texto = input("Digite uma mensagem: ")
    deslocamento = int(input("Digite o deslocamento: "))

    codificada = codificar(texto, deslocamento)
    original = decodificar(codificada, deslocamento)

    print("Mensagem codificada:", codificada)
    print("Mensagem decodificada:", original)
# Cifra.py

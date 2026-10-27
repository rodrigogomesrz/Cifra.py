
import hashlib
import hmac


def gerar_hash(texto):
    return hashlib.sha256(
        texto.encode("utf-8")
    ).hexdigest()


def verificar_hash(texto, hash_esperado):
    hash_calculado = gerar_hash(texto)

    return hmac.compare_digest(
        hash_calculado, hash_esperado
    )


if __name__ == "__main__":
    texto = input("Digite um texto para gerar o hash: ")
    hash_gerado = gerar_hash(texto)

    print("Hash SHA-256:", hash_gerado)

    verificacao = verificar_hash(texto, hash_gerado)
    print("Hash verificado:", verificacao)

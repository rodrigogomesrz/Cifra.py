
# Projeto de Segurança da Informação com Python

## Objetivo

Desenvolver um programa educacional para estudar conceitos
de criptografia, funções hash, força bruta e boas práticas
de segurança da informação utilizando Python.

## Funcionalidades

- Criptografia e decodificação com a Cifra de César.
- Geração e verificação de hashes SHA-256.
- Simulação local de força bruta com senhas fictícias.
- Geração de senhas aleatórias com o módulo `secrets`.
- Recomendações de segurança da informação.
- Uso de condicionais e laços de repetição.

## Tecnologias

- Python 3
- hashlib
- hmac
- itertools
- secrets
- string

## Como executar

1. Instale o Python 3.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python main.py
```

Em alguns sistemas, pode ser necessário usar `python3 main.py`.

## Segurança

A Cifra de César é apenas didática e não protege informações
reais. SHA-256 puro não deve ser utilizado para armazenar
senhas de usuários. Sistemas reais devem utilizar algoritmos
específicos para senhas, como Argon2id, scrypt ou bcrypt,
com salt e parâmetros adequados.

A simulação de força bruta funciona apenas localmente e
não tenta acessar sistemas externos.

## Boas práticas

- Utilizar senhas longas, únicas e aleatórias.
- Ativar autenticação multifator.
- Manter programas atualizados.
- Proteger informações sensíveis.
- Limitar tentativas de autenticação.
- Fazer cópias de segurança.

## Finalidade

Projeto desenvolvido para fins educacionais, com foco no
aprendizado de Python e dos fundamentos da segurança digital.

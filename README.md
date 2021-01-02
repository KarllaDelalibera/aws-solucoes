[![python](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Repositório destinado a criação de funções úteis para utilização de serviços AWS via Python

O objetivo desse repositório é disponibilizar algumas soluções simples, mas que facilitam o desenvolvimento de um código em Python quando o mesmo precisa utilizar serviços AWS.


## Soluções já disponíveis

- [X] Funções úteis para o serviço: STS (Security Token Service)
- [X] Funções úteis para o serviço: Athena
- [X] Funções úteis para o serviço: S3


## Como utilizar

No terminal, clone o projeto:

```bash
$ git clone https://github.com/KarllaDelalibera/aws-solucoes.git
```

Dentro da pasta aws-solucoes, execute os seguintes comandos no terminal:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pre-commit install
```
## Testes e cobertura

Para rodar os testes e vizualizar o relatório de cobertura, execute:

```bash
$ pytest -x --cov=s3 --cov-report=term-missing --cov-report=html:htmlcov
```
> Status do Projeto: Em desenvolvimento :construction:

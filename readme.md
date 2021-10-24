# API de validação de Password

Este serviço desenvolvimento em `python` garante que o password é valido, quando:

- Nove ou mais caracteres.
- Ao menos 1 dígito.
- Ao menos 1 letra minúscula.
- Ao menos 1 letra maiúscula.
- Ao menos 1 caractere especial.
- Considere como especial os seguintes caracteres: !@#$%^&*()-+.
- Não possuir caracteres repetidos dentro do conjunto.

## Solução (Racional)

Elaborei imaginando algumas premissas básicas para que a evolução do serviço seja orgânica,

- As regras `Rules` implementadas são independentes de modo que é possivel montar outros conjuntos de regras sem impactar as que esteja funcionando. Podendo ser serviço externo (api) ou lib.

- API exposta no metodo `POST` é um Recurso desacoplado das regras, não possui uma dependência direta, é abstraído pelo Controller.

- A model implementada está isolada de modo que é possivel reutilizar em outros recursos (endpoints) neste caso não é escopo, mas é possivel.

## Instalação ( Pré - requisitos )

- python3

```sh
#macos
brew install python3

#ubutu
 sudo apt-get install python3
```

- pip

```sh
#macos
 sudo easy_install pip

 #ubuntu
 sudo apt-get install python3-pip
```

## Configurando o ambiente de desenvolvimento

No diretório do projeto `./` vamos criar o virutalenv para que possamos instalar os packages do projeto de forma isolada.

```sh
python3 -m virtualenv venv
```

Note que será criada uma pasta com o nome de `venv`, após a criação do ambiente vamos ativa-lo.

```sh
activate ./venv/bin/activate
```

Feito isso, agora vamos instalar as dependência do serviço.

```sh
pip3 install -r requirements.txt

```

## Executar o serviço (local)

```shell
python app.py
```

Para acessar o swagger da api ela estará no `http://localhost:5000/doc`

## Docker

```sh
./build.sh

# after

./run.sh

```

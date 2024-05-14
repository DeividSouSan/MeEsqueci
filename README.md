## Como rodar?

### Clonando o repositório
Primeiro, clone o repositório para a sua máquina. Você pode fazer isso baixando o projeto ou utilizando o seguinte comando no seu terminal:

```
https://github.com/DeividSouSan/MeEsqueci.git
```

Após baixar acesse a pasta do projeto.

### Criando um ambiente virtual
Agora, nós temos todo o projeto baixado, mas precisamos instalar as dependencias. Não queremos as dependencias fiquem na nossa máquina conflitando com as dependicas que já existem, então vamos utilizar um ambiente virtual.

```
python3 -m venv .venv
```

Esse comando vai criar uma pasta chamada `.venv` no diretório do projeto.

Vamos ativar ele com:

```
source .venv/bin/activate
```

### Instalando as dependências
Com o ambiente virtual criado e ativado, podemos instalar as dependencias do projeto.

```
pip install requirements.txt
```

### Rodando
Finalmente, com todas as dependencias instaladas podemos rodar o nosso projeto.

```
guvicorn wsgi:app
```

Isso vai abrir um servidor em uma porta aleatória, mas verificar no seu terminal o endereço correto e acessa-lo.

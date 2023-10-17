# Local events API

O objetivo do projeto é a criação de um website que permita conseguir informações de eventos próximos na região de São Paulo

## Pré-requisitos

Certifique-se de que o Python esteja instalado. Você pode verificar se o Python está instalado executando o seguinte comando no seu terminal:

```bash
python --version
```
## Instalação

Siga estas etapas para configurar o ambiente de desenvolvimento:

```bash
# Clone o repositório
git clone https://github.com/gsajulia/local-events-api.git
cd local-events-api
```
1) Primeira opção
```bash

# Instale as dependências
pip install -r requirements.txt

# Clique no play ou rode
uvicorn main:app --reload 
```

2) Segunda opção
```bash
# Opcionalmente, crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows, use "venv\Scripts\activate"

# Instale as dependências
pip install -r requirements.txt

uvicorn main:app --reload
```

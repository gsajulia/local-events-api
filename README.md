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

# Opcionalmente, crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows, use "venv\Scripts\activate"

uvicorn main:app --reload # (or use the play if you don't use venv)

# Instale as dependências
pip install -r requirements.txt

# Exercícios Beecrowd

Lista de exercícios feitos através da plataforma [beecrowd](https://www.beecrowd.com.br/judge/en/login), com o objetivo de treinar lógica de programação.

### 📋 Pré-requisitos

Segue os requisitos necessários para testar cada código em sua máquina:

```
* Editor de código (sua escolha)
```

* Python
```
* Instalação de dependencias para exercícios SQL
    * Utilize o ambiente virtual de sua escolha
    * Instação de bibliotecas com o arquvio requirements.txt
    * Comando para pip env: pip install -r requirements.txt    
* Python >= 3.11v
```
* Node
```
Node >= 18.16v
```

## ⚙️ Executando arquivos Python

Cada arquivo deve ser executado de forma independente da seguinte forma:

```
python [nome do arquivo].py

Ex: python 1259_Pares_e_Impares.py
```

Para execução de scripts SQL foi utlizado o [DuckDB](https://duckdb.org/docs/stable/)

```
import duckdb

table = duckdb.read_csv('table.csv')

query = """

SELECT *
FROM table

"""

duckdb.sql(query).show()

```

## ⚙️ Executando arquivos Node

Cada arquivo deve ser executado de forma independente da seguinte forma:

```
cd [nome da pasta]
node index.js

Ex: 
cd exercise\node_2061_As_Abas_de_Pericles
node index.js
```

### ⌨️ Testes

Cada exercício foi validado e testado pela própria plataforma da [beecrowd](https://www.beecrowd.com.br/judge/en/login), com exito de 100% de sucesso na resolução de cada exercício.

<img src="https://github.com/LucasSouzaG/exercise-beecrowd/assets/66741091/a3cbc49d-351d-44f9-8dcf-738b4f30fb2e">

## 🛠️ Construído com

* [Python](https://www.python.org) - Linguagem de programação
* [Node](https://nodejs.org/pt-br) - Linguagem de programação
* [DuckDB](https://duckdb.org) - Simulação de Banco de dados
* [Visual studio code](https://code.visualstudio.com) - Editor de código
* Windows 11 Home - Sistema Operacional
'''A diretoria da empresa pediu para você um relatório simples de quantas cidades a empresa já alcançou.

Para fazer isso você deve exibir a quantidade de cidades distintas da tabela clientes.'''

import duckdb

customers = duckdb.read_csv('customers.csv')

query = """

SELECT COUNT(DISTINCT p.city)
FROM customers p


"""

duckdb.sql(query).show()
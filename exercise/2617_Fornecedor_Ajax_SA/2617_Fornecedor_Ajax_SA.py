'''
O setor financeiro encontrou alguns problemas na entrega de um dos nossos fornecedores, a entrega dos produtos não condiz com a nota fiscal.

Seu trabalho é exibir o nome dos produtos e o nome do fornecedor, para os produtos fornecidos pelo fornecedor ‘Ajax SA’.
'''

import duckdb

providers = duckdb.read_csv('providers.csv')
products = duckdb.read_csv('products.csv')

query = """

SELECT prod.name, p.name
FROM providers p
JOIN products prod ON p.id = prod.id_providers
WHERE p.name = 'Ajax SA'

"""

duckdb.sql(query).show()

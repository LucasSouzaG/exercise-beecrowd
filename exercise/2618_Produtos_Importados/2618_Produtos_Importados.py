'''
O setor de importação da nossa empresa precisa de um relatório sobre a importação de produtos do nosso fornecedor Sansul.

Sua tarefa é exibir o nome dos produtos, o nome do fornecedor e o nome da categoria, para os produtos fornecidos pelo fornecedor ‘Sansul SA’ e cujo nome da categoria seja 'Imported'.
'''

import duckdb

providers = duckdb.read_csv('providers.csv')
products = duckdb.read_csv('products.csv')
categories = duckdb.read_csv('categories.csv')

query = """

SELECT prod.name, p.name, c.name
FROM providers p
JOIN products prod ON p.id = prod.id_providers
JOIN categories c ON prod.id_categories = c.id
WHERE p.name = 'Sansul SA' and c.name = 'Imported'

"""

duckdb.sql(query).show()

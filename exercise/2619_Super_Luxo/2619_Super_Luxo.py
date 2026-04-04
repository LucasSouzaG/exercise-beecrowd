'''
A nossa empresa está querendo fazer um novo contrato para o fornecimento de novos produtos superluxuosos, e para isso precisamos de alguns dados dos nossos produtos.

Seu trabalho é exibir o nome dos produtos, nome dos fornecedores e o preço, para os produtos cujo preço seja maior que 1000 e sua categoria seja Super Luxury.
'''

import duckdb

providers = duckdb.read_csv('providers.csv')
products = duckdb.read_csv('products.csv')
categories = duckdb.read_csv('categories.csv')

query = """

SELECT prod.name, p.name, prod.price
FROM providers p
JOIN products prod ON p.id = prod.id_providers
JOIN categories c ON prod.id_categories = c.id
WHERE prod.price > 1000 and c.name = 'Super Luxury'

"""

duckdb.sql(query).show()

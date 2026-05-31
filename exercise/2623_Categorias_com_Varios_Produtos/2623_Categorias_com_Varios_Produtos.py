'''
O setor de vendas precisa de um relatório para saber quais produtos estão sobrando em estoque.

Para você ajudar o setor de vendas, exiba o nome do produto e o nome da categoria, para os produtos cuja quantidade seja maior que 100 e o código da categoria seja 1,2,3,6 ou 9. Mostre essas informações em ordem crescente pelo código da categoria.
'''

import duckdb

products = duckdb.read_csv('products.csv')
categories = duckdb.read_csv('categories.csv')

query = """

SELECT p.name, c.name as categorie_name
FROM products p
JOIN categories c on c.id = p.id_categories
WHERE p.amount > 100 AND p.id_categories IN (1,2,3,6,9)
ORDER BY p.id_categories ASC

"""

duckdb.sql(query).show()
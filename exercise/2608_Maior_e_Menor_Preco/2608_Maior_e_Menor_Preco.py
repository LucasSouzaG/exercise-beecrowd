'''
O setor financeiro da nossa empresa, está querendo saber os menores e maiores valores dos produtos, que vendemos.

Para isso exiba somente o maior e o menor preço da tabela produtos.
'''
import duckdb

products = duckdb.read_csv('products.csv')

query = """

SELECT max(price), min(price)
FROM products

"""

duckdb.sql(query).show()
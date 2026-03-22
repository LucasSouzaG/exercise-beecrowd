'''
Como de costume o setor de vendas está fazendo uma análise de quantos produtos temos em estoque, e você poderá ajudar eles.

Então seu trabalho será exibir o nome e a quantidade de produtos de cada uma categoria.
'''
import duckdb

products = duckdb.read_csv('products.csv')
categories = duckdb.read_csv('categories.csv')

query = """

SELECT c.name, sum(p.amount)
FROM products p
JOIN categories c on p.id_categories = c.id
GROUP BY c.name


"""

duckdb.sql(query).show()
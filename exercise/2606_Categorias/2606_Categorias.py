'''
Quando os dados foram migrados de Banco de Dados, houve um pequeno mal-entendido por parte do antigo DBA.

Seu chefe precisa que você exiba o código e o nome dos produtos, cuja categoria inicie com 'super'.
'''
import duckdb

products = duckdb.read_csv('products.csv')
categories = duckdb.read_csv('categories.csv')

query = """

SELECT p.id, p.name
FROM products p
INNER JOIN categories  c on p.id_categories = c.id
WHERE c.name LIKE 'super%'

"""

duckdb.sql(query).show()


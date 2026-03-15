'''
O setor financeiro precisa de um relatório sobre os fornecedores dos produtos que vendemos. Os relatórios contemplam todas as categorias, mas por algum motivo, os fornecedores dos produtos cuja categoria é a executiva, não estão no relatório.

Seu trabalho é retornar os nomes dos produtos e dos fornecedores cujo código da categoria é 6.
'''
import duckdb

products = duckdb.read_csv('products.csv')
categories = duckdb.read_csv('categories.csv')
providers = duckdb.read_csv('providers.csv')

query = """

SELECT p.name, pr.name 
FROM products p 
INNER JOIN providers pr on p.id_providers = pr.id 
where p.id_categories = 6

"""

duckdb.sql(query).show()


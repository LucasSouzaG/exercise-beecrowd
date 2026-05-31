'''
Na hora de entregar o relatório de quantos produtos a empresa tem em estoque, uma parte do relatório ficou corrompida, por isso o responsável do estoque lhe pediu uma ajuda, ele quer que você exiba os seguintes dados para ele.

Exiba o nome dos produtos cujas quantidades estejam entre 10 e 20 e cujo nome do fornecedor inicie com a letra ‘P’.
'''
import duckdb

products = duckdb.read_csv('products.csv')
providers = duckdb.read_csv('providers.csv')

query = """

SELECT p.name
FROM products p
JOIN providers pro on pro.id = p.id_providers
WHERE (p.amount BETWEEN 10 and 20) 
AND lower(LEFT(pro.name, 1)) = 'p'



"""

duckdb.sql(query).show()

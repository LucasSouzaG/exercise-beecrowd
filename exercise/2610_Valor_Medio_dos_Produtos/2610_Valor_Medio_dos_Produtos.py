'''
Na empresa que você trabalha está sendo feito um levantamento sobre os valores dos produtos que são comercializados.

Para ajudar o setor que está fazendo esse levantamento você deve calcular e exibir o valor médio do preço dos produtos.

OBS: Mostrar o valor com dois números após o ponto.
'''
import duckdb

products = duckdb.read_csv('products.csv')


# TRUNC / TRUNCATE = corta sem arredondar
query = """

SELECT TRUNC(AVG(p.price), 2)
FROM products p


"""

duckdb.sql(query).show()
'''A locadora tem objetivos de criar várias franquias espalhadas pelo Brasil. Para isso queremos saber em quais cidades nossos clientes moram.

Para você nos ajudar selecione o nome de todas as cidades onde a locadora tem clientes. Mas por favor, não repita o nome da cidade.'''

import duckdb

customers = duckdb.read_csv('customers.csv')

query = """

SELECT c.city
FROM customers c
GROUP BY c.city

"""

duckdb.sql(query).show()

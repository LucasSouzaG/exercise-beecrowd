'''
A locadora pretende fazer uma promoção para os clientes que ainda não fizeram nenhuma locação.

Seu trabalho é nos entregar o ID e o nome dos clientes que não realizaram nenhuma locação. Ordene a saída por ID.
'''

import duckdb

customers = duckdb.read_csv('customers.csv')
locations = duckdb.read_csv('locations.csv')

query = """

SELECT c.id, c.name
FROM customers c
LEFT JOIN locations l ON c.id = l.id_customers
WHERE l.id_customers is null

"""

duckdb.sql(query).show()

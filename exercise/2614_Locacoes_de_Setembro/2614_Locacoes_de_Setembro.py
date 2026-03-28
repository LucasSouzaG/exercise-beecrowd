'''A vídeo locadora está fazendo seu relatório semestral e precisa da sua ajuda. Basta você selecionar o nome dos clientes e a data de locação, das locações realizadas no mês de setembro de 2016.'''

import duckdb

customers = duckdb.read_csv('customers.csv')
rentals = duckdb.read_csv('rentals.csv')

query = """

SELECT c.name, r.rentals_date
FROM customers c
JOIN rentals r on c.id = r.id_customers
WHERE EXTRACT(MONTH FROM r.rentals_date) = 9

"""

duckdb.sql(query).show()

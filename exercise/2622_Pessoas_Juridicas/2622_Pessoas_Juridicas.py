'''
O setor de vendas quer fazer uma promoção para todos os clientes que são pessoas jurídicas. Para isso você deve exibir o nome dos clientes que sejam pessoa jurídica.

'''
import duckdb

customers = duckdb.read_csv('customers.csv')
legal_person = duckdb.read_csv('legal_person.csv')

query = """

SELECT c.name
FROM legal_person l
LEFT JOIN customers c on l.id_customers = c.id


"""

duckdb.sql(query).show()

'''
A auditoria financeira da empresa está pedindo para nós um relatório do primeiro semestre de 2016. Então exiba o nome dos clientes e o número do pedido para os clientes que fizeram pedidos no primeiro semestre de 2016.

'''
import duckdb

customers = duckdb.read_csv('customers.csv')
orders = duckdb.read_csv('orders.csv')

query = """

SELECT c.name, o.id
FROM customers c
JOIN orders o on o.id_customers = c.id
WHERE CAST(o.orders_date AS DATE) <= '2016-06-30'
ORDER BY o.id asc

"""

duckdb.sql(query).show()

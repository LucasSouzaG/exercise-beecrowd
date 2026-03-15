import duckdb

product = duckdb.read_csv('products.csv')
providers = duckdb.read_csv('provider.csv')
categories = duckdb.read_csv('categories.csv')


query = """

SELECT p.name, pr.name 
FROM product as p
INNER JOIN providers pr on p.id_providers = pr.id
where p.id_categories = 6;
ORDER BY p.name desc


"""

duckdb.sql(query).show()




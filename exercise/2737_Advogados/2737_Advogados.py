'''
O diretor da Mangojata Advogados ordenou que lhe fosse entregue um relatório sobre seus advogados atuais.

O diretor quer que você mostre para ele o nome do advogado que têm mais clientes, o nome do advogado que tem menos clientes e a média de clientes entre todos os advogados.

OBS: Antes de apresentar a média mostre um campo chamado Average a fim de deixar o relatório mais apresentável. A média deverá ser apresentada em inteiros.
'''
import duckdb

lawyers = duckdb.read_csv('lawyers.csv')

query = """

(
    SELECT 
        name,
        customers_number 
    FROM lawyers 
    ORDER BY customers_number DESC 
    LIMIT 1
)

UNION ALL

(
    SELECT 
        name,
        customers_number 
    FROM lawyers 
    ORDER BY customers_number ASC 
    LIMIT 1
)

UNION ALL

(
    SELECT
        'Average',
        CAST(AVG(customers_number) as INT)
    FROM lawyers
)


"""

duckdb.sql(query).show()
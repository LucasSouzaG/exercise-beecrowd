'''
Todos os meses a empresa pede um relatório das cidades que os fornecedores estão cadastrados. Dessa vez não vai ser diferente, faça uma consulta no Banco de Dados que retorne todas as cidades dos fornecedores, mas em ordem alfabética.

OBS: Você não deve mostrar cidades repetidas.
'''
import duckdb

providers = duckdb.read_csv('providers.csv')

query = """

SELECT distinct city
FROM providers
ORDER BY city asc

"""

duckdb.sql(query).show()
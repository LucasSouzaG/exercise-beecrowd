'''
Os diretores do setor de comunicação da sua empresa querem um relatório sobre os dados dos clientes físicos que estão cadastrados no banco de dados. Porem o antigo relatório teve um problema. Os dados do CPF dos clientes vieram sem a máscara.

Por isso seu trabalho agora é selecionar todos os CPFs de todos os clientes, e aplicar uma máscara sobre o retorno dos dados.

A máscara do CPF é parecida com: '000.000.000-00'.
'''
import duckdb

customers = duckdb.read_csv('customers.csv')
natural_person = duckdb.read_csv('natural_person.csv')

query = """

SELECT 
    CONCAT(
        SUBSTRING(cast(np.cpf as varchar), 1, 3),
        '.',
        SUBSTRING(cast(np.cpf as varchar), 4, 3),
        '.',
        SUBSTRING(cast(np.cpf as varchar), 7, 3),
        '-',
        SUBSTRING(cast(np.cpf as varchar), 10, 2)
    ) as cpf_primeira_parte
FROM customers c
JOIN natural_person np on np.id_customers = c.id


"""

duckdb.sql(query).show()
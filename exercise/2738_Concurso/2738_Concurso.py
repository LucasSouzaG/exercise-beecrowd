'''
A Universidade Tecnológica de Marte está com seu concurso aberto para Pesquisadores. Porém o computador que processava os dados dos candidatos estragou. Você deve mostrar a lista dos candidatos, contendo o nome do candidato e a sua pontuação final (com duas casas decimais após a vírgula). Lembre-se de mostrar a lista ordenada pela pontuação do candidato (maior pontuação no topo da lista).

A pontuação do candidato é o resultado da média ponderada descrita abaixo:



'''
import duckdb

candidate = duckdb.read_csv('candidate.csv')
score = duckdb.read_csv('score.csv')

query = """

SELECT 
    c.name,
    CAST(
        AVG(
                (CAST(s.math*2 as NUMERIC) + CAST(s.specific*3 as NUMERIC) + CAST(s.project_plan*5 as NUMERIC)
            ) / 10
        ) AS NUMERIC(18,2)
    ) avg
FROM candidate c
JOIN score s on s.candidate_id = c.id
GROUP BY c.name
ORDER BY avg DESC
"""

duckdb.sql(query).show()
'''
Na empresa que você trabalha está sendo feito um levantamento sobre os valores dos produtos que são comercializados.

Uma Vídeo locadora contratou seus serviços para catalogar os filmes dela. Eles precisam que você selecione o código e o nome dos filmes cuja descrição do gênero seja 'Action'.
'''
import duckdb

movies = duckdb.read_csv('movies.csv')
genres = duckdb.read_csv('genres.csv')

query = """

SELECT m.id, m.name
FROM movies m
JOIN genres g on m.id_genres = g.id
WHERE g.description = 'Action'

"""

duckdb.sql(query).show()
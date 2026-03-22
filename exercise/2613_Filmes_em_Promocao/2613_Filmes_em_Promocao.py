'''
Antigamente a locadora fez um evento em que vários filmes estavam em promoção, queremos saber que filmes eram esses.

Seu trabalho para nós ajudar é selecionar o ID e o nome dos filmes cujo preço for menor que 2.00.
'''
import duckdb

movies = duckdb.read_csv('movies.csv')
prices = duckdb.read_csv('prices.csv')

query = """

SELECT m.id, m.name
FROM movies m
JOIN prices p on m.id_prices = p.id
WHERE p.value < 2.00

"""

duckdb.sql(query).show()
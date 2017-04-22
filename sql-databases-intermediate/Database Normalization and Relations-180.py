## 4. Querying a normalized database ##

qry = "select c.year, n.movie from ceremonies c join nominations n on c.id = n.ceremony_id where n.nominee = 'Natalie Portman';"
portman_movies = conn.execute(qry).fetchall()
print(portman_movies)

## 6. Join table ##

qry1 = "select * from movies_actors limit 5"
five_join_table = conn.execute(qry1).fetchall()

qry2 = "select * from actors limit 5;"
five_actors = conn.execute(qry2).fetchall()

qry3 = "select * from movies limit 5;"
five_movies = conn.execute(qry3).fetchall()

print(five_join_table)
print(five_actors)
print(five_movies)

## 7. Querying a many-to-many relation ##

qry = "SELECT actors.actor, movies.movie FROM movies INNER JOIN movies_actors ON movies.id == movies_actors.movie_id INNER JOIN actors ON movies_actors.actor_id == actors.id WHERE movies.movie == 'The King''s Speech';"
kings_actors = conn.execute(qry).fetchall()
print(kings_actors)

## 8. Practice: querying a many-to-many relation ##

qry = "select m.movie, a.actor from movies m inner join movies_actors ma on ma.movie_id = m.id inner join actors a on a.id = ma.actor_id where a.actor = 'Natalie Portman';"
portman_joins = conn.execute(qry).fetchall()
print(portman_joins)
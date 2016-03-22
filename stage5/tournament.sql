-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players
    ( id SERIAL,
      name TEXT );


CREATE TABLE matches
    ( winner SMALLINT,
      loser SMALLINT );


CREATE VIEW player_standings AS
    SELECT players.id,
             players.name,
             CASE WHEN wins_table.wins IS NULL THEN 0
                  ELSE wins_table.wins
                  END,
            CASE WHEN match_count.matches IS NULL THEN 0
                  ELSE match_count.matches
                  END
        FROM players LEFT JOIN
            (SELECT winner, count(winner) AS wins
                FROM matches
                GROUP BY winner) AS wins_table
        ON players.id = wins_table.winner
        LEFT JOIN
            (SELECT check_in.id, count(*) AS matches
                FROM (
                    (SELECT winner AS id
                        FROM matches)
                    UNION
                    (SELECT loser AS id
                        FROM matches)
                    ) AS check_in
                GROUP BY check_in.id) AS match_count
        ON players.id = match_count.id
        ORDER BY wins DESC;


CREATE VIEW numbered_standings AS
    SELECT *, row_number() OVER(ORDER BY wins DESC) AS row
        FROM player_standings;


CREATE VIEW odd_standings AS
    SELECT *
        FROM numbered_standings
        WHERE row % 2 = 1;


CREATE VIEW even_standings AS
    SELECT *
        FROM numbered_standings
        WHERE row % 2 = 0;

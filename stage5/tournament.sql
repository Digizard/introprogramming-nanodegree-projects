-- Table definitions for the tournament project.


CREATE TABLE players (
-- Table of all players
--
-- Columns:
--    id: Unique identifier for each player.
--    name: Name associated with player.
    id SERIAL PRIMARY KEY,
    name TEXT
);


CREATE TABLE matches (
-- Table of all matches
--
-- Columns:
--     winner: ID of winning player.
--     loser: ID of losing player.
    winner SMALLINT REFERENCES players (id),
    loser SMALLINT REFERENCES players (id)
);


CREATE VIEW player_standings AS
-- Combination of player data.
--
-- Columns:
--     id: Unique identifier for each player.
--     name: Name associated with player.
--     wins: Number of match victories for player.
--     matches: Number of matches the player has participated in.
    SELECT players.id,
           players.name,
           CASE WHEN wins_table.wins IS NULL THEN 0
                ELSE wins_table.wins
                END,
           CASE WHEN match_count.matches IS NULL THEN 0
                ELSE match_count.matches
                END
        FROM players
             LEFT JOIN
             (SELECT winner, count(winner) AS wins
                FROM matches
                GROUP BY winner
             ) AS wins_table
             -- Each winner's number of wins.
             --
             -- Columns:
             --     winner: Unique identifier for each winning player.
             --     wins: Number of match victories for player.
             ON players.id = wins_table.winner
             LEFT JOIN
                (SELECT check_in.id, count(*) AS matches
                    FROM (
                        (SELECT winner AS id
                            FROM matches
                        )
                        UNION
                        (SELECT loser AS id
                            FROM matches
                        )
                    ) AS check_in
                    -- All participants of every match. Names are repeated if
                    -- player participates in multiple matches.
                    --
                    -- Columns:
                    --     id: Unique identifier for each player.
                    --     matches: Setup for counting matches.
                    GROUP BY check_in.id
                ) AS match_count
                -- Total number of matches for players who have participated in
                -- at least one.
                --
                -- Columns:
                --     id: Unique identifier for each player.
                --     matches: Number of matches the player has participated
                --              in.
            ON players.id = match_count.id
        ORDER BY wins DESC;


CREATE VIEW numbered_standings AS
-- Numbers each row in the player standings.
--
-- Columns:
--     id: Unique identifier for each player.
--     name: Name associated with player.
--     wins: Number of match victories for player.
--     matches: Number of matches the player has participated in.
--     row: Counting value for row number.
    SELECT *, row_number() OVER(ORDER BY wins DESC) AS row
        FROM player_standings;


CREATE VIEW odd_standings AS
-- Odd-numbered rows in player standings.
--
-- Columns:
--     id: Unique identifier for each player.
--     name: Name associated with player.
--     wins: Number of match victories for player.
--     matches: Number of matches the player has participated in.
--     row: Counting value for row number. All odd numbers.
    SELECT *
        FROM numbered_standings
        WHERE row % 2 = 1;


CREATE VIEW even_standings AS
-- Even-numbered rows in player standings.
--
-- Columns:
--     id: Unique identifier for each player.
--     name: Name associated with player.
--     wins: Number of match victories for player.
--     matches: Number of matches the player has participated in.
--     row: Counting value for row number. All even numbers.
    SELECT *
        FROM numbered_standings
        WHERE row % 2 = 0;


CREATE VIEW swiss_pairings AS
-- Pairs of players.
--
-- Columns:
--     id1: ID of the first player.
--     name1: Name of the first player.
--     id2: ID of the second player.
--     name2: Name of the second player.
    SELECT odd_standings.id AS id1,
           odd_standings.name AS name1,
           even_standings.id AS id2,
           even_standings.name AS name2
        FROM odd_standings, even_standings
        WHERE odd_standings.row = even_standings.row - 1;

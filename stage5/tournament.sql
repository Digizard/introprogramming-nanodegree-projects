-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players ( id SERIAL,
					   name TEXT );


CREATE TABLE pairings ( round INT,
                        first_id INT,
                        second_id INT );

CREATE TABLE outcomes ( round INT,
						winner_id INT,
						loser_id INT );
#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    cursor = DB.cursor()

    cursor.execute("DELETE FROM matches;")

    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    cursor = DB.cursor()

    cursor.execute("DELETE FROM players;")

    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    cursor = DB.cursor()

    cursor.execute("SELECT count(*) FROM players;")
    num_players = cursor.fetchone()[0]

    DB.close()

    return num_players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    cursor = DB.cursor()

    cursor.execute("INSERT INTO players (name) VALUES (%s);", (name, ))

    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    cursor = DB.cursor()

    cursor.execute("""
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
                            FROM matches)) AS check_in
                    GROUP BY check_in.id) AS match_count
            ON players.id = match_count.id
            ORDER BY wins DESC;
        """)

    standings = cursor.fetchall()

    DB.close()

    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """



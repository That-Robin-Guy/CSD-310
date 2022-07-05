
from ntpath import join
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password" : "Berta1219!",
    "host" : "127.0.0.1",
    "database" : "pysports",
    "raise_on_warnings" : True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    print("\n \n")
    print("-- Displaying Player Records --\n")

    cursor = db.cursor()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
    player = cursor.fetchall()
    
    for players in player:
        print("Player ID: {} \nFirst Name: {} \nLast Name: {}\nTeam Name: {}\n".format(players[0], players[1], players[2], players[3]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist.")

    else:
        print(err)

finally:
    db.close()
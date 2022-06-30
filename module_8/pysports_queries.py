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

    print("\n Database user {} connected to MySQL on host {} with database {}!".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    team = cursor.fetchall()

    print("\n -- Displaying Team Records -- \n")

    for team_members in team:
        print("Team ID: {} \nTeam Name: {} \nMascot: {} \n".format(team_members[0], team_members[1], team_members[2] ))

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    player = cursor.fetchall()

    print("\n -- Displaying Player Records -- \n")

    for players in player:
        print("Player ID: {} \nFirst Name: {} \nLast Name: {}\nTeam ID: {}\n".format(players[0], players[1], players[2], players[3]))

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



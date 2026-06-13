import sqlite3

conn = sqlite3.connect("../worldcup.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT matches.match_date, home.name, away.name, matches.status
    FROM matches
    JOIN teams AS home ON matches.home_team_id = home.id
    JOIN teams AS away ON matches.away_team_id = away.id
    LIMIT 5
""")

print("\n--- FIRST WC MATCHES ---\n")
for row in cursor.fetchall():
    data, home, away, status = row
    print(f"{data} | {home} x {away} | Status: {status}")

conn.close()
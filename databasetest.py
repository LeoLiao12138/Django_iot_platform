import sqlite3


conn = sqlite3.connect('./db.sqlite3')
cur = conn.cursor()
message = "INSERT INTO app_iot_platform_mqtt_message VALUES(NULL,'/ICE/port/2/pdi', '1234','1234')"
cur.execute(message)
conn.commit()
cur.close()
conn.close()
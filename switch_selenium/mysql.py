import pymysql

conn = pymysql.connect(
    user = "jeongwle",
    passwd = "1q2w3E4R!",
    host = "localhost",
    db = "NINTENDO"
)
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS switchtitle")
cursor.execute("CREATE TABLE switchtitle (number int, title text, price text, date text, 'review' text)")
idx = 0
i = 1
for j in range(total):
    cursor.execute(
        f'INSERT INTO switchtitle VALUES({i}, \"{results[idx][0]}\", \"{results[idx][1]}\", \"{results[idx][2]}\", \"{results[idx][3]}\")'
    )
    i += 1
    idx += 1
conn.commit()
conn.close()
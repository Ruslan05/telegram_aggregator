import pymysql


def get_db_connection():
    conn = pymysql.connect(
        db='aggregator',
        user='root',
        passwd='1',
        host='localhost')

    return conn.cursor(pymysql.cursors.DictCursor)


# c = get_db_connection()
# # Print the contents of the database.
# c.execute("SELECT * FROM public ")
# l = c.fetchall()
# print(l)

# c.execute("SELECT * FROM post_exucuted where id_channel = 1 AND id_public = 2 AND post_date >= 'post_date value'")
#
# c.execute("SELECT * FROM public_channel WHERE id_public = 1")
#
# c.execute("SELECT * FROM public_data WHERE id_public = 1")
#
# c.execute("SELECT * FROM channel")
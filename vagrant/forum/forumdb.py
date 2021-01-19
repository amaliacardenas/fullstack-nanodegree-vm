# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database = DBNAME)
  cursor = db.cursor()
  cursor.execute('select content, time from posts order by time desc;')
  return cursor.fetchall()
  db.close()

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database = DBNAME)
  cursor = db.cursor()
  cursor.execute("insert into posts values (%s)", (bleach.clean(content),))
  cursor.execute("update posts set content = 'cheese' where content like '%spam%'")
  db.commit()
  db.close()

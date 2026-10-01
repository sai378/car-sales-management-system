import os
from dotenv import load_dotenv
import MySQLdb

load_dotenv()

class DatabaseConnection:

    def __init__(self):
        self.host = "localhost"
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = "car_sales_db"

    def connect(self):

        try:
            con = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.database
            )

            return con

        except MySQLdb.Error as e:
            print("Database connection failed:", e)
            return None


if __name__ == "__main__":

    db = DatabaseConnection()

    con = db.connect()

    if con:
        print("Database connected successfully!")
        con.close()
import csv
from cs50 import SQL
from flask import Flask

db = SQL("sqlite:///busigence.db")

def main():
    db.execute("CREATE TABLE customers ('customerid' varchar(255),'companyname' varchar(255),'contactname' varchar(255),'contacttitle' varchar(255))")

if __name__ == "__main__":
    main()

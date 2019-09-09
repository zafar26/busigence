import csv
from cs50 import SQL
from flask import Flask

db = SQL("sqlite:///busigence.db")

def main():
    db.execute("DELETE FROM orders WHERE customerid='CustomerID'")

    
if __name__ == "__main__":
    main()

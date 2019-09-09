import csv
from cs50 import SQL
from flask import Flask

db = SQL("sqlite:///busigence.db")

def main():
    f = open("customers.csv")
    reader = csv.reader(f)
    for customerid, companyname, contactname, contacttitle in reader:
        db.execute("INSERT INTO customers (customerid, companyname, contactname, contacttitle) VALUES (:customerid, :companyname, :contactname, :contacttitle)",{'customerid': customerid, 'companyname': companyname,'contactname': contactname,'contacttitle': contacttitle})
        print(f"Added {customerid} , {companyname} , {contactname}")

if __name__ == "__main__":
    main()

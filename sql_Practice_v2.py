#Author: Lawrence Morris   November 2025  Released to public domain under MIT license

#version without dependencies

import sqlite3

# sql command input

def sqlCommandLine (con, cur):
    query = input("Enter your SQL query here: " )
    if query == 'exit':
        return query
    else:
        try:
            result=cur.execute(query)
            print (" ")
            for row in result:
                print("  ".join(str(x) for x in row))

        except:
            print("That command is not recognized.")
            print ('To see the database, type: SELECT * FROM inventory')
        return 'y'


def main ():

    # create database

    con = sqlite3.connect("bookstore.db")
    cur = con.cursor()

    # populate database


    try:
        cur.execute ("CREATE TABLE inventory (id INTEGER PRIMARY KEY, Title TEXT, Last_Name TEXT, In_Stock INTEGER, Cost REAL)")
    except:
        pass


    #these are the intial records
    a = "(1, 'Narnia and the Wardrobe', 'Lewis', 20, 2.50)"
    b = "(2, 'Frankenstein''s Mirror', 'Franks', 3, 3.25)"
    c = "(3, 'The Best of Michelangelo', 'Bonaventure', 55, 4.00)"
    d = "(4, 'Italian Made Even Easier', 'Smith', 7, 3.69)"
    e = "(5, 'Custer and Custard', 'Jones', 4, 10.00)"
    f = "(6, 'How to Tame a Toad', 'Jackson', 1, 25.99)"
    g = "(7, 'The Road More Traveled By', 'Pietro', 0, 5.25)"

    records = [a, b, c, d, e, f, g]


    try:
        for each in records:
            cur.execute ("INSERT INTO inventory VALUES  " + each)
    except:
        pass


    # Introduction
    print("WELCOME TO THE BOOKSTORE DATABASE! \n The database table is called 'inventory'")
    print ("The fields are called 'id', 'Title', 'Last_Name', 'In_Stock', and 'Cost'")
    print ("Type 'exit' at any time to quit.")
    print ()

    #set up sql loop

    keepGoing = 'y'
    while keepGoing != "exit":
        keepGoing = sqlCommandLine(con, cur)
        print ()

    # save prompt
    saveRequest = input ('Do you want to save your changes? Type y or n : ')
    if saveRequest == 'y':
        con.commit()



    # good bye
    con.close()
    print ('')
    print ("Thanks for using the bookstore database!")
    print ("Hit 'Enter' to close your window.")
    input()


main()


#Author: Lawrence Morris   October 2025  Released to public domain when appropriate

#version without dependencies

import pandas as pd
import duckdb

# sql command input

def sqlCommandLine (someDataFrame):
    query = input("Enter your SQL query here: " )
    if query == 'n':
        return query
    else:
        try:
            result=duckdb.sql(query).df()
            print ("Your results:")
            print (result)
        except:
            print("That command is not recognized.")
        return 'y'


#main program below


#Set up sample database

inventory = pd.DataFrame({"ID": [1, 2, 3, 4, 5, 6, 7], "Title": ["Narnia and the Wardrobe", "Frankenstein's Mirror", "The Best of Michelangelo", "Italian Made Even Easier", "Custer and Custard", "How to Tame a Toad", "The Road More Traveled By"], "Last_Name": ['Lewis', 'Franks', 'Bonaventure', 'Smith', 'Jones', 'Jackson', "Pietro"], "In_Stock": [20, 3, 55, 7, 4, 1, 0], "Cost": [2.50, 3.25, 4.00, 3.69, 10.00, 25.99, 5.25] })


# Introduction
print("WELCOME TO THE BOOKSTORE DATABASE! \n The database table is called 'inventory'")
print ("The fields are called 'ID', 'Title', 'Last_Name', 'In_Stock', and 'Cost'")
print ("Type n at any time to quit.")
print ()

#set up sql loop

keepGoing = 'y'
while keepGoing != "n":
    keepGoing = sqlCommandLine(inventory)
    print ()


# good bye
print ("Thanks for using the bookstore database!")
print ("You can now close your window.")
input()





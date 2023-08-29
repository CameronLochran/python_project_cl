
Spending Tracker

Build an app that allows a user to track their spending.

MVP

The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail (for Wee Cameron its DistroKid, Amazon)
The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.
Inspired by:

Monzo, MoneyDashboard, lots of mobile/online banking apps

Possible Extensions

The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction.
Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.


GIT
1 git add .  / gaa
2 git commit -m "message"
3 git push

TODO
BACKEND
1 run_sql file
2 createbd <dbname>
3 create tables - sql file  (PLANNING)
4 psql -d <dbname> -f db/<sqlfile>
5 Classes
6 Respoitories 
7 console.py - creqte objects and store them in the database and print them out  (you will need repositories and classes) 
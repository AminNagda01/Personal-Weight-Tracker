# Plan 1: Due 9/7 - Implement the Ingredients database, and a command line interface to get the information  
So testing, data validation, database, documentation should all be done 


## TODO: 
# Add "b" command everywhere except the r and d input so that use can go back a menu 
# Add API calls for the ingredients option 

### High Level Desired Features: 
a) input food in 5 categories: Breakfast, Lunch, Dinner, Drinks, Intermediate (Snaks or small meals) 
b) Input an ingredient or food with calories. 
	I should be able to look up past dishes and ingredients for faster input 
c) Be able to place food for current day and past X days, after that unable to edit. Also, be able to pull up previous days
	Any days that had no input are given a 0 when pulled up 
d) Set goals that are assignable per day of a week. Each sunday, set calorie goals for week till next sunday
	If u forget to open adn set goal on sunday, you should be able to set it for any x amount of days till the next 
	sunday. if you skip a week, forget it and move on. 
	It should notify how many calories are left if im inputting 
e) Be able to download a report for any X amount of pass days, where we can see what days i went over 
f) email the results or email if too many days go by without input 

### Some requirements: 
The user shall be able to select type of meal (breakfast, dinner, etc)
The user shall be able to add ingredients to a database, with a caloric number added to it
The user should be able to use food in the database to add to the selected meal type. 
The user shall be able to place food entries 
	It should be for 7 days before and including the current day 
The user shall be able to see the history of their eating
	 based on day 
The user shall be able to download a report of the past 
	for X days history 
Program can be hosted at all times through a server and docker
Program input of info is done through command line interface 

### Constraints: 
Flask, Python, SQL or Postgresql, Docker and Docker Compose
	Why?
		Flask and Python to better learn them. Sql to store the data, and docker to run it anywhere. Essentailly
		I am following the teclado stuff again but for a more thorough backend project 
Python will make the app, flask will handle requests. We can use marshmallow and open ai for validation and schemas, then 
have blueprints to manage it. Docker will allow us to run it on any server of our choosing. Postgresql will store two tables, 
one by day for eating history, and another for the food and calories per food 

### API Design: 

Ingredients/Foods: POST will make new ingredient or food with calories and serving size. PUT will update that ingredient
DELETE will remove it. GET will return the ingredient. GET will also get ALL ingredients

DAYS: POST will add given ingredients to day. PUT will update that day w new foods. GET will get that day's food and calories. GET will also get a date range 
DELETE will remove the ingredint's' passed as arguments for the date given 
Every year, the program will add another year of spaces to the storage for days

Only accept strings for names of food, ints for date, and ints for serving size (with a string for the unit of mesurement) 
Only return a string or int for what is requested 

### Testing: - Maybe use Cypress? Find a automatic testing tool 
User starts program and can choose to do one of the many api requests 
Foods: 
	POST - User should only be able to enter a string name, int calorie amount, int serving size, and string unit 
	       Ignored if values are below 0, ingredient already exists with same unit type, 
	PUT - Update the calorie int amount, serving size. Name should be unchanged. Ignored if no match or invalid arguments included 
	DELETE - Needs ingredient name to delete. ignored if no match 
	GET - Only for the get single ingredient do we ignore if no match. Otherwise no bad test cases 
Days:
	POST - 

### Database design:
The days should be the "main" database. They will be the primary key, with ingredients/food (many) being foreign keys. One-to-many relationship, as
one day can have many ingredients. All the day needs for itself is the date, and the api will, on any get, calculate the calories before output
to speed it up, day 1 could be indexed at 0, and so on, so that we can make some math to call it, rather than going through and checking each date

the food db should be independent. so each item in there is independent. These will have to be searchable by name, i dont think we can search with 
ids on this one 


### Design approach: 
Using a layered design. 
Input and output libraries will be called by an intemediary file that will handle sending data to api file, and printing output 
the api file will interact with the database, and send data back to the intemediary file 
Benifits: Easier to test, scalable if needed, and easier to make flexible in case of changes since everything is so seperated 
Cons: May increase size, which is unneeded on such a small project, may be too complex for something so simple 

But i dont want direct design because it will be harder to grow if needed 

Note: most error correction should be on the app layer, once we want to request info 
for any other errs, like bad commands, those can be raised normally 




Notes as I develop: 

"""
Main has 3 reasons: 
1. allows us to test contents better 
2. only executes code in main when it is called if the py file is imported 
3. better readability and understanding of variable scopes 

So in this case, we have 2 options: 
1. Run this file without main, so that all input goes out from here and is returned to here 
2. (my choice) have no functionality in main at all. only make defs here that facilitate input. the central app, whatever that may be, will call input.py defs as needed 
"""

"""

Layered architecture: https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch01.html

"""

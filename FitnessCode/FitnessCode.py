from guizero import App, Window, PushButton, Text, TextBox, Picture, ListBox, info, ButtonGroup
#
#This is needed for the sql database
import sqlite3
from sqlite3 import Error
#Import SQL
import os
import os.path
#Import datetime
import datetime

#Define the DDL SQL to make the tables
#Tables created in database with the following details below

sql = """
CREATE TABLE "User_Table" (
	"UserID"	    INTEGER NOT NULL,
	"UserName"		TEXT,
	"UserPassword"	TEXT,
	"UserFirstName"	TEXT,
	"UserSurname"	TEXT,
	"DateofBirth"	STRING,
	"EmailAddress"	STRING,
	"Premium"		INTEGER,
	PRIMARY KEY("UserID" AUTOINCREMENT)
);

CREATE TABLE "Credit_Card_Table" (
	"ID"			 INTEGER NOT NULL,
	"CardHolderName" STRING,
	"CardExpiryDate" STRING,
	"CardCVC"		 STRING,
	"UserID"		 INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT),
	CONSTRAINT "UserID_fk"  FOREIGN KEY("UserID") REFERENCES "User_Table"("UserID")
);

CREATE TABLE "Advice_Table" (
	"AdviceID"			INTEGER NOT NULL,
	"AdviceType"		STRING,
	"AdviceDescription" STRING,
	"AdviceUpdated"		STRING,
	"Advice"			STRING,
	PRIMARY KEY("AdviceID" AUTOINCREMENT)
);

insert into User_Table (UserName, UserPassword, UserFirstName, UserSurname, DateofBirth, EmailAddress, Premium) values ('joehpr', 'SverigeS', 'Joe', 'Harper', '011103', 'joe.harper@outlook.com', '1');
insert into Credit_Card_Table (CardHolderName, CardExpiryDate, CardCVC, UserID) values ('Joe Harper', '0322', '524', 1);
insert into Advice_Table (AdviceID, AdviceType, AdviceDescription, AdviceUpdated, Advice) values ('1', 'Smoking', 'We reccomend stopping smoking', '020220', 'We reccomend e-cigs');
"""
#
#Global variables here
#
userHasLoggedIn = False						#This is a boolean, so if the user is not logged in - they cannot access any further pages
premUser = 0 #1 indicates a premium user, 0 is standrd(free content only)
UserOn = 0
database_file = 'FitnessApp.db'
#
#
#
#Delete the database, only if it exists
#
#
if os.path.exists(database_file):
	os.remove(database_file)

#Connect to the database
conn = sqlite3.connect(database_file) #My connection is called 'conn'
#Get a cursor pointing to the database
cursor = conn.cursor()
#Create the tables
cursor.executescript(sql)
#Commit to save everything
conn.commit()
#Close the connection to the database

#Queries the database using the database paramater as the database
#to query and the query parameter as the actual query to issue

def query_database(database, query):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows

#Executes the sql statement
def execute_sql(database, sql_statement):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(sql_statement)
    conn.commit()
    return cur.lastrowid

def openMainWindow():
	if userHasLoggedIn == True:
		windowMain.show()
		windowMain.warn("Wahey!", "One free month of premium")
	else:
		windowMain.hide()
#
def open_windowLogIn():
#	Open log in window
	windowL.show()
	print("Log in button clicked")
#Open log in window but log out
def open_windowLogOut():
	#Closes all the windows and goes back to log in form
	windowMain.hide()		
	windowS.hide()
	input_boxU.clear()
	input_boxP.clear()
	app.hide()
	windowL.show()
	print("Log out successful")

def DarkMode():
	app.bg = "#222224"
	windowL.bg = "#222224"
	windowS.bg = "#222224"

#Open sign up window
def open_windowSignUp():
	windowS.show()
	print("Sign up button clicked")

def open_windowMain():
	windowMain.show()
	#print("Window main button clicked")
	windowMain.warn("Wahey!", "One free month of premium")

def open_windowFitness():
	windowFitness.show()
	print("Fitness button clicked")


def open_windowHealthy():
	windowHealthy.show()
	print("Healthy button clicked")

def open_windowPremium():
	windowPremium.show()
	print("Premium button clicked")

def open_windowPlanHealthy():
	windowPlanHealthy.show()
	print("Plan button clicked")

def open_windowPlanFitness():
	windowPlanFitness.show()
	print("Plan button clicked")

def open_windowPlanWeight():
	windowPlanWeight.show()
	print("Plan button clicked")

def open_windowPlanSmoking():
	windowPlanSmoking.show()
	print("Plan button clicked")

def open_windowBank():
	windowBank.show()
	info("Work in progress", "This area under development")
	print("Bank button clicked")

#Closes windows
def close_window():
	windowL.hide()
	windowS.hide()
	windowMain.hide()
	windowFitness.hide()
	windowHealthy.hide()

def close_Premiumwindow():
	windowPremium.hide()
	windowPlanFitness.hide()
	windowPlanHealthy.hide()
	windowPlanWeight.hide()
	windowPlanSmoking.hide()

#Checks the login, is user valid?
def check_login():
	global UserOn #Who is logged in?
	global userHasLoggedIn	#Indicates whether user is logged in or not
	global premUser #Indicates if user is free or prem
	#
	username = input_boxU.value
	password = input_boxP.value             #This makes sure to see if the user has entered a username and password, if nothing entered then query this
	print(username + password)
	#
	#To mitigate SQL injection I will only select the username.
	#
	query = f"select * from User_Table where UserName = '{username}'"
	rows = query_database(database_file, query)
	print(rows)
	 

	if len(rows) == 0:          #If there are no users then there are no rows
		info("Error", "Username or password incorrect")
		userHasLoggedIn = False
	else:
		if password == rows[0][2]:
			info("Logged in", "User found and password correct")
			UserOn = rows[0]  #rows[0] shows that 0 is the first user
								#Save the user details when they log in
			premUser = rows[0][7]	#Store if user is premium
			if premUser == 0:
				buttonPremium.disable()
			else:
				buttonPremium.enable()
			userHasLoggedIn = True
			open_windowMain()
		else:
			info("Error!","That's wrong")

#Sign up function
def sign_up():
    username = input_boxUs.value
    password = input_boxPa.value
    userfirstname = input_boxFn.value
    usersurname = input_boxSn.value
    checkPassword = input_boxPasswordConfirm.value
    
    sql_query = f"SELECT COUNT(*) FROM User_Table WHERE UserName = '{username}';"
    userExists = query_database(database_file, sql_query)
    print(userExists)
    if userExists [0][0] > 0:   #If userExists[0][0] is the count of the users in the database
        print("Username already taken")     #Here, if the username is already taken there will be a message to show that the username is already taken
    else:
        sql_query = f"insert into User_Table (UserName, UserPassword, UserFirstName, UserSurname, Premium) values ('{username}', '{password}', '{userfirstname}', '{usersurname}',  '{0}');"
        if password != checkPassword:
            info("Error", "Passwords don't match")
        else:
            execute_sql(database_file, sql_query)
    if len(password) < 8:
        info("Password error", "Length of password is not 8 characters")
    else:
        info("Password accepted", "Password at acceptable length")

app = App(title="Log in or sign up with Toka Fitness")

#Sign up window
windowS = Window(app, title="Sign up", width = 1500, height = 1000)
windowS.hide()

#Log in window
windowL = Window(app, title="Log in", width = 1500, height = 600)
windowL.hide()

#Main window
windowMain = Window(app, title="Main window", width = 1500, height = 600)
windowMain.hide()

#Fitness training window
windowFitness = Window(app, title="Fitness training")
windowFitness.hide()

#Healthy living window
windowHealthy = Window(app, title="Healthy living")
windowHealthy.hide()

#Premium plan window
windowPremium = Window(app, title="Premium Plan", width = 1500, height = 700)
windowPremium.hide()

#Plan healthy page
windowPlanHealthy = Window(app, title="Young People's Healthy Living", width = 1500, height = 700)
windowPlanHealthy.hide()

#Fitness page premium
windowPlanFitness = Window(app, title="Young People's Fitness Advice", width = 1500, height = 700)
windowPlanFitness.hide()

windowPlanWeight = Window(app, title="Bulking Up Fitness", width = 1500, height = 700)
windowPlanWeight.hide()

windowPlanSmoking = Window(app, title="Advice About Stopping Smoking", width = 1500, height = 700)
windowPlanSmoking.hide()

DarkModeButton = PushButton(windowMain, text="Dark Mode", grid=[6,0], width=27, command=DarkMode)
#LightModeButton = PushButton(windowMain, text="Light Mode", grid=[7,0], width=27, command=LightMode)

#Bank details window
windowBank = Window(app, title="Secure bank details", width = 1500, height = 600)
windowBank.hide()

Gologin_button = PushButton(app, text="Log In", command=open_windowLogIn)     
Gosignup_button = PushButton(app, text="Sign Up", command=open_windowSignUp)
closeS_button = PushButton(windowS, text="Close", command=close_window)
closeL_button = PushButton(windowL, text="Close", command=close_window)
picture = Picture(app, image="Tokafitness.png")
app.bg = "teal"

#Set up log in
text = Text(windowL, text="Enter username:")
input_boxU = TextBox(windowL)
text = Text(windowL, text="Enter password: \n")
input_boxP = TextBox(windowL, hide_text=True)   #hide_text=True makes the password have **** and not the real word
login_button = PushButton(windowL, text="Log In To Your Account", command=check_login) # pass username to check exists
signUpOnLogIn_button = PushButton(windowL, text="No account?\nSign up free!", command=open_windowSignUp)
text = Text(windowL, text="By logging in with ToKa Fitness, you agree to our terms and conditions which can be made available on request.", size=14)
picture = Picture(windowL, image="Tokafitness.png")


windowL.bg = "teal"
windowL.hide()
close_window()

#Set up sign up
text = Text(windowS, text="Enter a username:")
input_boxUs = TextBox(windowS)
text = Text(windowS, text="Enter a first name:")
input_boxFn = TextBox(windowS)
text = Text(windowS, text="Enter a surname:", width=45)
input_boxSn = TextBox(windowS)
text= Text(windowS, text ="Please enter a password:")
input_boxPa = TextBox(windowS, hide_text=True)  #hide_text=True makes the password have **** and not the real word - this is good because you don't want the user seeing their password
text = Text(windowS, text ="Confirm password:")
input_boxPasswordConfirm = TextBox(windowS, hide_text=True) #hide_text=True makes the password have **** and not the real word - this is good because you don't want the user seeing their password
text=Text(windowS, "Date of birth:")
input_boxDoB = TextBox(windowS)
text= Text(windowS, "Email:", width=100)
input_boxEmail = TextBox(windowS)
text = Text(windowS, text="By signing up with ToKa Fitness, you agree to our terms and conditions which can be made available on request.", size=14)
picture = Picture(windowS, image="Tokafitness.png")
buttonLogIn = PushButton(windowS, text="Go to log in", command=open_windowLogIn)
buttonSaveDetails = PushButton(windowS, text="Save details", command=sign_up)

windowS.bg = "teal"
windowS.hide()
close_window()

#Set up main screen
buttonFitness = PushButton(windowMain, text="Advice about fitness training", command=open_windowFitness)
buttonHealthy = PushButton(windowMain, text="Advice about healthy living", command=open_windowHealthy)
buttonPremium = PushButton(windowMain, text="Premium Plan - for Premium Users only", command=open_windowPremium)
buttonBank = PushButton(windowMain, text="Go Premium, click here to enter in your bank details - securely", command=open_windowBank)
windowMain.bg = "teal"
picture = Picture(windowMain, image="Tokafitness.png")
buttonLogOut = PushButton(windowMain, text="Log out", command=open_windowLogOut)

#Bank details form
textIntro = Text(windowBank, text="We are glad you want to go premium, feel free to use our secure bank details form here")
textName = Text(windowBank, text="Cardholder Name:")
input_boxCardName = TextBox(windowBank)
textNumber = Text(windowBank, text="Card number:")
input_boxNumber = TextBox(windowBank)
textExpiry = Text(windowBank, text = "Expiry date:")
input_boxExpiry = TextBox(windowBank)
textCVC = Text(windowBank, text = "CVC Code:")
input_boxCVC = TextBox(windowBank)
buttonSaveDetails = PushButton(windowBank, text="Go back", command=open_windowMain)


#Healthy living page
texthealthy1 = Text(windowHealthy, text="Eat five a day")
textblank= Text(windowHealthy, text="")
texthealthy2= Text(windowHealthy, text="Drink plenty of water")
PictureHealthy = Picture(windowHealthy, image="Theartofhealthyliving.png")
buttonGoBack = PushButton(windowHealthy, text="Go back", command=open_windowMain)

#Fitness advice page
textFitness1 = Text(windowFitness, text="Run at least once a day")
textblankFitness = Text(windowFitness, text="")
textFitness2 = Text(windowFitness, text="Keep healthy")
PictureFitness = Picture(windowFitness, image="Fitnesstips.png")
buttonGoBack = PushButton(windowFitness, text="Go back", command=open_windowMain)

#Premium content page
textblank= Text(windowPremium, text="")
textWeight = Text(windowPremium, text="Weight")
choice = ButtonGroup(windowPremium, options=["10-25kg", "25-50kg", "50kg+"], selected="10-25kg", horizontal=True)
textblank= Text(windowPremium, text="")
textblank= Text(windowPremium, text="")
textHeight = Text(windowPremium, text="Height")
choice = ButtonGroup(windowPremium, options=["1-1.5m", "1.5-2m", "2m+"], selected="1-1.5m", horizontal=True)
textblank= Text(windowPremium, text="")
textblank= Text(windowPremium, text="")
textAge = Text(windowPremium, text="Age")
choice = ButtonGroup(windowPremium, options=["Under 18", "18-30", "30+"], selected="Under 18", horizontal=True)
textblank= Text(windowPremium, text="")
textblank= Text(windowPremium, text="")
textHeight = Text(windowPremium, text="Smoker?")
choice = ButtonGroup(windowPremium, options=["Yes", "No"], selected="Yes", horizontal=True)
textblank= Text(windowPremium, text="")
picture = Picture(windowPremium, image="Tokafitness.png")
buttonGoBack = PushButton(windowPremium, text="Go back", command=open_windowMain)
buttonPlan = PushButton(windowPremium, text="See your plan", command=open_windowPlanHealthy)

#Premium plan page for healthy
textEat5 = Text(windowPlanHealthy, text="Eat five a day")
textblank= Text(windowPlanHealthy, text="")
textDrink = Text(windowPlanHealthy, text="Drink plenty of water")
PictureHealthy = Picture(windowPlanHealthy, image="Theartofhealthyliving.gif")
buttonGoNext = PushButton(windowPlanHealthy, text="Next", command=open_windowPlanFitness)

#Premium plan for fitness
textRun = Text(windowPlanFitness, text="Run at least once a day")
textblank= Text(windowPlanFitness, text="")
textHealthy = Text(windowPlanFitness, text="Keep healthy")
picture = Picture(windowPlanFitness, image="Running.gif")
buttonGoNext = PushButton(windowPlanFitness, text="Next", command=open_windowPlanWeight)

#Premium plan for weight
textCarbs = Text(windowPlanWeight, text= "Eat carbs after workout")
textblank= Text(windowPlanWeight, text="")
textFats = Text(windowPlanWeight, text="Eat healthy fats")
GifFitness = Picture(windowPlanWeight, image="Gainingweight.gif")
buttonGoNext = PushButton(windowPlanWeight, text="Next", command=open_windowPlanSmoking)

#Premium plan for smoking
textNicotine = Text(windowPlanSmoking, text="Don't use nicotine")
textblank= Text(windowPlanSmoking, text="")
textHealthier = Text(windowPlanSmoking, text="It'll make you healthier")
GifMartin = Picture(windowPlanSmoking, image="Martinsmoking.gif")
buttonCloseWindows = PushButton(windowPlanSmoking, text="Close all windows", command=close_Premiumwindow)
buttonReturnWeight = PushButton(windowPlanSmoking, text="Return to weight page", command=open_windowPlanWeight)
buttonReturnRun = PushButton(windowPlanSmoking, text="Return to running page", command=open_windowPlanFitness)
buttonReturnHealthy = PushButton(windowPlanSmoking, text="Return to healthy page", command=open_windowPlanHealthy)

app.display()
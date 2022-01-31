def check_loginStaff():
	global UserOn	#Who is logged in?
	
	username = inputboxUsername.value
	password = inputboxPassword.value
	print(username + password)

	query = f"select * from Staff_Table where S_UName = '{username}'"
	rows = query_database(database_file, query)
	print(rows)

	if len(rows) == 0:
		info("Error", "Username or password incorrect")
	else:
		#Username and password exist for the member of staff
		if inputboxPassword.value == rows[0][4]:
			info("Logged in", "User found and password correct")
			if TsAndCs.value == "Agree": #Ts and Cs have been ticked
				UserOn = rows[0][0]
				staffUser = 1 #This means a member of staff is logged in
				open_windowStaffDashboard()
			else:
				info("Error","Please check Ts and Cs")
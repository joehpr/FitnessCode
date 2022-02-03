def getStaffMessages():
	query = f"select * from Message_Table where S_ID = '{UserOn}'"
	rows = query_database(database_file, query)
	print(rows)

	if len(rows) == 0:
		info("Warning", "No messages found for this customer")
	else:
		#Put messages into a listbox
		info("Messages found", "Here are your messages")
		for x in range(0,len(rows)):
			listBoxMessagesStaff.append(rows[x])
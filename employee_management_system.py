#Setting up the titles, no variables here
print("Employee Management System")
print("-----------------------------------------------------------")
print("Your Information")
print("------------------------")

#Employee will input their information here, initializing variables
first_name = input("First Name: ")
last_name = input("Last Name: ")
company = input("Company: ")
street_address = input("Street Address: ")
city = input("City: ")
state = input("State: ")
zip_code = input("Zip Code: ")
hire_year = input("Hire Year: ")
print("-----------------------------------------------------------")

#Profile is created
print("Your Profile")
print("------------------------")
print(last_name + ", " + first_name) #added space after comma so they are separated by a space
print(company)
print(street_address)
print(city + ", " + state + " " + zip_code) #added city, state and zip_code here to complete the second line of address
print("Your temporary password: " + first_name + "*" + last_name + "%" + hire_year) #temporary password is first_name, an asterisk, last_name, percentage symbol and hire_year
print("Congratulations! Your profile has been created.") #show message to employee that the profile is created from user input
print("-----------------------------------------------------------")
print("Bye!")
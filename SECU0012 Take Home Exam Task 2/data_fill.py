survey_data = []  # originally an empty list

choice_1 = ["victim", "witness"] # variable list referring to question 1
choice_2 = ["bike", "scooter", "running", "dont know"] # variable list referring to question 2
choice_3 = ["males", "females", "dont know"] # variable list referring to question 3
choice_4 = ["one", "two", "dont know"] # variable list referring to question 4

for i in range(0, 20): # survey runs 20 times 
    while True:
        
        # Check if the input can be converted to an integer
        try:
            user_age = int(input("Enter age:"))  # variable where the user enters age 
        except ValueError:
            # If conversion fails, it's not a valid integer
            print("Invalid input. Please enter a valid age as a number.")
            continue  # Skip the rest of the loop and ask the user to enter age again
            
        if 18 < user_age < 50:  # age range must be between 18 to 50
            print("Thank you for choosing to participate in the survey.")
            break
        else:  # otherwise print the statement and make the user try again
            print("Sorry, but we want responses only from people under 50 and over 18.")

    user_in_incident = input("Were you the victim of phone snatching or a witness?: ") # input variable for question 1
    while user_in_incident not in choice_1: # if words in list 1 is not included, message below prints
        print(f"{user_in_incident} isn't in {choice_1}; please try again")
        user_in_incident = input("Were you the victim of phone snatching or a witness?: ")
        # user answers the first question and must be in one of the words in "" 

    transport_in_incident = input("Was the attacker using a bike, a scooter or were they running?:") # input variable for question 2
    while transport_in_incident not in choice_2:  # if words in list 2 is not included, message below prints
        print(f"{transport_in_incident} isn't in {choice_2}; please try again")
        user_in_incident = input("Was the attacker using a bike, a scooter or were they running?:")
        # user answers the second question and must be in one of the words in "" 

    gender_in_incident = input("Were they males or females?:") # input variable for question 3
    while gender_in_incident not in choice_3:
        print(f"{gender_in_incident} isn't in {choice_3}; please try again") # if words in list 3 is not included, message below prints
        user_in_incident = input("Were they males or females?:")
        # user answers the third question and must be in one of the words in "" 

    attacker_in_incident = input("Was it one or two attackers?:") # input variable for question 4
    while attacker_in_incident not in choice_4: # if words in list 4 is not included, message below prints
        print(f"{attacker_in_incident} isn't in {choice_4}; please try again") 
        user_in_incident = input("Was it one or two attackers?:")
        # user answers the fourth question and must be in one of the words in "" 

    user_data = [str(user_age), user_in_incident, transport_in_incident, gender_in_incident, attacker_in_incident]
    # a variable which contains all the previous defined variables mentioned above
    survey_data.append(user_data)  # user data is added to survey data   

file_path = r'C:\Users\user\OneDrive\Desktop\P SCS\Task 2\dataset.txt'

with open(file_path, "a") as f: # opens file to append data to it
    for line in survey_data:
        f.write(",".join(line) + "\n")  # this will result in the wanted format


        

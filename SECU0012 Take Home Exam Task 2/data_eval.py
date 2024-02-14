file_path = r'C:\Users\user\OneDrive\Desktop\P SCS\Task 2\dataset.txt' # file path of txt file 

ages = [] # originally an empty list 
total_age = 0 # originally an empty variable
num_ages = 0 # originally an empty variable

victim_dont_know_count = [0] * 5  # Initialize a list to count "don't know" at each index
witness_dont_know_count = [0] * 5 # Initialize a list to count "don't know" at each index

bike_count = 0 # originally an empty variable
scooter_count = 0 # originally an empty variable
running_count = 0 # originally an empty variable

with open(file_path, "r") as f: 
    for i, line in enumerate(f): # runs through every line in the txt file
        line = line.strip() # removes leading and trailing whitespaces
        survey_response = line.split(",") # splits every element as a list 
        print(survey_response)
      
        age = int(survey_response[0]) # returns integer value of element in index 0 of list 
        total_age += age # adds age to variable
        num_ages += 1 # adds 1 to variable
        ages.append(age) # adds age to list 

        # Check if there is a "don't know" answer at each index
        for index, answer in enumerate(survey_response[1:]):
            if answer == 'dont know':
                if i < 10:  # First 10 lists are victims
                    victim_dont_know_count[index] += 1
                else:  # Next 10 lists are witnesses
                    witness_dont_know_count[index] += 1

        # Checks for 'running' in index 2 of every survey response
        if survey_response[2] == 'running':
            running_count += 1 # adds 1 to the variable
        # Checks for 'scooter' in index 2 of every survey response
        elif survey_response[2] == 'scooter':
            scooter_count += 1 # adds 1 to the variable
        # Checks for 'bike' in index 2 of every survey response
        elif survey_response[2] == 'bike':
            bike_count += 1 # adds 1 to the variable

avg_age = total_age / num_ages # formula for calculating average 
print(f"Average age: {avg_age}")

ages.sort() # sorts ages in ascending order from list 
if num_ages % 2 == 0:
    # If the number is even, median is the average of the two middle values
    median = (ages[num_ages // 2 - 1] + ages[num_ages // 2]) / 2
else:
    # If the number of ages is odd, middle value is taken as the median
    median = ages[num_ages // 2]

print(f"Median: {median}")

# Answer the questions
for index, count in enumerate(victim_dont_know_count): # counts number of dont know responses from victim
    print(f"Number of 'don't know' answers at index {index} from victims: {count}")

for index, count in enumerate(witness_dont_know_count): # counts number of dont know responses from witness
    print(f"Number of 'don't know' answers at index {index} from witnesses: {count}")

print(f"Number of crimes perpetrated by bike: {bike_count}")
print(f"Number of crimes perpetrated by running: {running_count}")
print(f"Number of crimes perpetrated by scooter: {scooter_count}")


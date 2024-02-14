# Task 1

import pickle

def is_valid_neighbourhood(name):
    # Checks if the neighbourhood name input starts with a capital letter and the rest are small letters
    return name.istitle()

def is_valid_crime_type(crime_type):
    # Checks if the crime type input is in all small letters
    return crime_type.islower()

def neighbourhoods():
    neighbourhood_list = [] # empty list variable that will collect user neighbourhood inputs
    while True:
        neighbourhood_input = input("Enter a neighbourhood name or 'done' to finish: ") # input variable to enter neighbourhood name or finish to proceed
        if neighbourhood_input.lower() == "done": # function proceeds if 'done' is entered
            break
        if is_valid_neighbourhood(neighbourhood_input): # checks through valid function for neighbourhood
            neighbourhood_list.append(neighbourhood_input) # adds neighbourhood input to the list 
        else:
            print("Please start with a capital letter for the neighbourhood name.") # proceeds to else statement if input case check is incorrect
    print(neighbourhood_list)
    return neighbourhood_list

def year():
    while True:
        year_input = input("Enter a year (YYYY) format: ") # input variable to enter year
        if year_input.isdigit() and len(year_input) == 4:  # Check if input is a digit and has length 4
            return int(year_input)  # Convert the input to an integer
        else:
            print("Please enter a valid year in YYYY format.")

def month():
    while True:
        month_input = input("Enter a month (MM) format: ") # input variable to enter month
        if month_input.isdigit() and 1 <= int(month_input) <= 12:  # Check if input is a digit and within range
            return int(month_input)  # Convert the input to an integer
        else:
            print("Please enter a valid month within the range (1-12).")



def crime_type():
    crime_type_list = ['burglary', 'assault', 'cybercrime', 'fraud', 'vandalism', 'murder', 'robbery']
    crime_type_input = input("Enter a type of crime: ")  # Input variable to enter crime type

    if crime_type_input not in crime_type_list:
        print("Please choose one of the following crime types from the crime type list.")
        return crime_type()  # Re-prompt for valid input

    if is_valid_crime_type(crime_type_input):  # Checks through valid function for crime type input
        return crime_type_input
    else:
        print("Invalid input. Please use all small letters.") 
        return crime_type()

def main(): # collects inputs from user for each function
    neighbourhood_list = neighbourhoods()
    year_input = year()
    month_input = month()
    crime_type_input = crime_type()

    parameters = { # paramater dictionary to store inputs from each function
        'neighbourhoods': neighbourhood_list,
        'year': year_input,
        'month': month_input,
        'crime_type': crime_type_input
    }
    
    print(parameters) # prints parameter dictionary

    with open('parameters.pkl', 'wb') as file: # Saves the parameters dictionary using pickle
        pickle.dump(parameters, file)

if __name__ == "__main__":
    main()
    
    
    
# Task 2

import requests
import pickle

def neighbourhood_ids(neighbourhood_names):
    # API URL for neighbourhoods
    neighbourhood_url = 'https://data.police.uk/api/metropolitan/neighbourhoods'
    
    # Make an API request to get neighbourhood data
    response = requests.get(neighbourhood_url)

    # Changes the API response to JSON format
    neighbourhood_data = response.json()

    # Check if the response is a list of dictionaries
    if isinstance(neighbourhood_data, list):
        # Extract the IDs for each filtered neighbourhood
        dict_nid = {}
        for data in neighbourhood_data: 
            if data['name'] in neighbourhood_names: # If name is in neighbourhood_names
                dict_nid[data['name']] = data['id'] # Match neighbourhood name with respective id     
        return dict_nid
    else:
        print("Unexpected format in the API response") # Otherwise print this statement
    return None

def main():
    # List of neighbourhood names from user inputs
    user_input_neighbourhood_names = ["East Greenwood", "Peckham", "Goose Green", "Newington", "Arsenal"]

    # Retrieve the IDs for the specified neighbourhoods
    dict_nid = neighbourhood_ids(user_input_neighbourhood_names)

    if dict_nid:
        # Print whether the provided neighbourhoods are found in the retrieved IDs
        for neighbourhood_name in user_input_neighbourhood_names:
            if neighbourhood_name in dict_nid: # if neighbourhood name is in URL
                # Print this statement
                print(f"Neighbourhood '{neighbourhood_name}' found (ID: {dict_nid[neighbourhood_name]})")
                # Otherwise print this statement
            else:
                print(f"Neighbourhood '{neighbourhood_name}' not found in the retrieved IDs.")
        
        # Save the dictionary of neighbourhood names and IDs using pickle
        with open('dict_nid.pkl', 'wb') as file:
            pickle.dump(dict_nid, file)

if __name__ == "__main__":
    main()
    
    
    
    
# Task 3


import json

# Arsenal boundary coordinates 

# Arsenal boundary coordinates url
arsenal_url = 'https://data.police.uk/api/metropolitan/E05013697/boundary' 

# Function of arsenal boundary coordinates 
def Arsenal_boundary_coordinates(arsenal_url):
    response = requests.get(arsenal_url) # Makes a request on the url
    boundary_data = response.text  # Retrieve responses as text
    
    # loads boundary data in JSON format
    coordinates_json = json.loads(boundary_data)
    
    # Extract latitude and longitude pairs
    coordinates = [(float(coord['latitude']), float(coord['longitude'])) for coord in coordinates_json] # Gets all coordinates of Arsenal neighbourhood as floats
    
    return coordinates

# Gets coordinates for the Arsenal neighborhood
arsenal_coordinates = Arsenal_boundary_coordinates(arsenal_url) # Collects coordinates from Arsenal neighbourhood function
if arsenal_coordinates:
    print(f"Boundary coordinates of Arsenal neighborhood (latitude, Longitude): {arsenal_coordinates}") # Prints coordinates of Arsenal neighbourhood as floats
    



# Peckham boundary coordinates 

# Peckham boundary coordinates url    
peckham_url = 'https://data.police.uk/api/metropolitan/E05011110/boundary' 

# Function of peckham boundary coordinates 
def Peckham_boundary_coordinates(peckham_url):
    response = requests.get(peckham_url) # Makes a request on the url
    boundary_data = response.text  # Retrieves response as text
    
    # loads boundary data in JSON format
    coordinates_json = json.loads(boundary_data)
    
    # Gets all coordinates of Peckham neighbourhood as floats
    coordinates = [(float(coord['latitude']), float(coord['longitude'])) for coord in coordinates_json] 
    
    return coordinates

# Gets coordinates for the Peckham neighborhood
peckham_coordinates = Peckham_boundary_coordinates(peckham_url) # Collects coordinates from Peckham neighbourhood function
if peckham_coordinates:
    print(f"Boundary coordinates of Peckham neighborhood (latitude, Longitude): {peckham_coordinates}") # Prints coordinates of Peckham neighbourhood as floats
    




# Goose Green boundary coordinates 

# Goose Green boundary coordinates url
Goose_Green_url = 'https://data.police.uk/api/metropolitan/E05011103/boundary'

# Function of goose green boundary coordinates 
def Goose_Green_boundary_coordinates(Goose_Green_url):
    response = requests.get(Goose_Green_url) # Makes a request on the url
    boundary_data = response.text  # Retrieve response as text
    
    # loads boundary data in JSON format
    coordinates_json = json.loads(boundary_data)
    
    # Gets all coordinates of Goose Green neighbourhood as floats
    coordinates = [(float(coord['latitude']), float(coord['longitude'])) for coord in coordinates_json]
    
    return coordinates

# Get coordinates for the Goose Green neighborhood
goose_green_coordinates = Goose_Green_boundary_coordinates(Goose_Green_url)
if goose_green_coordinates:
    print(f"Boundary coordinates of Goose Green neighborhood (latitude, Longitude): {goose_green_coordinates}") # Prints coordinates of Goose Green neighbourhood as floats





# Newington boundary coordinates 

# Newington boundary coordinates url
Newington_url = 'https://data.police.uk/api/metropolitan/E05011105/boundary'

# Function of Newington boundary coordinates 
def Newington_boundary_coordinates(Newington_url):
    response = requests.get(Newington_url) # Makes a request on the url
    boundary_data = response.text  # Retrieve response as text
    
    # loads boundary data in JSON format
    coordinates_json = json.loads(boundary_data)
    
    # Gets all coordinates of Newington neighbourhood as floats
    coordinates = [(float(coord['latitude']), float(coord['longitude'])) for coord in coordinates_json]
    
    return coordinates

# Get coordinates for the Newington neighborhood
newington_coordinates = Newington_boundary_coordinates(Newington_url)
if newington_coordinates:
    print(f"Boundary coordinates of Newington neighborhood (latitude, Longitude): {newington_coordinates}") # Prints coordinates of Newington neighbourhood as floats



# Task 4

# Function to calculate bounding box from coordinates
def polygon_bounding_box(coordinates):
    # Extract latitude and longitude lists separately
    latitudes = [coord[0] for coord in coordinates]
    longitudes = [coord[1] for coord in coordinates]

    # Find maximum, minimum, and medium latitude and longitude
    max_lat = str(max(latitudes))
    min_lat = str(min(latitudes))
    med_lat = str(sorted(latitudes)[len(latitudes)//2])

    max_long = str(max(longitudes))
    min_long = str(min(longitudes))
    med_long = str(sorted(longitudes)[len(longitudes)//2])

    # Create vertices for the bounding box
    top = max_lat + ',' + med_long
    bottom = min_lat + ',' + med_long
    left = min_long + ',' + med_lat
    right = max_long + ',' + med_lat

    # Concatenate the vertices to create the polygon
    polygon = top + ':' + right + ':' + bottom + ':' + left

    return polygon




# Arsenal polygon coordinates 

# Arsenal boundary coordinates url
arsenal_url = 'https://data.police.uk/api/metropolitan/E05013697/boundary'

# Function of arsenal boundary coordinates
def Arsenal_boundary_coordinates(arsenal_url):
    response = requests.get(arsenal_url) # Makes a request on the url
    boundary_data = response.text  # Retrieve responses as text
    
    # loads boundary data in JSON format
    coordinates_json = json.loads(boundary_data)
    
    # Extract latitude and longitude pairs
    coordinates = [(float(coord['latitude']), float(coord['longitude'])) for coord in coordinates_json] # Gets all coordinates of Arsenal neighbourhood as floats
    
    return coordinates

# Gets coordinates for the Arsenal neighborhood
arsenal_coordinates = Arsenal_boundary_coordinates(arsenal_url) # Collects coordinates from Arsenal neighbourhood function
if arsenal_coordinates:
    # Calculate bounding box
    bounding_box = polygon_bounding_box(arsenal_coordinates)
    print(f"Polygon coordinates for Arsenal neighborhood: {bounding_box}") # Prints bounding box coordinates

# Saves bounding box coordinates in a dictionary with neighborhood ID as key
    arsenal_data = {
        'id': 'E05013697',  # Replace 'id' with the actual neighborhood ID
        'polygon coords': bounding_box
    }
    print(f"Arsenal crime neighborhood data: {arsenal_data}")  # Display neighborhood data
    
    
    
    
# Peckham boundary coordinates 

# Peckham boundary coordinates url    
peckham_url = 'https://data.police.uk/api/metropolitan/E05011110/boundary' 

# Function of peckham boundary coordinates 
def Peckham_boundary_coordinates(peckham_url):
    response = requests.get(peckham_url) # Makes a request on the url
    boundary_data = response.text  # Retrieves response as text
    
    # loads boundary data in JSON format
    coordinates_json = json.loads(boundary_data)
    
    # Gets all coordinates of Peckham neighbourhood as floats
    coordinates = [(float(coord['latitude']), float(coord['longitude'])) for coord in coordinates_json] 
    
    return coordinates

# Gets coordinates for the Peckham neighborhood
peckham_coordinates = Peckham_boundary_coordinates(peckham_url) # Collects coordinates from Peckham neighbourhood function
if peckham_coordinates:
    # Calculate bounding box
    bounding_box = polygon_bounding_box(peckham_coordinates)
    print(f"Polygon coordinates for Peckham neighborhood: {bounding_box}") # Prints coordinates of Peckham neighbourhood as floats
# Saves bounding box coordinates in a dictionary with neighborhood ID as key
    peckham_data = {
        'id': 'E05011110',  # Replace 'id' with the actual neighborhood ID
        'polygon coords': bounding_box
    }
    print(f"Peckham crime neighborhood data: {peckham_data}")  # Display neighborhood data




# Goose Green boundary coordinates 

# Goose Green boundary coordinates url
Goose_Green_url = 'https://data.police.uk/api/metropolitan/E05011103/boundary'

# Function of goose green boundary coordinates 
def Goose_Green_boundary_coordinates(Goose_Green_url):
    response = requests.get(Goose_Green_url) # Makes a request on the url
    boundary_data = response.text  # Retrieve response as text
    
    # loads boundary data in JSON format
    coordinates_json = json.loads(boundary_data)
    
    # Gets all coordinates of Goose Green neighbourhood as floats
    coordinates = [(float(coord['latitude']), float(coord['longitude'])) for coord in coordinates_json]
    
    return coordinates

# Get coordinates for the Goose Green neighborhood
goose_green_coordinates = Goose_Green_boundary_coordinates(Goose_Green_url)
if goose_green_coordinates:
    bounding_box = polygon_bounding_box(goose_green_coordinates)
    print(f"Polygon coordinates for Goose Green neighborhood: {bounding_box}") # Prints coordinates of Goose Green neighbourhood as floats

# Saves bounding box coordinates in a dictionary with neighborhood ID as key
    goose_green_data = {
        'id': 'E05011103',  # Replace 'id' with the actual neighborhood ID
        'polygon coords': bounding_box
    }
    print(f"Goose Green crime neighborhood data: {goose_green_data}")  # Display neighborhood data





# Newington boundary coordinates 

# Newington boundary coordinates url
Newington_url = 'https://data.police.uk/api/metropolitan/E05011105/boundary'

# Function of Newington boundary coordinates 
def Newington_boundary_coordinates(Newington_url):
    response = requests.get(Newington_url) # Makes a request on the url
    boundary_data = response.text  # Retrieve response as text
    
    # loads boundary data in JSON format
    coordinates_json = json.loads(boundary_data)
    
    # Gets all coordinates of Newington neighbourhood as floats
    coordinates = [(float(coord['latitude']), float(coord['longitude'])) for coord in coordinates_json]
    
    return coordinates

# Get coordinates for the Newington neighborhood
newington_coordinates = Newington_boundary_coordinates(Newington_url)
if newington_coordinates:
    bounding_box = polygon_bounding_box(newington_coordinates)
    print(f"Polygon coordinates of Newington neighborhood: {bounding_box}") # Prints coordinates of Newington neighbourhood as floats

# Saves bounding box coordinates in a dictionary with neighborhood ID as key
    newington_data = {
        'id': 'E05011105',  # Replace 'id' with the actual neighborhood ID
        'polygon coords': bounding_box
    }
    print(f"Newington crime neighborhood data: {newington_data}")  # Display neighborhood data



# Task 5

import csv
import requests
import json


# Crime data function for Arsenal neighbourhood
def arsenal_crime_data(arsenal_location_lat, arsenal_location_lng, arsenal_date, arsenal_neighborhood):
    arsenal_crime_url = f"https://data.police.uk/api/crimes-at-location?date={arsenal_date}&lat={arsenal_location_lat}&lng={arsenal_location_lng}"
    
    response = requests.get(arsenal_crime_url) # Makes a request on the url
    crime_data = response.json() # Retrieves response as json 
    arsenal_results = [] # Empty list of results variable 

    arsenal_unique_crime_events = set() # Variable to store unique crime events

    for crime in crime_data:
            arsenal_category = crime['category'] # Looks at category
            arsenal_latitude = crime['location']['latitude'] # Looks at latitude of location
            arsenal_longitude = crime['location']['longitude'] # Looks at longitude of location

            # Checks if crime event is unique 
            arsenal_event = (arsenal_category, arsenal_latitude, arsenal_longitude)
            if arsenal_event not in arsenal_unique_crime_events:
                arsenal_unique_crime_events.add(arsenal_event)
                arsenal_result = [arsenal_neighborhood, arsenal_category, arsenal_latitude, arsenal_longitude]
                arsenal_results.append(arsenal_result)

    return arsenal_results

# Arsenal location coordinates, date, and neighborhood
arsenal_location_lat = 51.557652311787
arsenal_location_lng = -0.098362612255377
arsenal_date = "2023-02"
arsenal_neighborhood = 'Arsenal'  # Replace with the neighborhood name

# Retrieves crime data for Arsenal and chosen date
crime_results = arsenal_crime_data(arsenal_location_lat, arsenal_location_lng, arsenal_date, arsenal_neighborhood)
if crime_results:
    for result in crime_results:
        print(f"Arsenal crime data: {result}")
       


# Task 6

# Function to write results to CSV
def write_results_to_csv(results, arsenal_csv_file):
    # Checks whether results list is empty
    if not results:
        print("No results to write to CSV.")
        return

    # Define the CSV file header
    arsenal_header = ['Neighbourhood', 'Category', 'Latitude', 'Longitude']

    # Opens CSV file for writing
    with open(arsenal_csv_file, mode='w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Writes header to the CSV file
        csv_writer.writerow(arsenal_header)

        # Iterate through the results list and write each row to the CSV file
        for result in results:
            csv_writer.writerow(result)

    print(f"Results have been added to {arsenal_csv_file}.")

# Retrieves crime data for Arsenal and chosen date
crime_results = arsenal_crime_data(arsenal_location_lat, arsenal_location_lng, arsenal_date, arsenal_neighborhood)

# CSV filename for Arsenal crime data
arsenal_csv_file = 'arsenal_crime_results.csv'

# Write results to CSV
write_results_to_csv(crime_results, arsenal_csv_file)
        
        
# Crime data function for Peckham neighbourhood
def peckham_crime_data(peckham_location_lat, peckham_location_lng, peckham_date, peckham_neighborhood):
    peckham_crime_url = f"https://data.police.uk/api/crimes-at-location?date={peckham_date}&lat={peckham_location_lat}&lng={peckham_location_lng}"
    
    response = requests.get(peckham_crime_url) # Makes a request on the url
    crime_data = response.json() # Retrieves response as json 
    peckham_results = [] # Empty list of results variable 

    peckham_unique_crime_events = set() # Variable to store unique crime events

    for crime in crime_data:
        peckham_category = crime['category'] # Looks at category
        peckham_latitude = crime['location']['latitude'] # Looks at latitude of location
        peckham_longitude = crime['location']['longitude'] # Looks at longitude of location

        # Checks if crime event is unique 
        peckham_event = (peckham_category, peckham_latitude, peckham_longitude)
        if peckham_event not in peckham_unique_crime_events:
            peckham_unique_crime_events.add(peckham_event)
            peckham_result = [peckham_neighborhood, peckham_category, peckham_latitude, peckham_longitude]
            peckham_results.append(peckham_result)

    return peckham_results
   
# Peckham location coordinates, date, and neighborhood
peckham_location_lat = 51.474254702682
peckham_location_lng = -0.077405447747295
peckham_date = "2023-07"
peckham_neighborhood = 'Peckham'

# Retrieves crime data for Peckham and chosen date
peckham_crime_results = peckham_crime_data(peckham_location_lat, peckham_location_lng, peckham_date, peckham_neighborhood)
if peckham_crime_results:
    for result in peckham_crime_results:
        print(f"Peckham crime data: {result}")



# Task 6

# Function to write results to CSV
def write_results_to_csv(results, peckham_csv_file):
    # Checks whether results list is empty
    if not results:
        print("No results to write to CSV.")
        return

    # Define the CSV file header
    peckham_header = ['Neighbourhood', 'Category', 'Latitude', 'Longitude']

    # Opens CSV file for writing
    with open(peckham_csv_file, mode='w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Writes header to the CSV file
        csv_writer.writerow(peckham_header)

        # Iterate through the results list and write each row to the CSV file
        for result in results:
            csv_writer.writerow(result)

    print(f"Results have been added to {peckham_csv_file}.")

# Retrieves crime data for Peckham and chosen date
crime_results = peckham_crime_data(peckham_location_lat, peckham_location_lng, peckham_date, peckham_neighborhood)

# CSV filename for Peckham crime data
peckham_csv_file = 'peckham_crime_results.csv'

# Writes results to CSV file
write_results_to_csv(crime_results, peckham_csv_file)




# Crime data function for Goose Green neighbourhood
def goose_green_crime_data(goose_green_location_lat, goose_green_location_lng, goose_green_date, goose_green_neighborhood):
    goose_green_crime_url = f"https://data.police.uk/api/crimes-at-location?date={goose_green_date}&lat={goose_green_location_lat}&lng={goose_green_location_lng}"
    
    response = requests.get(goose_green_crime_url) # Makes a request on the url
    crime_data = response.json() # Retrieves response as json 
    goose_green_results = [] # Empty list of results variable

    goose_green_unique_crime_events = set()  # Variable to store unique crime events

    for crime in crime_data:
        goose_green_category = crime['category'] # Looks at category
        goose_green_latitude = crime['location']['latitude'] # Looks at latitude of location
        goose_green_longitude = crime['location']['longitude'] # Looks at longitude of location

        # Checks if crime event is unique
        goose_green_event = (goose_green_category, goose_green_latitude, goose_green_longitude)
        if goose_green_event not in goose_green_unique_crime_events:
            goose_green_unique_crime_events.add(goose_green_event)
            goose_green_result = [goose_green_neighborhood, goose_green_category, goose_green_latitude, goose_green_longitude]
            goose_green_results.append(goose_green_result)

    return goose_green_results

   
# Goose Green location coordinates, date, and neighborhood
goose_green_location_lat = 51.458748868743
goose_green_location_lng = -0.066286337928898
goose_green_date = "2023-01"
goose_green_neighborhood = 'Goose Green'

# Retrieves crime data for Goose Green and chosen date
goose_green_crime_results = goose_green_crime_data(goose_green_location_lat, goose_green_location_lng, goose_green_date, goose_green_neighborhood)
if goose_green_crime_results:
    for result in goose_green_crime_results:
        print(f"Goose Green crime data: {result}")
        
        
# Task 6

# Function to write results to CSV
def write_results_to_csv(results, goose_green_csv_file):
    # Checks whether results list is empty
    if not results:
        print("No results to write to CSV.")
        return

    # Define the CSV file header
    goose_green_header = ['Neighbourhood', 'Category', 'Latitude', 'Longitude']

    # Opens CSV file for writing
    with open(goose_green_csv_file, mode='w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Writes header to the CSV file
        csv_writer.writerow(goose_green_header)

        # Iterate through the results list and write each row to the CSV file
        for result in results:
            csv_writer.writerow(result)

    print(f"Results have been added to {goose_green_csv_file}.")

# Retrieves crime data for Goose Green and chosen date
crime_results = goose_green_crime_data(goose_green_location_lat, goose_green_location_lng, goose_green_date, goose_green_neighborhood)

# CSV filename for Goose Green crime data
goose_green_csv_file = 'goose_green_crime_results.csv'

# Writes results to CSV file
write_results_to_csv(crime_results, goose_green_csv_file)

        
        


# Crime data function for Newington neighbourhood
def newington_crime_data(newington_location_lat, newington_location_lng, newington_date, newington_neighborhood):
    newington_crime_url = f"https://data.police.uk/api/crimes-at-location?date={newington_date}&lat={newington_location_lat}&lng={newington_location_lng}"
    
    response = requests.get(newington_crime_url) # Makes a request on the url
    crime_data = response.json() # Retrieves response as json 
    newington_results = [] # Empty list of results variable

    newington_unique_crime_events = set()  # Variable to store unique crime events

    for crime in crime_data:
        newington_category = crime['category'] # Looks at category
        newington_latitude = crime['location']['latitude'] # Looks at latitude of location
        newington_longitude = crime['location']['longitude'] # Looks at longitude of location

        # Checks if crime event is unique
        newington_event = (newington_category, newington_latitude, newington_longitude)
        if newington_event not in newington_unique_crime_events:
            newington_unique_crime_events.add(newington_event)
            newington_result = [newington_neighborhood, newington_category, newington_latitude, newington_longitude]
            newington_results.append(newington_result)

    return newington_results

# Newington location coordinates, date, and neighborhood
newington_location_lat = 51.480853513069
newington_location_lng = -0.10447095482967
newington_date = "2023-05"
newington_neighborhood = 'Newington'

# Retrieves crime data for Newington and chosen date
newington_crime_results = newington_crime_data(newington_location_lat, newington_location_lng, newington_date, newington_neighborhood)
if newington_crime_results:
    for result in newington_crime_results:
        print(f"Newington crime data: {result}")
        
        
# Task 6

# Function to write results to CSV
def write_results_to_csv(results, newington_csv_file):
    # Checks whether results list is empty
    if not results:
        print("No results to write to CSV.")
        return

    # Define the CSV file header
    newington_header = ['Neighbourhood', 'Category', 'Latitude', 'Longitude']

    # Opens CSV file for writing
    with open(newington_csv_file, mode='w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Writes header to the CSV file
        csv_writer.writerow(newington_header)

        # Iterate through the results list and write each row to the CSV file
        for result in results:
            csv_writer.writerow(result)

    print(f"Results have been added to {newington_csv_file}.")

# Retrieves crime data for Newington and chosen date
crime_results = newington_crime_data(newington_location_lat, newington_location_lng, newington_date, newington_neighborhood)

# CSV filename for Peckham crime data
newington_csv_file = 'newington_crime_results.csv'

# Writes results to CSV file
write_results_to_csv(crime_results, newington_csv_file)


# Task 7

import csv 
import requests

# Function to write burglary results to CSV
def write_burglary_results_to_csv(burglary_results, burglary_csv_file):

    # Opens CSV file for appending
    with open(burglary_csv_file, mode='a', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)
        
        burglary_header = ['Category', 'Latitude', 'Longitude', 'Street name', 'Outcome category', 'Outcome status', 'Outcome date']
        
        csv_writer.writerow(burglary_header)

        # Iterates through the results list and write each row to the CSV file
        for result in burglary_results:
            csv_writer.writerow([
                result['category'],
                result['location']['latitude'],
                result['location']['longitude'],
                result['location']['street']['name'],
                result['outcome_status']['category'],
                result['outcome_status']['date']
            ])

    print(f"Results have been added to {burglary_csv_file}.")

# Neighbourhoods list in dictionary format
neighborhoods = {
    'Peckham': {'lat': 51.474254702682, 'lng': -0.077405447747295},
    'Bexleyheath': {'lat': 51.452674492684, 'lng': 0.13737750812627},
    'West ham': {'lat': 51.531308081133, 'lng':0.017579512291011},
    'Golders Green': {'lat':51.589778519051, 'lng':-0.19980069833419},
    'King Cross': {'lat':51.541143286328, 'lng':-0.12506277440316}
}

# CSV file for burglary results 
burglary_csv_file = 'burglary_results.csv'

# Iterates through all neighborhoods and appends results from each to the same CSV file
for names, coordinates in neighborhoods.items():
    url = f'https://data.police.uk/api/crimes-street/burglary?lat={coordinates["lat"]}&lng={coordinates["lng"]}&date=2023-05'
    response = requests.get(url)
    if response.status_code == 200:
        burglary_data = response.json()
        write_burglary_results_to_csv(burglary_data, burglary_csv_file)
    else:
        print(f"Failed to fetch data for following neighbourhoods, status code {response.status_code}")
      
        
      
        
      

# Function to write robbery results to CSV
def write_robbery_results_to_csv(robbery_results, robbery_csv_file):

    # Opens CSV file for appending
    with open(robbery_csv_file, mode='a', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)
        
        robbery_header = ['Category', 'Latitude', 'Longitude', 'Street name', 'Outcome category', 'Outcome date']
        
        csv_writer.writerow(robbery_header)

        # Iterates through the results list and write each row to the CSV file
        for result in robbery_results:
            csv_writer.writerow([
                result['category'],
                result['location']['latitude'],
                result['location']['longitude'],
                result['location']['street']['name'],
                result['outcome_status']['category'],
                result['outcome_status']['date']
            ])

    print(f"Results have been added to {robbery_csv_file}.")

# Neighbourhoods list in dictionary format
neighborhoods = {
    'Peckham': {'lat': 51.474254702682, 'lng': -0.077405447747295},
    'Bexleyheath': {'lat': 51.452674492684, 'lng': 0.13737750812627},
    'West ham': {'lat': 51.531308081133, 'lng':0.017579512291011},
    'Golders Green': {'lat':51.589778519051, 'lng':-0.19980069833419},
    'King Cross': {'lat':51.541143286328, 'lng':-0.12506277440316}
}

# CSV file for robbery results 
robbery_csv_file = 'robbery_results.csv'

# Iterates through all neighborhoods and appends results from each to the same CSV file
for names, coordinates in neighborhoods.items():
    url = f'https://data.police.uk/api/crimes-street/robbery?lat={coordinates["lat"]}&lng={coordinates["lng"]}&date=2023-05'
    response = requests.get(url)
    if response.status_code == 200:
        robbery_data = response.json()
        write_robbery_results_to_csv(robbery_data, robbery_csv_file)
    else:
        print(f"Failed to fetch data for following neighbourhoods, status code {response.status_code}")





# Scatter plots 

import requests
import matplotlib.pyplot as plt


# Function for burglary scatter plot
def burglary_scatter_plot(crime_name, neighborhoods, date, month):
    for neighborhood, coords in neighborhoods.items():
        
        # General crime type link for burglary and robbery 
        crimetype_url = f"https://data.police.uk/api/crimes-street/{crime_name}?lat={coords['lat']}&lng={coords['lng']}&date={date}-{month}"

        # Requests data from URL
        response = requests.get(crimetype_url)

        # Checks if request was successful (status code 200)
        if response.status_code == 200:
            # Extracts coordinates based on given neighborhood details
            burglary_data = response.json()
            latitudes = [float(data['location']['latitude']) for data in burglary_data]
            longitudes = [float(data['location']['longitude']) for data in burglary_data]

            # Creates a scatter plot of burglary crimes for every neighborhood below
            plt.figure(figsize=(10, 8))
            plt.scatter(longitudes, latitudes, label=f'{neighborhood} - {date}-{month}')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.title(f'{crime_name} scatter plot in neighborhood')
            plt.legend()
            plt.show()
        else:
            print(f"Error: Unable to fetch data from the API for {neighborhood}. Status Code: {response.status_code}")

# Details of coordinates for the 5 neighborhoods
neighborhoods = {
    'Peckham': {'lat': 51.474254702682, 'lng': -0.077405447747295},
    'Bexleyheath': {'lat': 51.452674492684, 'lng': 0.13737750812627},
    'West ham': {'lat': 51.531308081133, 'lng':0.017579512291011},
    'Golders Green': {'lat':51.589778519051, 'lng':-0.19980069833419},
    'King Cross': {'lat':51.541143286328, 'lng':-0.12506277440316}
}

# Returns burglary scatter plot and makes a scatter plot for each of the 5 neighborhoods

burglary_scatter_plot('burglary', neighborhoods, 2023, '05')






# Function for robbery scatter plot
def robbery_scatter_plot(crime_name, neighborhoods, date, month):
    for neighborhood, coords in neighborhoods.items():
        
        # General crime type link for burglary and robbery 
        crimetype_url = f"https://data.police.uk/api/crimes-street/{crime_name}?lat={coords['lat']}&lng={coords['lng']}&date={date}-{month}"

        # Requests data from URL
        response = requests.get(crimetype_url)

        # Checks if request was successful (status code 200)
        if response.status_code == 200:
            # Extracts coordinates based on given neighborhood details
            robbery_data = response.json()
            latitudes = [float(data['location']['latitude']) for data in robbery_data]
            longitudes = [float(data['location']['longitude']) for data in robbery_data]

            # Creates a scatter plot of robbery crimes for every neighborhood below
            plt.figure(figsize=(10, 8))
            plt.scatter(longitudes, latitudes, label=f'{neighborhood} - {date}-{month}')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.title(f'{crime_name} scatter plot in neighborhood')
            plt.legend()
            plt.show()
        else:
            print(f"Error: Unable to fetch data for neighborhood. Status Code: {response.status_code}")

# Details of coordinates for the 5 neighborhoods
neighborhoods = {
    'Peckham': {'lat': 51.474254702682, 'lng': -0.077405447747295},
    'Bexleyheath': {'lat': 51.452674492684, 'lng': 0.13737750812627},
    'West ham': {'lat': 51.531308081133, 'lng':0.017579512291011},
    'Golders Green': {'lat':51.589778519051, 'lng':-0.19980069833419},
    'King Cross': {'lat':51.541143286328, 'lng':-0.12506277440316}
}

# Returns robbery scatter plot and makes a scatter plot for each of the 5 neighborhoods
robbery_scatter_plot('robbery', neighborhoods, 2023, '05')




# Task 8

# KDE plots 

import requests
import matplotlib.pyplot as plt
import seaborn as sns


# Function for burglary kde plot
def burglary_kde_plot(crime_name, neighborhoods, date, month):
    for neighborhood, coords in neighborhoods.items():
        
        # General crime type link for burglary and robbery 
        crimetype_url = f"https://data.police.uk/api/crimes-street/{crime_name}?lat={coords['lat']}&lng={coords['lng']}&date={date}-{month}"

        # Requests data from URL
        response = requests.get(crimetype_url)

        # Checks if request was successful (status code 200)
        if response.status_code == 200:
            
            # Extracts coordinates based on given neighborhood details
            burglary_data = response.json()
            latitudes = [float(data['location']['latitude']) for data in burglary_data]
            longitudes = [float(data['location']['longitude']) for data in burglary_data]

            # Creates a scatter plot of burglary crimes for every negiborhood below
            plt.figure(figsize=(10, 8))
            sns.kdeplot(data=burglary_data, x=longitudes, y=latitudes, fill=True, label=f'{neighborhood} - {date}-{month}')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.title(f'{crime_name} kde plot in neighborhood')
            plt.legend()
            plt.show()
        else:
            print(f"Error: Unable to fetch data for neighborhood. Status Code: {response.status_code}")

# Details of coordinates for the 5 neighborhoods
neighborhoods = {
    'Peckham': {'lat': 51.474254702682, 'lng': -0.077405447747295},
    'Bexleyheath': {'lat': 51.452674492684, 'lng': 0.13737750812627},
    'West ham': {'lat': 51.531308081133, 'lng':0.017579512291011},
    'Golders Green': {'lat':51.589778519051, 'lng':-0.19980069833419},
    'King Cross': {'lat':51.541143286328, 'lng':-0.12506277440316}
}

# Returns burglary scatter plot and makes a scatter plot for each of the 5 neighborhoods

burglary_kde_plot('burglary', neighborhoods, 2023, '05')





import requests
import matplotlib.pyplot as plt
import seaborn as sns


# Function for robbery kde plot
def robbery_kde_plot(crime_name, neighborhoods, date, month):
    for neighborhood, coords in neighborhoods.items():
        
        # General crime type link for burglary and robbery 
        crimetype_url = f"https://data.police.uk/api/crimes-street/{crime_name}?lat={coords['lat']}&lng={coords['lng']}&date={date}-{month}"

        # Requests data from URL
        response = requests.get(crimetype_url)

        # Checks if request was successful (status code 200)
        if response.status_code == 200:
            
            # Extracts coordinates based on given neighborhood details
            robbery_data = response.json()
            latitudes = [float(data['location']['latitude']) for data in robbery_data]
            longitudes = [float(data['location']['longitude']) for data in robbery_data]

            # Creates a scatter plot of burglary crimes for every neighborhood below
            plt.figure(figsize=(10, 8))
            sns.kdeplot(data=robbery_data, x=longitudes, y=latitudes, fill=True, label=f'{neighborhood} - {date}-{month}')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.title(f'{crime_name} kde plot in neighborhood')
            plt.legend()
            plt.show()
        else:
            print(f"Error: Unable to fetch data for neighborhood. Status Code: {response.status_code}")

# Details of coordinates for the 5 neighborhoods
neighborhoods = {
    'Peckham': {'lat': 51.474254702682, 'lng': -0.077405447747295},
    'Bexleyheath': {'lat': 51.452674492684, 'lng': 0.13737750812627},
    'West ham': {'lat': 51.531308081133, 'lng':0.017579512291011},
    'Golders Green': {'lat':51.589778519051, 'lng':-0.19980069833419},
    'King Cross': {'lat':51.541143286328, 'lng':-0.12506277440316}
}

# Returns burglary scatter plot and makes a scatter plot for each of the 5 neighborhoods

robbery_kde_plot('robbery', neighborhoods, 2023, '05')

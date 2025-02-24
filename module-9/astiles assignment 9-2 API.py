"""
Name: Andrew Stiles
Date: 2-23-2025
Assignment: Module 9.2 Assignment
Purpose: API
Citation: N/A
"""

import requests

""" 
# Google Request
response = requests.get("http://www.google.com")
print("Status Code:", response.status_code)


# Astros Astronaut Data Request
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

print("Status Code:", response.status_code)  # Print response status
print("\nRaw JSON Response:")
print(response.json())  # Print unformatted JSON response



# Astros Astronaut Data Request Formatted
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()  # Convert response to JSON

print("\nNumber of Astronauts in Space:", data["number"])

print("\nList of Astronauts:")
for person in data["people"]:
    print(f"- {person['name']} on {person['craft']}") """

# Random User Request Raw, Then Formatted

URL = "https://randomuser.me/api/"

# Test API Connection
response = requests.get(URL)

if response.status_code == 200:
    print("Successfully connected to Random User API!\n")
else:
    print(f"API connection failed! Status Code: {response.status_code}")
    exit()  # Stop execution if API request fails

# Print raw response
data = response.json()
print("\nRaw JSON Response from API:")
print(data)

# Extract relevant user data
print("\nFormatted User Data:")
user = data["results"][0]
name = f"{user['name']['first']} {user['name']['last']}"
gender = user["gender"].capitalize()
email = user["email"]
city = user["location"]["city"]
country = user["location"]["country"]
age = user["dob"]["age"]

print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Location: {city}, {country}")

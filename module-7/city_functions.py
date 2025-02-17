"""
Name: Andrew Stiles
Date: 2-16-2025
Assignment: Assignment 7-2 "City Functions"
Purpose: City Functions - Formatting city, country, population, and language
Citation: N/A
"""

def city_country(city, country, population=None, language=None):
    """
    This function takes a city and country as required arguments and optionally 
    includes population and language. It returns a formatted string.
    """

    # Base format: "City, Country"
    formatted_string = f"{city.title()}, {country.title()}"

    # If population is provided, append it to the string
    if population:
        formatted_string += f" - population {population}"

    # If language is provided, append it to the string
    if language:
        formatted_string += f", {language.title()}"

    return formatted_string


# Run the function with different arguments to test output
if __name__ == "__main__":
    # Test with just city and country
    print(city_country("santiago", "chile"))

    # Test with city, country, and population
    print(city_country("santiago", "chile", 4837295))

    # Test with city, country, population, and language
    print(city_country("santiago", "chile", 4837295, "spanish"))

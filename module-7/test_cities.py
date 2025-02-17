"""
Name: Andrew Stiles
Date: 2-16-2025
Assignment: Assignment 7-2 "Test Cities"
Purpose: Unit Test for City Functions
Citation: N/A
"""

import unittest  # Import the unittest module for testing
from city_functions import city_country  # Import the function to be tested

class TestCityCountryFunction(unittest.TestCase):
    """
    This test class contains multiple test cases to verify the correct 
    formatting of the city_country function.
    """

    def test_city_country(self):
        ## Test to check if the function correctly formats a city and country.
        formatted = city_country("santiago", "chile")
        self.assertEqual(formatted, "Santiago, Chile")

    def test_city_country_population(self):
        ## Test to check if the function correctly formats city, country, and population.
        formatted = city_country("santiago", "chile", 4837295)
        self.assertEqual(formatted, "Santiago, Chile - population 4837295")

    def test_city_country_population_language(self):
        ## Test to check if the function correctly formats city, country, population, and language.
        formatted = city_country("santiago", "chile", 4837295, "spanish")
        self.assertEqual(formatted, "Santiago, Chile - population 4837295, Spanish")


# Run
if __name__ == "__main__":
    unittest.main()

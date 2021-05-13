#Name: Michael Moyo
#Lab: lab assignment 3, sorting it all out
#Purpose: using python to sort out data
#Date: 15/05/2019

from city import City
from quick_sort import*

in_file = open("world_cities.txt", "r") #Opens the files containing original city information.
alpha_file = open("cities_alpha.txt", "w") #Opens new file where cities will be printed alphabetically.
population_file = open("cities_population.txt", "w") #Opens new file where cities will be printed in order of increasing population
latitude_file = open("cities_latitude.txt", "w") #Opens new file where cities will be printed relative to their latitudes.

city_data_list = [] #List that will contain cities' data

for city in in_file: #loops through every line in the original file, world_cities.txt.

    city_data_raw = city.strip("\n") #Strips off all blanks lines at the ends of the strings

    city_data1 = city_data_raw.split(",") #Separates all information in the strings into components of a list

    cities_objects = City(city_data1[0], city_data1[1], city_data1[2], city_data1[3], city_data1[4],city_data1[5]) #Creates objects with the six necessary parameters

    city_data_list.append(cities_objects) #adds the objects into the city_data_list

def compare_names(city1,city2): #returns True if name of city1 is greater than or equal to name of city2

    return city1.name.upper() >= city2.name.upper()

sort(city_data_list, compare_names) #a call to sort the city_data_list into city names arranged in alphabetical order.

for cities in city_data_list:

    alpha_file.write(str(cities) + "\n") #writes down the alphabetically arranged city names and data in the new file "cities_alpha.txt."

def compare_populations(city1, city2): #returns True if the population of city2 is greater than or equal to population of city1.

    return city2.population >= city1.population

sort(city_data_list, compare_populations) #a call to sort the city_data_list into cities arranged in increasing population order.

for cities in city_data_list:

    population_file.write(str(cities) + "\n") ##writes down the "increasing population" arranged cities and data in the new file "cities_population.txt."

def compare_latitudes(city1, city2): #returns True if the latitude of city1 is greater than or equal to latitude of city2.

    return city1.latitude >= city2.latitude

sort(city_data_list, compare_latitudes) #a call to sort the city_data_list into cities arranged in increasing latitude order.

for cities in city_data_list:

    latitude_file.write(str(cities) + "\n")  ##writes down the "increasing latitude" arranged cities and data in the new file "cities_latitude.txt."


#closing all open files
latitude_file.close()
population_file.close()
alpha_file.close()
in_file.close()



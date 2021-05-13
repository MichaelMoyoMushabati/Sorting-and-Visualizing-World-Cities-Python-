
#Name: Michael Moyo
#Lab: lab assignment 3, sorting it all out
#Purpose: using python to sort out data
#Date: 15/05/2019

world_cities = open("world_cities.txt", "r")

#city_populations = open("cities_population.txt", "r")

from cs1lib import*
from quick_sort import*
from city import City

limit = 50 #number of cities to be drawn


def blank_world_map():

    image = load_image("world.png")

    draw_image(image, 0, 0)

city_data_list = []

for city in world_cities:

    city_data_raw = city.strip("\n")  # Strips off all blanks lines at the ends of the strings

    city_data_split = city_data_raw.split(",") #splits the strings in world_cities into their components

    city_data = City(city_data_split[0], city_data_split[1], city_data_split[2], city_data_split[3], city_data_split[4], city_data_split[5]) #Creates city objects with the six necessary parameters

    city_data_list.append(city_data) #adds the objects into the city_data_list


def compare_population(city1, city2): #returns True if population of city1 is greater than or equal to name of city2

    return city1.population <= city2.population

sort(city_data_list, compare_population) #a call to sort the city_data_list into cities arranged in increasing population order.

drawn = True
count = 0 #initial value of count

def draw():
    global count, drawn


    if drawn: #only draws the world map when drawn is True

        blank_world_map()

        drawn = False

    if count <= limit: #stops when count (number of drawn squares) == limit

        city_data_list[count].draw() #draws the squares on the world map

        count += 1

world_cities.close()

start_graphics(draw, height = 360, width = 720, framerate = 10)
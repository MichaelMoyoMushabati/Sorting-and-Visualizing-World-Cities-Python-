#Name: Michael Moyo
#Lab: lab assignment 3, sorting it all out
#Purpose: using python to sort out data
#Date: 15/05/2019

from cs1lib import*
class City:

    def __init__(self, code, name, region, population, latitude, longitude): #Initiates the class City with instance variables

        self.name = name #City name
        self.population = float(population) #city population in float format
        self.latitude = float(latitude) #city latitude in float format
        self.longitude = float(longitude) #city longitude in float format
        self.code = code #city code
        self.region = region #city region

    def __str__(self): #Generates the four printed strings, describing a city's name, population, latitude, and longitude

        return str(self.name) + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)


    def draw(self): #draws the squares, indicating the cities' locations on the map

        X_CENTER = 360 #Horizontal center of the map

        Y_CENTER = 180 #Vertical center of the map

        set_stroke_width(2)
        set_fill_color(1, 165/255, 0) #Orange color of the squares
        draw_rectangle((self.longitude + Y_CENTER)*2, (X_CENTER - (self.latitude + 90)*2), 10, 10) #sizes of each squares = 10 x 10
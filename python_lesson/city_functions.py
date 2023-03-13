def city_country(city, country, population=""):
    """ A City Inside a Country """ 
    places = {} 
    if population:
        places[city] = country
        places['population'] = population
        for cities, countries in places.items(): 
            place = (cities + ", " + countries + " - " + "population " +
            str(places['population'])) 
            return place
    else:
        places[city] = country 
        for cities, countries in places.items(): 
            place = cities + ", " + countries
            return place.title()

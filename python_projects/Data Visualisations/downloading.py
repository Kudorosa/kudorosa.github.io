import json 
from pygal.maps.world import COUNTRIES
from country_codes import retrieve_country_code
import pygal
from pygal.style import LightColorizedStyle as Ls, RotateStyle as Rs
import csv

place = "data/population_data.json"
with open(place) as file_object:
    population = json.load(file_object) 

country_inhabitants = {}     
for info in population:
    if info["Year"] == "2010":
        country = info["Country Name"]
        inhabitants = int(float(info["Value"]))
        code = retrieve_country_code(country)
        if code:
            country_inhabitants[code] = inhabitants
        else: 
            pass
       
            
        
      
c_inhabs_low, c_inhabs_med, c_inhabs_high = {}, {}, {}      
for c, inhabs in country_inhabitants.items():
    if inhabs < 10000000:
        c_inhabs_low[c] = inhabs
    elif inhabs < 1000000000:
        c_inhabs_med[c] = inhabs
    else:
        c_inhabs_high[c] = inhabs

print(len(c_inhabs_low),len(c_inhabs_med),len(c_inhabs_high)) 

for c_code in sorted(COUNTRIES.keys()):
    print(f"{c_code} |-| {COUNTRIES[c_code]}")     

wmap = pygal.maps.world.World()
wmap.title = "North America, Central America and South America"
wmap.add("North America",["ca","mx","us"])
wmap.add("Central America",["bz","cr","gt","hn","ni","pa","sv"])
wmap.add("South America",["ar","bo","br","cl","co","ec","gf","gy","pe","py",
"sr","uy","ve"])

wmap.render_to_file("America, Land of the Free.svg") 

wm = pygal.maps.world.World()
wm.title = "The Population of America!"
wm.add("North America",{"ca": 34126000, "us": 309349000, "mx":113423000})

wm.render_to_file("Population Count of North America (NA).svg") 

w = pygal.maps.world.World()
w_style = Rs("#224466", base_style=Ls)
w = pygal.maps.world.World(style=w_style)
w.title = "Inhabitants of the Different Countries (2010)"
w.add("0 - 10M",c_inhabs_low)
w.add("10M - 1B",c_inhabs_med) 
w.add("1B+",c_inhabs_high) 

w.render_to_file("Population Count of the Different Countries..svg")

#Test V------------------------------

countries_wealth = "data/gdp.json"
with open(countries_wealth) as file_object:
    h = json.load(file_object)
    
country_wealth = {} 
for information in h:
    if information["Year"] == 2016:
        country = information['Country Name']
        gross_income = int(float(information['Value']))
        code = retrieve_country_code(country)
        if code:
            country_wealth[code] = gross_income
        else: 
            pass

poor, average, rich = {}, {}, {}
for country, money in country_wealth.items():
    if money < 10000000000:
        poor[country] = money
    elif money < 1000000000000:
        average[country] = money
    else:
        rich[country] = money
        
wgdp = pygal.maps.world.World() 
wgdp_style = Rs("#334455", base_style=Ls)
wgdp = pygal.maps.world.World(style=wgdp_style)
wgdp.title = "Countries Gross Domestic Product ($)"
wgdp.add("0 - $100B", poor)
wgdp.add("$100B - $1T", average)
wgdp.add("$1T+", rich)

wgdp.render_to_file("Rich and Poor Countries around the World.svg")



import json 
from pygal.maps.world import COUNTRIES
import unittest

other_countries = {
'ye':"Yemen, Rep.",
'cg':"Congo, Dem. Rep.",
'do':"Dominican Republic",
'eg':"Egypt, Arab Rep.",
'gm':"Gambia",
'hk':"Hong Kong SAR, China",
'ir':"Iran, Islamic Rep.",
'kp':"Korea, Dem. Rep.",
'kr':"Korea, Rep.",
'kg':"Kyrgyz Republic",
'la':"Lao PDR",
'ly':"Libya",
'mo':"Macao SAR, China",
'md':"Macedonia, FYR",
'mo':"Moldova",
'sk':"Slovak Republic",
'tz':"Tanzania",
've':"Venezuela, RB",
}


def retrieve_country_code(country):
    """ Getting a Country's Code """ 
    
    for code, name in COUNTRIES.items():
        if name == country:
            return code
    
    for code, name in other_countries.items():
        if name == country:
            return code




        
    


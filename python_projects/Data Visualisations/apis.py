import requests 
import pygal
from pygal.style import LightColorizedStyle as Lcs, LightenStyle as Ls
import unittest

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
#Create an Application Programming Interface call and store the Output.
req = requests.get(url)
print("|current_status_code|:",req.status_code)

#Storing the Application Programming Interface into a Variable. 
output_dictionary = req.json() 

#--- Processing --- 
print("Repository Amount:", output_dictionary["total_count"]) 
repository_dictionaries = output_dictionary["items"]
print("Returned Repositories:", len(repository_dictionaries))


repository_dictionary = repository_dictionaries[0]
names, plot_dicts = [], []
for repository_dictionary in repository_dictionaries:
    names.append(repository_dictionary["name"])
    
    plot_dict = {
        'value': repository_dictionary["stargazers_count"],
        'label': repository_dictionary["description"],
        'xlink': repository_dictionary["html_url"],
        }
    plot_dicts.append(plot_dict)
    

my_creation = Ls("#776655", base_style=Lcs)
configuration = pygal.Config()
configuration.x_label_rotation = 45
configuration.show_legend = False
configuration.title_font_size = 14
configuration.major_label_font_size = 20
configuration.label_font_size = 14
configuration.truncate_label = 15
configuration.show_y_guides = False
configuration.width = 1000

chart = pygal.Bar(configuration, style=my_creation)
chart.title = "Github's Most Favourited Projects!"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file("Top Github Projects.svg")

class Test(unittest.TestCase): 
    """ Testing if our Code Works """ 
    def test_apis(self): 
        """ """ 
        a = req.status_code
        b = 200 
        self.assertEqual(a, b)
    
    def test_expected_repos(self): 
        """ Testing to see if the Repositories a Returned """ 
        a = repository_dictionaries
        self.assertTrue(len(a) == 30)
    
    def test_total_repos(self): 
        """ """ 
        a = output_dictionary['total_count']
        self.assertTrue(a > 945000) 

unittest.main()




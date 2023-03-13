import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as Lcs, LightenStyle as Ls

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
re = requests.get(url) 
print("Status:",re.status_code) 

submissions = re.json() 
submission_dictionaries = []
plot_dicts, names = [], []
for submission in submissions[:30]: 
    #Create an Application Programming Interface call for individual Submissions.
    url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submission) 
        + ".json")
    submissioned = requests.get(url)
    
    output_dictionary = submissioned.json()
    
    submission_dictionary = {
        'title': output_dictionary["title"], 
        'link': "http://news.ycombinator.com/item?id=" + str(submission),
        'comments': output_dictionary.get('descendants', 0) 
        }
    submission_dictionaries.append(submission_dictionary) 
    
submission_dictionaries = sorted(submission_dictionaries,
key=itemgetter('comments'), reverse=True)

for submission_dictionary in submission_dictionaries:
    names.append(submission_dictionary["title"])
    
    plot_dict = {
        'label': submission_dictionary["title"],
        'xlink': submission_dictionary["link"],
        'value': submission_dictionary["comments"],
        }
    plot_dicts.append(plot_dict)
    

#Test V-------------------------------------

my_style = Ls("#349120", base_style=Lcs) 
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False) 
chart.title = "Top Hackernews Articles."
chart.x_labels = names
chart.add("", plot_dicts)
chart.render_to_file("Hackernews Articles.svg")


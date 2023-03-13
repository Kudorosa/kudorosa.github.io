import pygal
from pygal.style import LightColorizedStyle as Lcs, LightenStyle as Ls

the_style = Ls("#451241", base_style=Lcs) 
chart = pygal.Bar(style=the_style, x_label_rotation=45, show_legend=False) 
chart.title = "Github Python's Best!"
chart.x_labels = ["httpie", "django", "flask"]

plot_dicts = [
    {'value': 16101, 'label': "Description of Httpie."},
    {'value': 15028, 'label': "Description of Django."},
    {'value': 14798, 'label': "Description of Flask."},
    ]

chart.add("", plot_dicts) 
chart.render_to_file("Github Pythons Projects.svg") 

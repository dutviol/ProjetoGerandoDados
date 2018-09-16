import requests
import pygal
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS


# Faz a chamada da API
url = 'http://api.github.com/search/repositories?q=language:python&sort=starts'
r = requests.get(url)
print('Status code: ', r.status_code)

# Armazena a resposta em variável

response_direct = r.json()
print("Total Repositories: ", response_direct['total_count'])


# Explorar informações sobre os repositórios
repo_dicts = response_direct['items']

names, plot_dicts, stars = [], [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {'value': repo_dict['stargazers_count'], 
                 'label':repo_dict['description'],}
    plot_dicts.append(plot_dict)
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)

chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars) # verificar por que não funciona passando plot_dict
chart.render_to_file('arquivos/python_repos.svg')



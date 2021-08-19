import pywebcopy
from pywebcopy import save_website
pywebcopy.config['bypass_robots'] = True
kwargs = {'project_name': 'IslamQA'}

save_website(
    url='https://islamqa.info/en',
    project_folder='D:\IslamQA',
    **kwargs
)

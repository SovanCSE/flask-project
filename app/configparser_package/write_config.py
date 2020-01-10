from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {'secret_key': 12345}
config['settings']['debug'] = 'True'
config['settings']['log_path'] = 'app/file.log'

config.add_section('db')
config.set('db','db_name', 'prod_db')
config.set('db','db_host', 'localhost')
config.set('db','db_port', '8080')

config['files'] = {
    'usr_cdn': False,
    'image_path': 'image/img.png'
}

config['main settings'] = {
    "setting.dev": True,
    'setting.prod': False
}
config['main settings']['server_timeout'] = '2'


with open('config.ini', 'w') as fileObj:
    config.write(fileObj)
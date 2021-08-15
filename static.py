import os
import sys

from six.moves import configparser

SETTINGS = {}

def get_settings():
    сonf_path = os.path.abspath(os.getenv('CONF', ''))

    if not сonf_path or not os.path.isfile(сonf_path):
        sys.exit('Could not find configuration file')

    parser = configparser.ConfigParser()
    parser.read(сonf_path)

    SETTINGS['DEBUG'] = parser.getboolean('manual settings', 'debug')
    SETTINGS['GROUPS'] = parser.getboolean('manual settings', 'groups')
    SETTINGS['PROXIES'] = parser.get('manual settings', 'proxies').split(',')
    SETTINGS['IS_TARGET'] = parser.getboolean('manual settings', 'target_specified')
    SETTINGS['TARGET'] = str(parser.get('manual settings', 'target')).split(',')
    SETTINGS['OWNER'] = str(parser.get('manual settings', 'owner'))

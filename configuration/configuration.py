__author__ = "Matthew Kidza-Griffiths"
__copyright__ = "Copyright 2007, Swiftly.org"
__credits__ = ["Matthew Kidza-Griffiths", "Jon Gosier"]
__license__ = "LGPL"
__version__ = "0.0.1"
__maintainer__ = "Matthew Kidza-Griffiths"
__email__ = "mg@swiftly.org"
__status__ = "Development"


from ConfigParser import ConfigParser
from environment import ENV
import sys
import os
import re

def get_config(environment):
    config_dir = "%s/%s" % (re.sub('configuration\.(pyc|py)', '', os.path.abspath(__file__)), environment)
    config_files = os.listdir(config_dir)
    config_files = ["%s/%s" % (config_dir, file_name) for file_name in config_files]
    configuration = ConfigParser()
    configuration.read(config_files)
    return configuration

config = get_config(ENV)


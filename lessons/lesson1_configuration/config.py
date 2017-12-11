# print working directory to confirm we are in the ml_guild dir
pwd

# view the files to confirm the raw_data dir exists
ls

# view the directories and files inside the raw_data dir
ls raw_data

# change directory into the configuration_files folder
cd raw_data/configuration_files

# confirm we are in the correct dir
pwd

# list the directories and files
ls

# cd in aws_config_files_1
cd aws_config_files_1

# list the directories and files
ls 


# https://docs.python.org/2/library/configparser.html
import configparser

# instantiate config parser
config = configparser.ConfigParser()

# read a config file
config.read('config1.ini')


# store config values
# config uses dict syntax to store values
REGION = config['default']['region']
OUTPUT = config['default']['region']
AWS_ACCESS_KEY_ID = config['keys']['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = config['keys']['aws_secret_access_key']


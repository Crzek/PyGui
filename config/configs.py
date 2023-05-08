import configparser
import os

CONFIGFile = "./config/config.ini"

current_directory = os.path.abspath(CONFIGFile)
# configFilePATH = os.path.join(current_directory, CONFIG)

print(current_directory)
# print(configFilePATH)
config = configparser.ConfigParser()
config.read(CONFIGFile)

data_dir = config['PATHS']["data_dir"]
files_save = config['PATHS']['save_files']

print(data_dir)
print(files_save)


def get_config():
    return {'data_dir': data_dir, 'files_save': files_save}

import shutil
import urllib.request
import zipfile
import os


path='D:/28_GitHub/Inception V3'

download_dir = path+'/tmp/'
if not (os.path.exists(download_dir)):
    os.mkdir(download_dir)

data_url = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip"
data_file_name = "catsdogs.zip"
urllib.request.urlretrieve(data_url, data_file_name)
zip_ref = zipfile.ZipFile(data_file_name, 'r')
zip_ref.extractall(download_dir)
zip_ref.close()

print("Number of cat images:",len(os.listdir(path+'/tmp/PetImages/Cat/')))
print("Number of dog images:", len(os.listdir(path+'/tmp/PetImages/Dog/')))

#Creating Train-Test-Split Directories

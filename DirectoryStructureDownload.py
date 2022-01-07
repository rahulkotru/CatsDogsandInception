import shutil
import urllib.request
import zipfile
import os
import random

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
try:
    os.mkdir(path+'/tmp/cats-v-dogs')
    os.mkdir(path+'/tmp/cats-v-dogs/training')
    os.mkdir(path+'/tmp/cats-v-dogs/testing')
    os.mkdir(path+'/tmp/cats-v-dogs/training/cats')
    os.mkdir(path+'/tmp/cats-v-dogs/training/dogs')
    os.mkdir(path+'/tmp/cats-v-dogs/testing/cats')
    os.mkdir(path+'/tmp/cats-v-dogs/testing/dogs')
except OSError:
    pass

def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    files = []
    for filename in os.listdir(SOURCE):
        file = SOURCE + filename
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + " is zero length, so ignoring.")

    training_length = int(len(files) * SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[training_length:]

    for filename in training_set:
        this_file = SOURCE + filename
        destination = TRAINING + filename
        shutil.copyfile(this_file, destination)

    for filename in testing_set:
        this_file = SOURCE + filename
        destination = TESTING + filename
        shutil.copyfile(this_file, destination)

CAT_SOURCE_DIR = path+"/tmp/PetImages/Cat/"
TRAINING_CATS_DIR = path+"/tmp/cats-v-dogs/training/cats/"
TESTING_CATS_DIR = path+"/tmp/cats-v-dogs/testing/cats/"
DOG_SOURCE_DIR = path+"/tmp/PetImages/Dog/"
TRAINING_DOGS_DIR = path+"/tmp/cats-v-dogs/training/dogs/"
TESTING_DOGS_DIR = path+"/tmp/cats-v-dogs/testing/dogs/"

split_size = .9
split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)
split_data(DOG_SOURCE_DIR, TRAINING_DOGS_DIR, TESTING_DOGS_DIR, split_size)

print("Number of training cat images", len(os.listdir(path+'/tmp/cats-v-dogs/training/cats/')))
print("Number of training dog images", len(os.listdir(path+'/tmp/cats-v-dogs/training/dogs/')))
print("Number of testing cat images", len(os.listdir(path+'/tmp/cats-v-dogs/testing/cats/')))
print("Number of testing dog images", len(os.listdir(path+'/tmp/cats-v-dogs/testing/dogs/')))

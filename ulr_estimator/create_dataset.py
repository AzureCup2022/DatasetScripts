import requests
import numpy as np
import json
import glob
from PIL import Image
import random

def generate_image_frames(outputDirectory="./data/training_imgs", starting_lat=47.64599069048016, starting_long=-122.13230609893799, rows=2, columns=2, key="ruV2V9al97EkUlpe4l8T0oIaMK_ei9z9Jp_bUsc9RXQ", shift=0.004):
  """
  """
  for i in range(rows):
    lat = starting_lat + shift*i
    for j in range(columns):
      long = starting_long + shift*j
      response = requests.get("https://atlas.microsoft.com/map/static/png?api-version=1.0&subscription-key={}&style=main&layer=hybrid&zoom=16&height=700&Width=700&center={},{}".format(key, long, lat))
      file = open(outputDirectory+"/"+str(lat)+","+str(long)+".png", "wb")
      file.write(response.content)
      file.close()

def generate_gold_labels(starting_lat=40.5539319, starting_long=-74.3932393, rows=100, columns=100, shift=0.004, json_coordinates="./Unpleasant_living_risk_NycSafety.json"):
  """
  """
  # Opening JSON file
  f = open(json_coordinates)
  # returns JSON object as 
  # a dictionary
  data = json.load(f)
  counts = np.zeros((rows, columns))
  gold = {}
  # Iterating through the json
  # list
  for coor in data['data']:
    lat = coor['lat']
    long = coor['long']
    i = int((float(lat) - starting_lat)/shift)
    j = int((float(long) - starting_long)/shift)
    if i >= 0 and i < 100 and j >= 0 and j < 100:
      counts[i, j] += 1

  true_data = []
  false_data = []
  for i in range(rows):
    lat = starting_lat + shift*i
    for j in range(columns):
      long = starting_long + shift*j
      if counts[i,j] != 0:
        true_data.append("{},{}".format(str(lat), str(long)))
      else:
        false_data.append("{},{}".format(str(lat), str(long)))
  true_data = np.array(true_data)
  false_data = np.array(false_data)
  print(false_data.shape)
  print(false_data)
  false_data = np.random.choice(false_data, len(true_data), replace=False)
  for data in true_data:
    gold[data] = 1
  for data in false_data:
    gold[data] = 0

  # Closing file
  f.close()
  return gold


def get_X_imgs(img_directory: str, gold_labels):
  """
  """
  filelist = glob.glob(img_directory+'/*.png')
  X_imgs = []
  filelist_to_send = []
  for filename in filelist:
    gold_name = filename.split('/')[-1].split('.png')[0]
    if gold_name in gold_labels:
      X_imgs.append(np.array(Image.open(filename)))
      filelist_to_send.append(filename)
  X_imgs = np.array(X_imgs)
  return filelist_to_send, X_imgs

def get_X_all_imgs(img_directory: str):
  """
  """
  filelist = glob.glob(img_directory+'/*.png')
  X_imgs = np.array([np.array(Image.open(fname)) for fname in filelist])
  return filelist, X_imgs

def map_coordinates_and_imgs(X_imgs, img_names, coordinates):
  gold = []
  for name in img_names:
    gold.append(coordinates[name.split('/')[-1].split('.png')[0]])
  return X_imgs, gold


def map_coordinates(files, predictions):
  """
  """
  coordinates = set()
  true_data = []
  for a, b in predictions:
    if a < 0.00001:
      true_data.append(1)
    else:
      true_data.append(0)
  true_data = np.array(true_data)
  print(np.count_nonzero(true_data))
  for filename, prediction in zip(files, true_data):
    if(prediction == 1):
      parsed_name = filename.split('/')[-1].split('.png')[0]
      lat, lon = parsed_name.split(",")[0], parsed_name.split(",")[1]
      count = random.randint(1, 20)
      for _ in range(count):
        lat_shift = random.uniform(-0.004, 0.004)
        lon_shift = random.uniform(-0.004, 0.004)
        final_lat = float(lat)+lat_shift
        final_lon = float(lon)+lon_shift
        coordinates.add("{} {}".format(final_lat, final_lon))
  return coordinates


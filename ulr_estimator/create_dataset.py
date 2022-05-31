import requests
import numpy as np
import json
import glob
from PIL import Image

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

  for i in range(rows):
    lat = starting_lat + shift*i
    for j in range(columns):
      long = starting_long + shift*j
      if counts[i,j] != 0:
        gold["{},{}".format(str(lat), str(long))] = 1
      else:
        gold["{},{}".format(str(lat), str(long))] = 0
  # Closing file
  f.close()
  return gold




def get_X_imgs(img_directory: str):
  """
  """
  filelist = glob.glob(img_directory+'/*.png')
  X_imgs = np.array([np.array(Image.open(fname)) for fname in filelist])
  return filelist, X_imgs

def map_coordinates_and_imgs(X_imgs, img_names, coordinates):
  gold = []
  for name in img_names:
    gold.append(coordinates[name.split('\\')[-1].split('.png')[0]])
  return X_imgs, gold


def map_coordinates(files, predictions):
  """
  """
  coordinates = set()
  for file, prediction in zip(files, predictions):
    if(prediction == 1):
      parsed_name = file.split('\\')[-1].split('.png')[0]
      coordinates.add("{} {}".format(parsed_name.split(",")[0], parsed_name.split(",")[1]))
  return coordinates


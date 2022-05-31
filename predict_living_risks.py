import argparse
from asyncio.log import logger
import logging
from pyexpat import model
import sys
from ulr_estimator.create_dataset import generate_image_frames, get_X_imgs, map_coordinates

from ulr_estimator.model import ulr_model
from utils.output_generators import generate_jsonfile
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("--model_path", default="./models/model.ulr", type=str, help="The path to the model that predicts cities.")
parser.add_argument("--starting_lat", default=40.5539319, type=float, help="Starting lat, the left bottom corner.")
parser.add_argument("--starting_long", default=-74.3932393, type=float, help="Starting long, the left bottom corner.")
parser.add_argument("--number_of_rows", default=50, type=int, help="Number of frames in column")
parser.add_argument("--number_of_columns", default=50, type=int, help="Number of frames in row")


TEMP_IMG_DIRECTORY="./data/predicting_imgs"

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    model = ulr_model()
    model.load(args.model_path)
    logging.info("The model was successfully loaded.")
    generate_image_frames(outputDirectory=TEMP_IMG_DIRECTORY, starting_lat=args.starting_lat, starting_long=args.starting_long, rows=args.number_of_rows, columns=args.number_of_columns)
    filelist, imgs = get_X_imgs(args.imgs_directory)
    predictions = model.predict(imgs)
    logging.info("The prediction was successfully generated.")
    coordinates = map_coordinates(filelist, predictions)
    generate_jsonfile("ulr_prediction", coordinates)
    logging.info("The prediction was successfully printed into json file and coordinates are ready to upload.")
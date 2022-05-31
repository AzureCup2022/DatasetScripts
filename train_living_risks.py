import argparse
import logging
import sys
from ulr_estimator.create_dataset import generate_image_frames, map_coordinates_and_imgs, generate_gold_labels, get_X_imgs
from ulr_estimator.model import ulr_model
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("--model_path", default="./models/model.ulr", type=str, help="The path of the model that is going to be trained.")
parser.add_argument("--json_safety_coordinates", default="./Unpleasant_living_risk_NycSafety.json", type=str, help="Starting lat, the left bottom corner.")
parser.add_argument("--imgs_directory", default="./data/training_imgs", type=str, help="Starting long, the left bottom corner.")
parser.add_argument("--number_of_rows", default=100, type=int, help="Number of frames in column")
parser.add_argument("--number_of_columns", default=100, type=int, help="Number of frames in row")
parser.add_argument("--starting_lat", default=40.5539319, type=float, help="Starting lat, the left bottom corner.")
parser.add_argument("--starting_long", default=-74.3932393, type=float, help="Starting long, the left bottom corner.")



if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    # Generate Training Dataset
    generate_image_frames(outputDirectory=args.imgs_directory, starting_lat=args.starting_lat, starting_long=args.starting_long, rows=args.number_of_rows, columns=args.number_of_columns)
    gold_labels = generate_gold_labels(starting_lat=args.starting_lat, starting_long=args.starting_long, rows=args.number_of_rows, columns=args.number_of_columns, json_coordinates=args.json_safety_coordinates)
    filelist, imgs = get_X_imgs(args.imgs_directory)
    X_imgs, X_labels = map_coordinates_and_imgs(imgs, filelist, gold_labels)
    logging.info("Data are successfully prepared.")
    model = ulr_model()
    model.train(X_imgs[0:9000], X_labels[0:9000], X_imgs[9000:10000], X_labels[9000:10000])
    logging.info("The model is successfully trained.")
    model.save(args.model_path)
    logging.info("The model is successfully saved.")


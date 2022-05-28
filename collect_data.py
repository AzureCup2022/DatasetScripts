import argparse
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


from utils.geoportal_collector import collect_geoportal_gmls, generate_geoportal_JSONs

parser = argparse.ArgumentParser()
parser.add_argument("--geoportal_folders", default=["./data/geoportalpraha/badatmosphere", "./data/geoportalpraha/noise", "./data/geoportalpraha/safety"], type=list, help="List of geoportalpraha data to collect.")
parser.add_argument("--thickening", default=1, type=float, help="ToDo: implement the thickening of points that heat map will be better visualize.")
parser.add_argument("--output_folder", default="./outputs", type=str, help="Path to the output dictionary path.")


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)

    collected_geoportal = collect_geoportal_gmls(args.geoportal_folders)
    logging.info('Geoportal data were successfuly collected!')
    generate_geoportal_JSONs(collected_geoportal)
    logging.info('JSONs of Geoportal data were successfuly generated!')
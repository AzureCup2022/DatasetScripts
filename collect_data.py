import argparse
import logging
import sys
from utils.azure_collector import collect_azure_coordinates
from utils.geoportal_collector import collect_geoportal_gmls, generate_geoportal_JSONs
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("--geoportal_folders", default=["./data/geoportalpraha/badatmosphere", "./data/geoportalpraha/noise", "./data/geoportalpraha/safety"], type=list, help="List of geoportalpraha data to collect.")
parser.add_argument("--azure_datasets", default=["BostonSafety", "ChicagoSafety", "SanFranciscoSafety", "NycSafety"], type=list, help="List of azure datasets to collect.")
parser.add_argument("--thickening", default=1, type=float, help="ToDo: implement the thickening of points that heat map will be better visualize.")
parser.add_argument("--geoportal", default=False, type=bool, help="Whether you want to collect geoportal data.")
parser.add_argument("--azure", default=True, type=bool, help="Whether you want to collect azure data.")


def collect_geoportal(args):
    """
    """
    collected_geoportal = collect_geoportal_gmls(args.geoportal_folders)
    logging.info('Geoportal data were successfuly collected!')
    generate_geoportal_JSONs(collected_geoportal)
    logging.info('JSONs of Geoportal data were successfuly generated!')


def collect_azure(args):
    """
    """
    collect_azure_coordinates(args.azure_datasets)
    

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    if args.geoportal:
        collect_geoportal(args)
    if args.azure:
        collect_azure(args)
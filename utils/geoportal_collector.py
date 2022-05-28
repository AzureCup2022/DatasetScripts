from utils.output_generators import generate_jsonfile
from utils.extractors import extractGMLCoordinates
import glob
import logging

def collect_geoportal_gmls(folders: list):
    """
    """
    collected_data = {}
    for folder in folders:
        name = folder.split('/')[-1]
        extracted_coordinates = set()
        for file in glob.glob(folder + '/*.gml'):
            extracted_coordinates = extracted_coordinates.union(extractGMLCoordinates(file))
            logging.info("The file {} was processed and the folder {} contains {} coordinates for now.".format(file, name, len(extracted_coordinates)))
        collected_data[name] = extracted_coordinates
    return collected_data
        


def generate_geoportal_JSONs(collected_data: dict):
    """
    """
    for name in collected_data:
        generate_jsonfile(name, collected_data[name])

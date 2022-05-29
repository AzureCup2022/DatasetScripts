import re

GML_POSLIST_PATTERN = re.compile(r'\<gml:posList\>([0-9. ]*)\<\/gml:posList\>')
GML_POS_PATTERN = re.compile(r'\<gml:pos\>([0-9. ]*)\<\/gml:pos\>')


def extractGMLCoordinates(gml_path: str):
    """
    """
    coordinates = []
    gml_file = open(gml_path, "r")
    gml_content = gml_file.read()
    for posList in re.findall(GML_POSLIST_PATTERN, gml_content):
        __parsePosList(posList, coordinates)
    for pos in re.findall(GML_POS_PATTERN, gml_content):
        coordinates.append(pos)
    return set(coordinates)

def __parsePosList(posList: str, coordinates: list):
    """
    """
    numbers = posList.split(' ')
    if len(numbers)%2 != 0:
        raise Exception("GML file coordinates are wrongly formated.")
    for i in range((int)(len(numbers)/2)):
        coordinates.append(numbers[2*i] + " " + numbers[2*i + 1])
    return coordinates
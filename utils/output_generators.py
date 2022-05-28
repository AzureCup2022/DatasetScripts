

from math import fabs


def generate_jsonfile(name: str, coordinates: set, color = "red", radius = 1, intensity = 1):
    """
    """
    final_json = ""
    final_json += "{\n"
    final_json += "\t\"name\": \"{}\",\n".format(name)
    final_json += "\t\"color\": \"{}\",\n".format(color)
    final_json += "\t\"data\": [\n"
    first = True
    for coor in coordinates:
        if first:
            first = False
        else:
            final_json += ",\n"
        final_json += "\t\t{\n"
        final_json += "\t\t\t\"long\": {},\n".format(coor.split(' ')[0])
        final_json += "\t\t\t\"lat\": {},\n".format(coor.split(' ')[1])
        final_json += "\t\t\t\"radius\": {},\n".format(radius)
        final_json += "\t\t\t\"intensity\": {}\n".format(intensity)
        final_json += "\t\t}"
    final_json += "\n"
    final_json += "\t]\n"
    final_json += "}"
    f = open(name+".json", "a")
    f.write(final_json)
    f.close()

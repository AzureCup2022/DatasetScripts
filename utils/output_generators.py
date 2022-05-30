

from math import fabs


def generate_jsonfile(name: str, coordinates: set, color = "red", radius = 1, intensity = 1):
    """
    """
    final_json = open(name+".json", 'a')
    final_json.write("{\n")
    final_json.write("\t\"name\": \"{}\",\n".format(name))
    final_json.write("\t\"color\": \"{}\",\n".format(color))
    final_json.write("\t\"data\": [\n")
    first = True
    for coor in coordinates:
        if first:
            first = False
        else:
            final_json.write(",\n")
        final_json.write("\t\t{\n")
        final_json.write("\t\t\t\"lat\": {},\n".format(coor.split(' ')[0]))
        final_json.write("\t\t\t\"long\": {},\n".format(coor.split(' ')[1]))
        final_json.write("\t\t\t\"radius\": {},\n".format(radius))
        final_json.write("\t\t\t\"intensity\": {}\n".format(intensity))
        final_json.write("\t\t}")
    final_json.write("\n")
    final_json.write("\t]\n")
    final_json.write("}")
    
    final_json.close()
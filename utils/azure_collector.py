from azureml.opendatasets import BostonSafety, ChicagoSafety, SanFranciscoSafety, NycSafety, SeattleSafety
from utils.output_generators import generate_jsonfile
from dateutil import parser
import logging


UNPLEASANT_LIVING_RISK_CATEGORIES = set(['Graffiti', 'Air Pollution Control', 'Consumer Affairs Issues', 'Water Issues', 'Generic Noise Disturbance', 
                                'Parking Complaints', 'Housing', 'Noise Disturbance', 'Needle Program', 'Abandoned Bicycle', 'Environmental Services', 
                                'Building', 'Traffic Signal Out Complaint', 'Graffiti Removal Request', 'Aircraft Noise Complaint', 'Water Quality Concern',
                                'Water On Street Complaint', 'Consumer Fraud Complaint', 'Street Light Out Complaint', 'Street Light Pole Damage Complaint', 
                                'Restaurant Complaint', 'Sanitation Code Violation', 'Vacant/Abandoned Building Complaint', 'Street Cleaning Request', 
                                'Weed Removal Request', 'Low Water Pressure Complaint', 'Sewer Cleaning Inspection Request', 'No Water Complaint',
                                'Building Violation', 'Alley Light Out Complaint', 'Abandoned Vehicle Complaint', 'Abandoned Vehicle', 'Graffiti',
                                'General Request - BUILDING INSPECTION', 'Streetlights', 'Damaged Property', 'Parking Enforcement', 'Potentially Life-Threatening',
                                'Residential Building Request', 'Alarm', 'Sewer Issues', 'Fire', 'Illegal Postings', 'Noise Report', 'Homeless Person Assistance',
                                'Mobile Food Vendor', 'Unsanitary Condition','Building/Use', 'Street Sign - Missing', 'Plumbing',  'Derelict Vehicles', 'HEAT/HOT WATER',
                                'Illegal Parking', 'Noise - Park', 'General Construction/Plumbing', 'Noise - Residential',  'Blocked Driveway', 'Sanitation Condition', 
                                'Noise', 'Ferry Inquiry', 'Homeless Encampment', 'PLUMBING', 'Indoor Sewage', 'Derelict Vehicle', 'Vending', 'Noise - Helicopter', 
                                'Abandoned Vehicle', 'PAINT/PLASTER','Sewer', 'For Hire Vehicle Complaint', 'Noise - Street/Sidewalk', 'Indoor Air Quality', 
                                'UNSANITARY CONDITION', 'WATER LEAK', 'Dirty Conditions', 'Missed Collection (All Materials)', 'Food Poisoning', 'Electronics Waste Appointment', 
                                'Noise - Vehicle', 'Street Light Condition', 'Air Quality', 'ELECTRIC','Lost Property', 'Graffiti', 'Consumer Complaint', 'Water Quality',  
                                'Violation of Park Rules', 'Water System', 'Broken Parking Meter', 'Drinking', 'Drug Activity', 'Street Condition', 'Noise - Commercial', 
                                'Standing Water'
                                ])

START_DATE = '2015-05-01'
END_DATE = '2022-01-01'


def collect_azure_coordinates(datasets, type = 'ULR'):
    """
    """
    for datasetName in datasets:
        if datasetName == 'BostonSafety':
            dataset = getBostonSafety()
        elif datasetName == 'ChicagoSafety':
            dataset = getChicagoSafety()
        elif datasetName == 'SanFranciscoSafety':
            dataset = getSanFranciscoSafety()
        elif datasetName == 'NycSafety':
            dataset = getNycSafety()
        elif datasetName == 'SeattleSafety':
            dataset = getSeattleSafety()
        if (type == 'ULR'):
            coordinates = collectULRCoordinates(dataset)
        logging.info("Coordinates of {} were downloaded and collected successfully! There are {} coordinates.".format(datasetName, len(coordinates)))
        generate_jsonfile('Unpleasant_living_risk_'+datasetName, coordinates)
        logging.info("The json file of {} was successfully generated!".format(datasetName))
            



def collectULRCoordinates(dataset, limit=1000000):
    """
    """
    coordinates = set()
    for index, row in dataset.iterrows():
        if row['category'] in UNPLEASANT_LIVING_RISK_CATEGORIES:
            coordinates.add("{} {}".format(row['latitude'], row['longitude']))
        if(len(coordinates) > limit):
            break
    return coordinates




def display_safety_dataset(dataset):
    """
    """
    uniqueCategory = set()
    uniqueSubcategory = set()
    for index, row in dataset.iterrows():
        uniqueCategory.add(row['category'])
        uniqueSubcategory.add(row['subcategory'])
        #if(row['category'] == 'Building'):
            #print(row['subcategory'])
        if index > 10000:
            break
    print(uniqueCategory)
    #print(uniqueSubcategory)


def getBostonSafety(since = START_DATE, to=END_DATE):
    """
    """
    start_date = parser.parse(since)
    end_date = parser.parse(to)
    safety = BostonSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()
    return safety

def getChicagoSafety(since = START_DATE, to=END_DATE):
    """
    """
    start_date = parser.parse(since)
    end_date = parser.parse(to)
    safety = ChicagoSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe() 
    return safety
    
def getSanFranciscoSafety(since = START_DATE, to=END_DATE):
    """
    """
    start_date = parser.parse(since)
    end_date = parser.parse(to)
    safety = SanFranciscoSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()
    return safety

def getNycSafety(since = START_DATE, to=END_DATE):
    """
    """
    start_date = parser.parse(since)
    end_date = parser.parse(to)
    safety = NycSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()
    return safety

def getSeattleSafety(since = START_DATE, to=END_DATE):
    """
    Data structured more in the safety way in the medical meaning.
    We are not going to use this dataset for now.
    {'Electrical Problem', 'Rescue Standby', 'MVI Freeway', 'Wires Down', 
     'LINK - Link Control Center', 'Medic Response- 6 per Rule', 'Aid Response Freeway',
     'Automatic Fire Alarm False', '2RED - 1 + 1', 'Medic Response, 6 per Rule', 'Dumpster Fire',
     'Referral To Agency', 'Mutual Aid- Aid', '1RED 1 Unit', 'Rescue Elevator', 'Scenes Of Violence MCI',
     'Automatic Fire Alarm Resd', 'Encampment Fire', 'Water Rescue Standby', 'Illegal Burn', 
     'EVENT - Special Event', 'Aid Response Yellow', 'Low Acuity Response', 'Natural Gas Leak',
     'Unk Odor', 'Single Medic Unit', 'Water Job Minor', 'Natural Gas Leak Major', 'Triaged Incident',
     'Car Fire', 'Rescue Heavy Major', 'Water Rescue Response', 'Scenes Of Violence 7', 'Rubbish Fire',
     'AFA4 - Auto Alarm 2 + 1 + 1', 'MVI Medic', 'Bark Fire', 'Fire in Building', 'Brush Fire', 
     'Brush Fire Major', 'Medic Response, 7 per Rule', 'Fire in Single Family Res', 'Rescue Extrication',
     'Auto Fire Alarm', '4RED - 2 + 1 + 1', 'Chimney Fire', 'Hang-Up, Aid', 'Medic Response', 'Aid Response',
     'Food On The Stove Out', 'Brush Fire Freeway', 'Car Fire Freeway', 'Trans to AMR', 'MVI - Motor Vehicle Incident',
     'Automatic Medical Alarm', 'Fuel Spill', 'Brush Fire W/Exp.', 'Water Rescue Recon Response', 'HazMat Reduced', 
     'Medic Response- 7 per Rule', 'Encampment Aid', 'Activated CO Detector', 'Rescue Lock In/Out', 'Natural Gas Odor', 
     'Alarm Bell', 'Investigate Out Of Service'}
    """
    start_date = parser.parse(since)
    end_date = parser.parse(to)
    safety = SeattleSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()
    return safety
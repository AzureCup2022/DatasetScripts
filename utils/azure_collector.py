from azureml.opendatasets import BostonSafety, ChicagoSafety, SanFranciscoSafety, NycSafety, SeattleSafety
from datetime import datetime
from dateutil import parser




def collectBostonSafety():
    """
    """
    end_date = parser.parse('2016-01-01')
    start_date = parser.parse('2015-05-01')
    safety = BostonSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()
    print(safety)

def collectChicagoSafety():
    """
    """
    end_date = parser.parse('2016-01-01')
    start_date = parser.parse('2015-05-01')
    safety = ChicagoSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()
    
def collectSanFranciscoSafety():
    """
    """
    end_date = parser.parse('2016-01-01')
    start_date = parser.parse('2015-05-01')
    safety = SanFranciscoSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()

def collectNycSafety():
    """
    """
    end_date = parser.parse('2016-01-01')
    start_date = parser.parse('2015-05-01')
    safety = NycSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()

def collectSeattleSafety():
    """
    """
    end_date = parser.parse('2016-01-01')
    start_date = parser.parse('2015-05-01')
    safety = SeattleSafety(start_date=start_date, end_date=end_date)
    safety = safety.to_pandas_dataframe()
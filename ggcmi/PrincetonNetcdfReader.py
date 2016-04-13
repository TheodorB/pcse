from pcse.pcse.fileinput import Hdf5WeatherDataProvider;

class PrincetonWeatherDataProvider(Hdf5WeatherDataProvider):
    # Dummy lambda function
    dummy = lambda x: x;
    
    def __init__(self, longitude, latitude, fpath=None, force_update=False):
        # Add optional variables; conversion to VAP is not done by means of a lambda function
        self.netcdf_variables.append("hus");
        self.pcse_variables.append(("VAP", "hus", self.dummy, "hPa"));
        
        Hdf5WeatherDataProvider.__init__(self, "Princeton", longitude, latitude, fpath, force_update);

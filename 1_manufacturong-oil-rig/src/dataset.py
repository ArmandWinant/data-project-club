import pandas as pd
import numpy as np
import os
from pathlib import Path
import re

class DataSet:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__project_dir = os.path.join(Path.home(), "Desktop/Projects/data-project-club/1_manufacturong-oil-rig")
        self.__data_dir = os.path.join(self.__project_dir, "data")
        
        self.__data = None
        
    def read_data(self):
        self.__data = pd.read_csv(os.path.join(self.__data_dir, self.__file_name), delimiter="\t", header=None)
    
    def cycle_metadata(self):
        try:
            self.__data["cycleNumber"] = self.__data.index + 1
        except AttributeError:
            print("The data has not been loaded.")
            
    def get_sensor_name(self):
        sensor_type = re.search(r"^[a-zA-Z]+", self.__file_name).group()
        sensor_number = re.search(r"(\d)+", self.__file_name).group()
        
        return sensor_type, sensor_number
    
    def sensor_meta_data(self):
        sensor_type, sensor_number = self.get_sensor_name()
        try:
            self.__data["sensorType"] = sensor_type
            self.__data["sensorNumber"] = sensor_number
        except AttributeError:
            print("The data has not been loaded.")
        
    def cycle_to_sample(self):
        try:
            long_data = self.__data.melt(id_vars=["cycleNumber"], var_name="metric", value_name="value")
            long_data["sampleNumber"] = long_data.index + 1
            
            print(long_data.head())
        except AttributeError:
            print("The data has not been loaded.")
        except KeyError:
            print("Cound not find cycle number.")
            
    def metrics_upload():
        pass
    
    def sensors_upload():
        pass
    
    def samples_upload():
        pass
    
    def cycles_upload():
        pass
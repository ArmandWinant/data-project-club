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
        try:
            self.__data = pd.read_csv(os.path.join(self.__data_dir, self.__file_name), delimiter="\t", header=None)

            self.__cycleCount = self.__data.shape[0]
            self.__sampleCount = self.__data.shape[1]
        except FileNotFoundError:
            print(f"Could not file '{self.__file_name}' in folder '{self.__data_dir}'")
    
    def cycle_metadata(self):
        try:
            self.__data["cycleNumber"] = self.__data.index + 1
        except AttributeError:
            print("The data has not been loaded.")
            
    def get_sensor_name(self):
        sensor_type = re.search(r"^[a-zA-Z]+", self.__file_name).group()
        sensor_number = re.search(r"(\d)+", self.__file_name).group()
        
        self.sensor_type = sensor_type
        self.sensor_number = sensor_number
    
    def sensor_metadata(self):
        try:
            self.__data["sensorType"] = self.sensor_type
            self.__data["sensorNumber"] = self.sensor_number
        except TypeError:
            print("The data has not been loaded.")
        
    def cycle_to_sample(self):
        try:
            long_data = self.__data.melt(id_vars=["cycleNumber", "sensorType", "sensorNumber"], var_name="sampleNumber", value_name="value")
            long_data["sampleNumber"] += 1
            long_data.sort_values(by=["cycleNumber", "sampleNumber"], inplace=True)
        except AttributeError:
            print("The data has not been loaded.")
        except KeyError:
            print("Cound not find cycle number.")
    
    def get_data(self):
        return self.__data

            
class SensorDataSet(DataSet):
    def __init__(self, filename):
        super().__init__(filename)
        
        self.get_sensor_name()
        
    def extractTransformLoad(self):
        self.read_data()
        self.cycle_metadata()
        self.sensor_metadata()
        self.cycle_to_sample()
        
#     def metrics_upload():
#         pass
    
#     def sensors_upload():
#         pass
    
#     def samples_upload():
#         pass
    
#     def cycles_upload():
#         pass
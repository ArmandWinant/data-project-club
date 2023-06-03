import pandas as pd
import numpy as np
import os
from pathlib import Path
import re
from datetime import datetime


class DataSet:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__project_dir = os.path.join(Path.home(), "Desktop/Projects/data-project-club/1_manufacturong-oil-rig")
        self.__data_dir = os.path.join(self.__project_dir, "data")
                
    def read_data(self):
        try:
            file_full_path = os.path.join(self.__data_dir, self.__file_name)
            self.__data = pd.read_csv(file_full_path, delimiter="\t", header=None)
            
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_full_path))
            file_mod_date_str = file_mod_time.strftime("%Y-%m-%d")
            self.__cycleDate = file_mod_date_str
            
            self.__cycleCount = self.__data.shape[0]
            self.__sampleCount = self.__data.shape[1]
        except FileNotFoundError:
            print(f"Could not file '{self.__file_name}' in folder '{self.__data_dir}'")
    
    def cycle_metadata(self):
        try:
            self.__data["cycleNumber"] = self.__data.index + 1
            self.__data["cycleDate"] = self.__cycleDate
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
            self.__data_long = self.__data.melt(id_vars=["cycleDate", "cycleNumber", "sensorType", "sensorNumber"],
                                         var_name="sampleNumber", value_name="value")
            
            self.__data_long["sampleNumber"] += 1
            self.__data_long["samplingRate"] = self.__sampleCount
        except AttributeError:
            print("The data has not been loaded.")
        except KeyError:
            print("Cound not find cycle number.")
    
    def get_data(self, long=False):
        if long:
            return self.__data_long
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
        
        print(self.get_data(long=True).head())
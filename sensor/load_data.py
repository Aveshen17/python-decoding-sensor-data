import os
import glob
import csv

def load_sensor_data():
    sensor_data=[]

    sensor_files= glob.glob(os.path.join(os.getcwd(),"datasets","*.csv"))
    for sensor_file in sensor_files:
        open data_file with sensor_file
            data_reader = csv.DictReader(data_file,delimiter=',')
            for row in data_file:
                sensor_data.append(self, row)


    return sensor_data



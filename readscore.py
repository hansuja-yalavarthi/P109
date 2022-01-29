import pandas as pd
import statistics
import csv

df=pd.read_csv("StudentsPerformance.csv")
reading=df["reading score"].to_list()
reading_mean=statistics.mean(reading)
reading_median=statistics.median(reading)
reading_mode=statistics.mode(reading)
print("mean, median, and mode of reading is {}, {}, and {}".format(reading_mean, reading_median, reading_mode))
reading_stdev=statistics.stdev(reading)
reading_first_stdev_start, reading_first_stdev_end = reading_mean - reading_stdev, reading_mean + reading_stdev
reading_second_stdev_start, reading_second_stdev_end = reading_mean - (2*reading_stdev), reading_mean + (2*reading_stdev)
reading_third_stdev_start, reading_third_stdev_end = reading_mean - (3*reading_stdev), reading_mean + (3*reading_stdev)
reading_data_1stdev=[result for result in reading if result > reading_first_stdev_start and result < reading_first_stdev_end]
reading_data_2stdev=[result for result in reading if result > reading_second_stdev_start and result < reading_first_stdev_end]
reading_data_3stdev=[result for result in reading if result > reading_third_stdev_start and result < reading_first_stdev_end]
print("{} % of data for reading within 1 stdev".format(len(reading_data_1stdev)*100.0/len(reading)))
print("{} % of data for reading within 2 stdev".format(len(reading_data_2stdev)*100.0/len(reading)))
print("{} % of data for reading within 3 stdev".format(len(reading_data_3stdev)*100.0/len(reading)))
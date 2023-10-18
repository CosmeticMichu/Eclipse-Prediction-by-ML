import csv
from datetime import datetime, date, timedelta
from Calculations.aux_funcs import get_minimum_separation, get_minimum_separation_lunar
import pandas as pd

def get_separation(csv_read_path, csv_output_path, type):
    df = pd.read_csv(csv_read_path, parse_dates=['Date'])
    df = df.tail(500)
    eclipses_list = df['Date'].tolist()

    with open(csv_output_path, mode='w') as csv_file:
        fieldnames = ['Date', 'Separation', 'Is Eclipse']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        start_date = date(1950, 1, 1)
        end_date = date(2100, 12, 31)
        while start_date <= end_date:
            date_str = datetime.strftime(start_date, '%Y-%m-%d')
            if type == 'solar':
                sep = get_minimum_separation(date_str)
            elif type == 'lunar':    
                sep = get_minimum_separation_lunar(date_str)
            else: raise Exception('type was not a solar or lunar type. Please check')
            isEclipse = date_str in eclipses_list
            writer.writerow({'Date': date_str, 'Separation': sep, 'Is Eclipse': isEclipse})
            print(date_str)
            start_date += timedelta(days=1)
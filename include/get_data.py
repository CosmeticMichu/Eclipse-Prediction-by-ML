from DataManagement.download import Download_LE_Data, Download_SE_Data
from DataManagement.tocsv import txttocsv

firstYear = -1999
lastYear = 2001

if __name__ == '__main__':
# Data download
    Download_LE_Data.iterate(firstYear,lastYear)
    Download_SE_Data.iterate(firstYear,lastYear)

    # Data convertion from txt to csv

    # solar
    s_inpath = 'data/solar-eclipses.txt'
    s_outpath = 'data/solar-eclipses.csv'
    txttocsv.convert(s_inpath,s_outpath, 'solar')

    # lunar
    l_inpath = 'data/lunar-eclipses.txt'
    l_outpath = 'data/lunar-eclipses.csv'
    txttocsv.convert(l_inpath, l_outpath, 'lunar')
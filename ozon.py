#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('longitude', metavar='LON', type=float, help='Longitude, deg')
parser.add_argument('latitude',  metavar='LAT', type=float, help='Latitude, deg')

if __name__ == "__main__":
    args = parser.parse_args()
    print(args.longitude, args.latitude)
    
long = f.variables['longitude'][:]
lat = f.variables['latitude'][:]
o3 = f.variables['Average_O3_column'][:] 
time = f.variables['time'][:]


def func(latitude, longitude):
    dict = {}
    dict['coordinates'] = [float(latitude), float(longitude)]
    dict['january'] = {}
    dict['july'] = {}
    dict['all'] = {}

    index_lat = np.where(lat == latitude) #индексы соответсвующие широте
    index_long = np.where(long == longitude) #индексы, соответствующие долготе
    
    date = (pd.date_range(start='1990-1', end='2029-1', freq='M'))
    years = (pd.date_range(start='1990-1', end='2029-1', freq='Y'))
    
    january = date.month == 1
    july = date.month == 6
       
    O_all = (o3[:, index_lat, index_long].flatten()) #среднее содержание азота за все время
    O_jan = (o3[january, index_lat, index_long].flatten()) #среднее содержание азота за январь
    O_jul = (o3[july, index_lat, index_long].flatten()) #среднее содержание азота за июль
   
    dict['all']['mean'] = O_all.mean().round(1) # среднее содержание азота за все время
    dict['all']['max'] = float(O_all.max()) # максимальное
    dict['all']['min'] = float(O_all.min())    # минимальное 

    dict['january']['mean'] = O_jan.mean().round(1) # среднее содержание азота за январь
    dict['january']['max'] = float(O_jan.max()) # максимальное
    dict['january']['min'] = float(O_jan.min())   # минимальное 
    
    dict['july']['mean'] = O_jul.mean().round(1) #среднее содержание азота за июль
    dict['july']['max'] = float(O_jul.max()) #максимальное
    dict['july']['min'] = float(O_jul.min()) # минимальное 
    
    plt.figure(dpi=80)
    
    plt.plot(date, O_all, color = 'orange')
    plt.plot(years, O_jan, color = 'blue')
    plt.plot(years, O_jul, color= 'red')
    plt.xlabel('Year')
    plt.ylabel('O3, d. unit')
    plt.legend(['january', 'jul', 'all'])
    plt.title('time dependence of ozone')
    plt.savefig('ozon.png')
    return dict

coordinates = func(37, 55)

with open('ozon.json', 'w') as g:
    json.dump((coordinates), g)
    
with open('ozon.json', 'r') as g:    
    print(json.load(g))    
 

import pandas as pd
import sys
import os
import glob
import numpy as np

def df_from_csvs(path):
    """
    Función para crear un df a partir de munchos csv. 
    arg: 
    path= ruta relativa hasta la carpeta contenedora de los csv
    """
    all_files = glob.glob(path + "/*.csv")
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0,sep= ';')
        li.append(df)
        # print(li)
    union = pd.concat(li, axis=0, ignore_index=True)
    return union 


def ley_orden(df):
    horas = ['01', '02','03','04','05', '06', '07', '08', '09', '10', '11', '12',
         '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
    columns_names = ['provincia', 'municipio', 'estacion', 'magnitud', 'punto_muestreo',
       'year', 'month', 'day', 'h01', 'v01', 'h02', 'v02', 'h03', 'v03', 'h04',
       'v04', 'h05', 'v05', 'h06', 'v06', 'h07', 'v07', 'h08', 'v08', 'h09',
       'v09', 'h10', 'v10', 'h11', 'v11', 'h12', 'v12', 'h13', 'v13', 'h14',
       'v14', 'h15', 'v15', 'h16', 'v16', 'h17', 'v17', 'h18', 'v18', 'h19',
       'v19', 'h20', 'v20', 'h21', 'v21', 'h22', 'v22', 'h23', 'v23', 'h24',
       'v24']
    df.set_axis(columns_names, axis='columns', inplace=True)
    for hora in horas:
        df[f'h{hora}'] = np.where(df[f'v{hora}']=='N', np.nan, df[f'h{hora}'])
    li_v = []
    for hora in horas:
        li_v.append(f'v{hora}')
    df.drop(li_v, axis = 1, inplace=True) 
    df.fillna(method='ffill', inplace=True)
    li_h = []
    for hora in horas:
        li_h.append(f'h{hora}')
    df_melt = df.melt(['provincia', 'municipio', 'estacion', 'magnitud', 'punto_muestreo',
       'year', 'month', 'day']) 
    df_melt.rename(columns = {'variable':'hour'}, inplace = True)    
    horas = [int(x[1:]) for x in li_h]
    dic_horas = dict(zip(li_h, horas))
    df_melt['hour']= df_melt['hour'].map(dic_horas)
    df_melt['miDt']=pd.to_datetime(df_melt[['year','month','day','hour']])
    df_melt.drop(['provincia','year','month','day','hour'], axis = 1, inplace=True)
    df_melt = df_melt.iloc[:,[0,1,2,3,5,4]]
    df_total = pd.pivot_table(data=df_melt,
               index=['miDt', 'estacion', 'municipio'],
               columns=['magnitud']
              )
    df_total.reset_index()

    return df_total


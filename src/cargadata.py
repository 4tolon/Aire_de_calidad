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
    """
    
    """
    horas = ['01', '02','03','04','05', '06', '07', '08', '09', '10', '11', '12',
         '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

    columns_names = ['provincia', 'municipio', 'estacion', 'magnitud', 'punto_muestreo',
       'year', 'month', 'day', 'h01', 'v01', 'h02', 'v02', 'h03', 'v03', 'h04',
       'v04', 'h05', 'v05', 'h06', 'v06', 'h07', 'v07', 'h08', 'v08', 'h09',
       'v09', 'h10', 'v10', 'h11', 'v11', 'h12', 'v12', 'h13', 'v13', 'h14',
       'v14', 'h15', 'v15', 'h16', 'v16', 'h17', 'v17', 'h18', 'v18', 'h19',
       'v19', 'h20', 'v20', 'h21', 'v21', 'h22', 'v22', 'h23', 'v23', 'h24',
       'v24']
    # Renombro columnas 
    df.set_axis(columns_names, axis='columns', inplace=True)
    # Dropeo filas con ensayos minoritarios 
    lista_dropeos = [22, 35, 37, 38, 39, 431]
    for i in lista_dropeos:
        indexNames = df[ df['magnitud'] == i ].index
        df.drop(indexNames , inplace=True)
    # Bucle para poner NaN en ensayos no validos
    for hora in horas:
        df[f'h{hora}'] = np.where(df[f'v{hora}']=='N', np.nan, df[f'h{hora}'])
    # Dropeo de columnas de verificación
    li_v = []
    for hora in horas:
        li_v.append(f'v{hora}')
    df.drop(li_v, axis = 1, inplace=True) 
    # Relleno de los NaN creados con el valos posterior válido.
    df.fillna(method='ffill', inplace=True)
    # Listeo de columnsa por hora.
    li_h = []
    for hora in horas:
        li_h.append(f'h{hora}')
    # Giro radical del dataframe bloqueado las columns listadas.
    df_melt = df.melt(['provincia', 'municipio', 'estacion', 'magnitud', 'punto_muestreo',
       'year', 'month', 'day']) 
    # Renombre de la colunna a horas
    df_melt.rename(columns = {'variable':'hour'}, inplace = True)
    # Transformacion de los valores de la colunma horas a int mediante dicionario.  
    horas = [int(x[1:]) for x in li_h]
    dic_horas = dict(zip(li_h, horas))
    df_melt['hour']= df_melt['hour'].map(dic_horas)
    # Creacion de columna datetime.
    df_melt['miDt']=pd.to_datetime(df_melt[['year','month','day','hour']])
    # Modificacion columna codigo estacion --- punto_muestreo
    df_melt['punto_muestreo']=df_melt['punto_muestreo'].apply([lambda x: x[:8]])
    # Drop de lo que sobra
    df_melt.drop(['provincia','year','month','day','hour', 'municipio', 'estacion'], axis = 1, inplace=True)
    # Orden de colunas
    df_melt = df_melt.iloc[:,[3,1,0,2]]
    # Desdoblamiento para dejar index vertical datetime
    df_total = pd.pivot_table(data=df_melt,
               index=['miDt', 'punto_muestreo'],
               columns=['magnitud']
              )
    # Nombramiento de cada ensayo
    multi_col = df_total.columns
    new_col = pd.Index(['ensayo_' + str(e[1]) for e in multi_col.tolist()])
    df_total.columns = new_col
    # Desdoble final para pasa a mono index vertical y mult horizontal
    df_total = pd.pivot_table(data=df_total,
               index=['miDt'],
               columns=['punto_muestreo']
              )
    return df_total


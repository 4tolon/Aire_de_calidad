import pandas as pd
import sys
import os
import glob


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
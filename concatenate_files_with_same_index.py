# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 09:50:46 2016

@author: correabe
"""
import pandas as pd

fixed_df = pd.read_csv("D:/kaggle/bancolombia/ESTADOTDC201506.csv",
                    dtype={'CEDULA1':str,'FRANQUICIA':str,'NUMEROTARJETA1':str,
                    'CODIGO_VENDEDOR':str,'TIPO TARJETA':str}, sep=';',
                    index_col=['CEDULA1','NUMEROTARJETA1'])
                    
month_07 = pd.read_csv("D:/kaggle/bancolombia/ESTADOTDC201507.csv",
                    dtype={'CEDULA1':str,'FRANQUICIA':str,'NUMEROTARJETA1':str,
                    'CODIGO_VENDEDOR':str,'TIPO TARJETA':str,}, sep=';',
                    names=['CED_07','FRANQUICIA_07','TIPO_TARJETA_07','TARJ_07','CUPO GLOBAL_07',
                    'DISPONIBLE_07','FECHA DE EMISION_07','FECHA ULT AUMENTO CUPO_07','TOTAL MES EN MORA_07',
                    'ALTURA DE MORA_07','CODIGO VENDEDOR_07','CODIGO ESTADO TARJETA_07'],
                    index_col=['CED_07','TARJ_07'])
                    
month_08 = pd.read_csv("D:/kaggle/bancolombia/ESTADOTDC201508.csv",
                    dtype={'CEDULA1':str,'FRANQUICIA':str,'NUMEROTARJETA1':str,
                    'CODIGO_VENDEDOR':str,'TIPO TARJETA':str,}, sep=';',
                    names=['CED_08','FRANQUICIA_08','TIPO_TARJETA_08','TARJ_08','CUPO GLOBAL_08',
                    'DISPONIBLE_08','FECHA DE EMISION_08','FECHA ULT AUMENTO CUPO_08','TOTAL MES EN MORA_08',
                    'ALTURA DE MORA_08','CODIGO VENDEDOR_08','CODIGO ESTADO TARJETA_08'],
                    index_col=['CED_08','TARJ_08'])

month_09 = pd.read_csv("D:/kaggle/bancolombia/ESTADOTDC201509.csv",
                    dtype={'CEDULA1':str,'FRANQUICIA':str,'NUMEROTARJETA1':str,
                    'CODIGO_VENDEDOR':str,'TIPO TARJETA':str,}, sep=';',
                    names=['CED_09','FRANQUICIA_09','TIPO_TARJETA_09','TARJ_09','CUPO GLOBAL_09',
                    'DISPONIBLE_09','FECHA DE EMISION_09','FECHA ULT AUMENTO CUPO_09','TOTAL MES EN MORA_09',
                    'ALTURA DE MORA_09','CODIGO VENDEDOR_09','CODIGO ESTADO TARJETA_09'],
                    index_col=['CED_09','TARJ_09'])
                    
month_10 = pd.read_csv("D:/kaggle/bancolombia/ESTADOTDC201510.csv",
                    dtype={'CEDULA1':str,'FRANQUICIA':str,'NUMEROTARJETA1':str,
                    'CODIGO_VENDEDOR':str,'TIPO TARJETA':str,}, sep=';',
                    names=['CED_10','FRANQUICIA_10','TIPO_TARJETA_10','TARJ_10','CUPO GLOBAL_10',
                    'DISPONIBLE_10','FECHA DE EMISION_10','FECHA ULT AUMENTO CUPO_10','TOTAL MES EN MORA_10',
                    'ALTURA DE MORA_10','CODIGO VENDEDOR_10','CODIGO ESTADO TARJETA_10'],
                    index_col=['CED_10','TARJ_10'])
                    
#cancel_06 = fixed_df[fixed_df['CODIGO ESTADO TARJETA']==3000000000]
#cancel_07 = month_07[month_07['CODIGO ESTADO TARJETA_07']==3000000000]
#cancel_08 = month_08[month_08['CODIGO ESTADO TARJETA_08']==3000000000]
#cancel_09 = month_09[month_09['CODIGO ESTADO TARJETA_09']==3000000000]
#cancel_10 = month_10[month_10['CODIGO ESTADO TARJETA_10']==3000000000]

count=0

result = pd.concat([fixed_df,month_07,month_08,month_09,month_10],axis=1)

result.to_csv("concatenacion_entera.csv")
first_ok = result['CODIGO ESTADO TARJETA']==0
last_not_ok = result['CODIGO ESTADO TARJETA_10']==3000000000

cambio = result[first_ok & last_not_ok]

print cambio[:5]

print len(cambio)


#print result.loc[126127,56495]

#print len(result)
#print len(cancel_10)

#grouped = cancel_06.groupby(['CEDULA1','NUMEROTARJETA1'])
#grouped_07= cancel_07.groupby(['CEDULA1','NUMEROTARJETA1'])

#for name,group in grouped:
#    print (name)
#    print (group)





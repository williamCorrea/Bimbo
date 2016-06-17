# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 14:15:11 2016

@author: correabe
"""
import pandas as pd

fixed_df = pd.read_csv("change.csv",
                    dtype={'CEDULA':str,'NUMTARJETA':str,'FRANQUICIA':str,
                    'CODIGO_VENDEDOR':str,'TIPO TARJETA':str,'FRANQUICIA_07':str,
                    'CODIGO_VENDEDOR_07':str,'TIPO TARJETA_07':str,'FRANQUICIA_08':str,
                    'CODIGO_VENDEDOR_08':str,'TIPO TARJETA_08':str,'FRANQUICIA_09':str,
                    'CODIGO_VENDEDOR_09':str,'TIPO TARJETA_09':str,'FRANQUICIA_10':str,
                    'CODIGO_VENDEDOR_10':str,'TIPO TARJETA_10':str}, sep=',')
                    
print fixed_df[['DISPONIBLE','DISPONIBLE_07','DISPONIBLE_08','DISPONIBLE_09','DISPONIBLE_10']].iloc[:10]

change_1 = fixed_df['CODIGO ESTADO TARJETA_07']==3000000000
change_2 = fixed_df['CODIGO ESTADO TARJETA_08']==3000000000
change_3 = fixed_df['CODIGO ESTADO TARJETA_09']==3000000000
change_4 = fixed_df['CODIGO ESTADO TARJETA_10']==3000000000


change_07 = fixed_df[change_1]
change_08 = fixed_df[change_2 & ~change_1]
change_09 = fixed_df[change_3 & ~change_2 & ~change_1]
change_10 = fixed_df[change_4 & ~change_3 & ~change_2 & ~change_1]

print len(change_07)
print len(change_08)
print len(change_09)
print len(change_10)

change_07.to_csv("change_07.csv")
change_08.to_csv("change_08.csv")
change_09.to_csv("change_09.csv")
change_10.to_csv("change_10.csv")





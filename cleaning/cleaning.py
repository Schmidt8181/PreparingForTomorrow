import pandas as pd
import numpy as np
import datetime

def clean_temperature_data_step1(df):
    temp_df = df.drop(['J-D', 'D-N', 'DJF', 'MAM', 'JJA', 'SON'], axis=1)
    clean_temp_df = temp_df[temp_df.Year > 1989].copy()
    clean_temp_df.rename(columns={'Jan':'1','Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}, inplace=True)
    clean_temp_df = pd.melt(clean_temp_df, id_vars='Year', value_vars=['1', '2', '3','4','5','6','7','8','9','10','11','12'])
    return clean_temp_df

def clean_temperature_data_step2(clean_temp_df):
    clean_temp_df.rename(columns={'variable': 'Month'}, inplace=True)
    clean_temp_df.loc[:,'Day'] = 1
    clean_temp_df.loc[:,'Date'] = np.nan
    clean_temp_df.loc[:,'Date'] = pd.to_datetime(clean_temp_df[['Year','Month', 'Day']])
    clean_temp_df.loc[:,'Temperature'] = pd.to_numeric(clean_temp_df['value'], errors='coerce')
    clean_temp_df = clean_temp_df.drop(['Month', 'Day', 'Year', 'value'], axis=1)
    clean_temp_df.sort_values('Date', inplace=True)
    clean_temp_df = clean_temp_df.reset_index(drop=True)
    #print(clean_temp_df.tail(7))
    return clean_temp_df

def clean_food_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    food_data = df.copy()
    food_data = food_data.drop(['Food Price Index'], axis=1)
    #print(food_data.tail(12))
    return food_data

def reshape_for_pyflux(df,id_vars):
    new_df = pd.melt(df, id_vars=id_vars)
    return new_df

# coding: utf-8

import pandas as pd
import numpy as np
import datetime

def fix_formatting(df, starttime_raw = '2021-07-21 20:00'):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df[df['Timestamp'] > starttime_raw].copy()
    return df.reset_index()

def find_peak_gravity(df):
    peak_gravity_idx = df[df['SG']==df['SG'].max()].index[0]
    df = df.loc[peak_gravity_idx:,:]
    return df.reset_index()

def make_t(df):
    df = df[['Timestamp', 'SG']].copy()
    starttime = df['Timestamp'].min()
    df['t'] = (df['Timestamp'] - starttime) / np.timedelta64(1,'s')
    return df.copy()


def main():
    df = pd.read_csv('../data/data.csv')
    df = fix_formatting(df)
    df = find_peak_gravity(df)
    df = make_t(df)
    df.to_csv(f'../data/processed_data_{datetime.date.today()}.csv')

if __name__ == '__main__':
    main()

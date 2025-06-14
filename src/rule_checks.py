import pandas as pd
import numpy as np

def check_missing_values(df):
    return df[df.isnull().any(axis=1)]

def check_negative_closing_values(df):
    return df[df['Closing_Value'] < 0]

def check_sudden_spikes(df, z_thresh=2.5):
    mean = df['Closing_Value'].mean()
    std = df['Closing_Value'].std()
    z_scores = (df['Closing_Value'] - mean) / std
    return df[np.abs(z_scores) > z_thresh]

def check_volume_spikes(df, z_thresh=2.5):
    mean = df['Volume'].mean()
    std = df['Volume'].std()
    z_scores = (df['Volume'] - mean) / std
    return df[np.abs(z_scores) > z_thresh]

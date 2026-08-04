import pandas as pd
import sklearn
import numpy as np
import math

def elo_rating():
    return

def elo_change():
    return

def logistic_regression():
    return

def gradient_boosting():
    return

def main():
    df = pd.read_csv('afl_matches_clean.csv')
    INITIAL_ELO = 1500
    team_elo = {
        'Adelaide': INITIAL_ELO,
        'Brisbane': INITIAL_ELO,
        'Carlton': INITIAL_ELO,
        'Collingwood': INITIAL_ELO,
        'Essendon': INITIAL_ELO,
        'Fremantle': INITIAL_ELO,
        'Geelong': INITIAL_ELO,
        'Gold Coast': INITIAL_ELO,
        'GWS Giants': INITIAL_ELO,
        'Hawthorn': INITIAL_ELO,
        'Melbourne': INITIAL_ELO,
        'North Melbourne': INITIAL_ELO,
        'Port Adelaide': INITIAL_ELO,
        'Richmond': INITIAL_ELO,
        'St Kilda': INITIAL_ELO,
        'Sydney': INITIAL_ELO,
        'West Coast': INITIAL_ELO,
        'Western Bulldogs': INITIAL_ELO,
    }

main()

# -*- coding: utf-8 -*-
"""Project - 108.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yDBQvTCOVWl6gtmWm2j1KOxPuyZtJ5WL
"""

import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('loldata.csv')
df
fig = ff.create_distplot([df["Avg Rating"]],["Avg Rating"],show_hist = False)
fig.show()
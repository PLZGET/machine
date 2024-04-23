import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from stemgraphic import stem_graphic

# from stemgraphic import stem_graphic
gender = np.array(['M','M','M','M',
                    'M','M','M','M',
                    'F','F','F','F','F',
                    'F','F','F','F','F'])
score = np.array([98,90,96,54,
                43,87,88,90,
                94,92,81,79,85,
                91,79,88,89,83])
print("np.median(score): ", np.median(score)) # 중앙값 print(np.percenpntile(score,50))과 같음

print("np.quantile(score,0.25) 1사분위수: ", np.quantile(score,0.25)) # 1사분위수
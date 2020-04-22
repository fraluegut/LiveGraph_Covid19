import random
from itertools import count
import tkinter
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
#plt.style.use('fivethirtyeight')

x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 7, 3, 2, 5]

plt.plot(x_vals, y_vals)
plt.savefig("mygraph.png")
as
plt.tight_layout()
plt.show()



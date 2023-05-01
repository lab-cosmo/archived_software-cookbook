#!/usr/bin/env python
# coding: utf-8

"""
MLP with Linear Model
=====================
"""
# %%
#


import numpy as np
import matplotlib.pyplot as plt

# %%
# Explanation

X = np.random.rand(10000)*400
Y = 0.1*X+10.1
Y_p = Y + np.random.randn(10000)*1.5

# %%
# widget does not work

import ipywidgets
from IPython.display import display
widget = ipywidgets.IntSlider()
display(widget)

# %%
# widget
# ------
# 
# .. jupyter-execute::
# 
#     import ipywidgets as widgets
#     from IPython.display import display
# 
#     a = widgets.IntSlider()
#     display(a)
# 

# %%
# widget
# ------
# if you run this on your machine it prints something
# but inside this nbsphinx this does not work
#
# .. jupyter-execute::
# 
#     button = widgets.Button(description="Click Me!")
#     output = widgets.Output()
#     
#     display(button, output)
#     
#     def on_button_clicked(b):
#         with output:
#             print("Button clicked.")
#     
#     button.on_click(on_button_clicked)

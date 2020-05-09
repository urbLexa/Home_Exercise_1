# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:10:44 2020

@author: Axel
"""

from utils import pv_Power
from utils import pv_roof_area

'''
Test panel: https://static.trinasolar.com/sites/default/files/Datasheet_Tallmax_1500V%20M%20Plus_2019_May.pdf
Test irradiance on tilted surface 600 W/m2
Roof dimensions 6 x 15 meters
'''
panel = {
    "x_pan": 0.992,
    "y_pan": 1.960,
    "b": 0.04,
    "eff": 0.195
    }

g_tilt = 600

def test_pv_roof_area():
    assert pv_roof_area(6, 15, panel) == 72.01152

def test_pv_Power():
    assert pv_Power(g_tilt, 6, 15, panel) == 6.740278272
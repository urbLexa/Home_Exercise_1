# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:35:47 2020

@author: Axel
"""


def pv_roof_area(x_roof, y_roof, panel):
    '''
    Calculation of effective PV area of roof considering complete roof
    available for panels

    Parameters
    ----------
    x_roof : float
        Length of roof in x-direction in meters.
    y_roof : float
        Length of roof in y-direction in meters..
    panel : dict
        Python dictonary with the following keys:
            'x_pan' --> x-dimension panel in meters
            'y_pan' --> y-dimension panel in meters
            'b'     --> Panel boarder thickness in meters
            'eff'   --> Panel efficiency in decimal
    
    Returns
    -------
    PV area
        Effective PV area in m^2 to be used in PV power calculations.

    '''
    nr_pan_x = int(x_roof / panel['x_pan'])
    nr_pan_y = int(y_roof / panel['y_pan'])
    return (nr_pan_x * (panel['x_pan'] - 2 * panel['b']) * nr_pan_y * 
            (panel['y_pan'] - 2 * panel['b']))

def pv_Power(g_tilt, x_roof, y_roof, panel, pr=0.8):
    '''
    Calculation of pv power in [kW] for specific irradiance on tilted surface

    Parameters
    ----------
    g_tilt : float
        Irradiance on roof surface in W/m2 taking into account roof elevation
        and azimuth angle.
    x_roof : flaot
        Length of roof in x-direction in meters.
    y_roof : float
        Length of roof in y-direction in meters..
    panel : dict
        Python dictonary with the following keys:
            'x_pan' --> x-dimension panel in meters
            'y_pan' --> y-dimension panel in meters
            'b'     --> Panel boarder thickness in meters
            'eff'   --> Panel efficiency in decimal
    pr : float, optional
        Performance ratio of PV installation including all losses. 
        The default is 0.8.

    Returns
    -------
    float
        Pv power in kW.

    '''
    pv_area = pv_roof_area(x_roof, y_roof, panel)
    return g_tilt * pv_area * panel['eff'] * pr / 1000

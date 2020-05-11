# Home Exercise 1 - Solar PV Power Calculation

Copyright 2020 Axel Bruck

![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Description

Home Exercise for Open Source Energy System Modeling with shorter functions (sorry that there are more lines than 40 but most of it is docstring and it said at least 2 functions)

The chosen mini-project consitits of two functions:

1) pv_roof_area
2) pv_Power

Depending on the solar irradiance on the titled PV surface, the roof dimensions and panel specifications (hight, length, boarder thickness and efficiency) pv_Power caluculates the pv output power in kW for the respective input irradiance of the respective roof. Therefore, given a time series of the resepective solar irradiance on the correct tilted surface, a pv power profile can be obtained for an arbitrary timeframe for the respective roof.

pv_roof_area is hereby called by pv_Power to calculate the effective panel area of the roof, taking into account that the panels might not exactly fit perfectly within the roof dimensions and also for the boarders of the panels. Due to code length requirements certain points were not taken into account but could be interesting for further developement:
- Exception if unvalid arguments are passed to the function such as 0 to the panel dimensions
- Incusion of windows or chimnies on the roof
- Therefore, an optimisation of available space to allocation of pv panels
- Additional function for calculation of the irradiance on the tilted surface from global horizontal, direct and diffuse horizontal irradiance
- Additional function to create pv power time series of arbitrary resolution and length.
- More extensive and less exact tests --> use rounding or a certain range within the test passes

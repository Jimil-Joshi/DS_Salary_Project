# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 15:10:09 2021

@author: Jimil Joshi
"""

import Githelp as gs
import pandas as pd 

path =  "C:/Users/Jimil Joshi/Documents/DS_Salary_Project/chromedriver.exe"

df =  gs.get_jobs("data scientist", 5, False, path, 15)
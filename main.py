import Glassdoor_Web_Scrapper as gs
import pandas as pd 
path =  "C:/Users/Jimil Joshi/Documents/DS_Salary_Project/chromedriver"

df =  gs.get_jobs(keyword='data scientist',num_jobs=15,verbose = False,path = "C:/Users/Jimil Joshi/Documents/DS_Salary_Project/chromedriver.exe",slp_time=15)
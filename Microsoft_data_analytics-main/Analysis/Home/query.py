import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


BUDGET_data = ( 
        ("1", "200000-500000"), 
        ("2", "500000-1000000"), 
        ("3", "1000000-2000000"), 
        ("4", "2000000-3000000"), 
        ("5", "3000000-4000000"),
        ("6", "4000000-5000000"),
        ("7", "5000000-7000000"),
        ("8", "7000000-10000000"),
        ("9", "10000000-50000000"),
        ("10", "50000000-100000000"),
        ("11", "100000000-200000000"),
        ("12", "200000000-250000000")
    ) 
    
BODY_TYPE = (
    ("1", "Hatchback"),
    ("2", "SUV"),
    ("3", "MPV"),
    ("4", "Sedan"),
    ("5", "Coupe"),
    ("6", "Crossover"),
    ("7", "Sports"),
    ("8", "MUV"),
    ("9", "Pick-up")
)

SEATS = (
    ("1", "2"),
    ("2", "4"),
    ("3", "5"),
    ("4", "6"),
    ("5", "7"),
    ("6", "8"),
    ("7", "9")
)

MILEAGE_data = (
    ("1", "0-5"),
    ("2", "5-10"),
    ("3", "10-15"),
    ("4", "15-20"),
    ("5", "20-25"),
    ("6", "25-30"),
    ("7", "30-35")
)


url = "https://raw.githubusercontent.com/AKR20/Microsoft_data_analytics/main/Analysis/Home/cars_engage_2022_updated.csv"
df = pd.read_csv(url)
#df = pd.read_csv("D:\MyProject\github\Microsoft_data_analytics\Analysis\Home\cars_engage_2022_updated.csv")
# df = pd.read_csv("D:\MyProject\Analysis\Home\cars_engage_2022 updated.csv")
# print(df.head())

def get_query(a,b,c,d):
    price1 ,price2 = BUDGET_data[int(a)-1][1].split('-')  

    mileage1,mileage2 = MILEAGE_data[int(d)-1][1].split('-')
    mileage1+= " km/litre"
    mileage2+= " km/litre"
    body_type = BODY_TYPE[int(b)-1][1]
    seat = int(SEATS[int(c)-1][1])

    # price1 ,price2 = '200000','500000' 

    mileage1,mileage2 = '20 km/litre', '25 km litre'
    # mileage1+= " km/litre"
    # mileage2+= " km/litre"
    body_type = 'Hatchback'
    seat = 4

    print(price1,price2,mileage1,mileage2,body_type,seat)


    data = df[(df['Price'].between(price1,price2)) & (df['City_Mileage'].between(mileage1,mileage2)) & (df['Body_Type'] == body_type) & (df['Seating_Capacity'] == seat)]

    return data



content = get_query(1,1,2,5)
# 
# print(content)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

 

 
df = pd.read_csv("D:\MyProject\github\Microsoft_data_analytics\Analysis\Home\cars_engage_2022_updated.csv")
df.head()



 

def get_graph_cylinder():
    data = list(set(df.Cylinders))
    # print(data)
    # for i in data:
    #     if i.isdecimal():
    #         pass
    #     else:
    #         data.remove(i)
    # print(data)

    li = []
    content = list(df.Cylinders)
    for i in data:
        li.append(content.count(i))
    print(li)

    fig = plt.figure("")
    plt.barh(data,li,color="skyblue")
    plt.xlabel("No. of cylinder")
    plt.ylabel("No of car")

    for index, value in enumerate(li):
        plt.text(value, index, str(value))

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    fig = imgdata.getvalue()
    return fig

# get_graph_cylinder()


# def get_graph_fuel_type():
#     data = list(df.Fuel_Type)

#     data = list(set(data)) 
#     l = []
#     dataset = list(df.Fuel_Type)

#     for val in data:
#         l.append(dataset.count(val))

#     fig = plt.figure("")
#     plt.barh(data,l,color="yellow")
#     plt.xlabel("No of Cars")
#     plt.ylabel("Fuel Types")
#     plt.title("Fuel Types vs No of Cars")

#     for index, value in enumerate(l):
#         plt.text(value, index, str(value))
        

    
#     imgdata = StringIO()
#     fig.savefig(imgdata, format='svg')
#     imgdata.seek(0)

#     fig = imgdata.getvalue()
#     return fig

 
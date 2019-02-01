import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori

dataset=pd.read_csv('Market_Basket_Optimisation.csv',header=None)


records = []  
for i in range(0, 7501):  
    records.append([str(dataset.values[i,j]) for j in range(0, 20)])


association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)  
association_results = list(association_rules)

for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

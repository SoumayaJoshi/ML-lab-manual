import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
print(cars_data)
cars_data.dropna(axis=0,inplace=True)
print(cars_data)

plt.scatter(cars_data['Age'],cars_data['Price'],c='red')
plt.title('Scatter plot of Price vs Age of cars')
plt.xlabel('Age:(Months)')
plt.ylabel('Price:(Dollars)')
plt.show()
plt.savefig("scatter.png")

plt.hist(cars_data['KM'],color='green',edgecolor='black',bins=20)
plt.show()
counts=[979,120,12]
fuelType=['Petrol','Diesel','CNG']
index=np.arange(len(fuelType))
plt.bar(index,counts,color=['red','blue','cyan'])
plt.title("bar plot of fuel types")
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.show()

plt.bar(index,counts,color=['red','blue','cyan'])
plt.title("bar plot of fuel types")
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.xticks(index,fuelType,rotation=90)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\1 Credo Training\python\ML\Housing_Altered.csv")

print(df.head(5))

from os import replace


list1 = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning","prefarea"]

df[list1] = df[list1].replace({"yes":1, "no":0})

print(df.head(5))

df["furnishingstatus"] = df["furnishingstatus"].replace({"unfurnished":0, "semi-furnished":1, "furnished":2})

print(df.head(5))


#corelation

core = df.corr()

plt.figure(figsize=(10,10))
sns.heatmap(core, annot=True, cmap='Blues')
plt.show()


#statistics
df.hist(figsize=(10,10), bins=10)
plt.show()


#data spliting x, y

x = df.drop("price", axis=1)
y = df["price"]


#data spliting for train and test

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1,random_state=42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train,y_train)

y_predict = lr.predict(x_test)

from sklearn.metrics import r2_score

accurary = r2_score(y_test,y_predict) * 100

print(accurary)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_predict)

mse = mean_squared_error(y_test, y_predict)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_predict)

print()
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2 * 100)
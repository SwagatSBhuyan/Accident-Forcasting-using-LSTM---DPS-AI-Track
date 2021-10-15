# Imports
import sys
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Reading CSV dataset with ANSI encoding as it includes German Tokens
df = pd.read_csv(r"dataset/accident_by_date_insgesamt.csv", encoding="utf8")
df.rename(columns = {'Unnamed: 0':'Date'}, inplace = True)
df.tail()

# Regression Setter for Alkoholunfälle: insgesamt
X = df['Date']
x = pd.DataFrame(X)
y_alcohol_subtotal = df['alcohol_subtotal']

# Model
x_train, x_test, y_train, y_test = train_test_split(x, y_alcohol_subtotal, test_size = 0.1)
poly_reg = PolynomialFeatures(degree = 2)
x_train = poly_reg.fit_transform(x_train)
x = poly_reg.fit_transform(x)
reg=LinearRegression()
reg.fit(x_train, y_train)
reg.fit(x, y_alcohol_subtotal)
score = reg.score(poly_reg.fit_transform(x_test), y_test)
# print('Score of model: ', score)

# Prediction
print(reg.predict(poly_reg.fit_transform([[int(sys.argv[1])]]))[0])
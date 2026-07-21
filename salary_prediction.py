from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import numpy as np
import pandas as pd
ds = pd.read_csv('medium_dataset_1000.csv')
# model = KNeighborsClassifier(n_neighbors=8)
# برای پیش‌بینی، 8 همسایه‌ی نزدیک را بررسی کن.

# model = KNeighborsClassifier(
#     n_neighbors=5,
#     weights='uniform')
# تعداد همسایه ها مهمه . مقدار محتوا مهم نیست

# model = KNeighborsClassifier(
#     n_neighbors=7,
#     weights='distance')
# همسایه‌ی نزدیک‌تر، رأی قوی‌تری دارد.

# model = KNeighborsClassifier(
#     n_neighbors=3,
#     metric='euclidean')
# همان فاصله‌ی معمول بین دو نقطه است.

# model = KNeighborsClassifier(
#     n_neighbors=10,
#     metric='manhattan')
# فاصله را مثل حرکت در خیابان‌های شطرنجی محاسبه می‌کند.

# your_age = int(input("enter your age : "))
# your_purchase_count = int(input("enter your purchase_count : "))

# model = KNeighborsRegressor(
#     n_neighbors=5,
# )
# ds = ds.dropna()
# x = ds[["age","purchase_count"]]
# y = ds["salary"]
# model.fit(x,y)

# new_guy = pd.DataFrame({
#     "age": [your_age],
#     "purchase_count": [your_purchase_count],
# })
# prediction= model.predict(new_guy)
# print(f"Predicted salary: {prediction[0]}")



# def ask_Q (age,purchase):
#     return age,purchase

ds = pd.read_csv("medium_dataset_1000.csv")

ds = ds.dropna()


def normalize_data(ds):

    ds = ds.copy()

    scaler = MinMaxScaler()

    columns = ["age", "purchase_count"]

    ds[columns] = scaler.fit_transform(ds[columns])

    return ds, scaler


def prepare_data():

    normalized_ds, scaler = normalize_data(ds)

    X = normalized_ds[["age", "purchase_count"]]

    Y = ds["salary"]

    return X, Y, scaler


def predict_salary(age, purchase_count):

    X, Y, scaler = prepare_data()

    model = KNeighborsRegressor(
        n_neighbors=9)

    model.fit(X, Y)

    new_user = pd.DataFrame({
        "age": [age],"purchase_count": [purchase_count]})

    new_user[["age", "purchase_count"]] = scaler.transform(new_user[["age", "purchase_count"]])

    prediction = model.predict(new_user)

    return f"Predicted salary: {prediction[0]:.2f}"


age = int(input("Enter your age: "))

purchase_count = int(input("Enter your purchase count: "))


print(predict_salary(age,purchase_count))
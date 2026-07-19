from sklearn.neighbors import KNeighborsRegressor
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



ds = ds.dropna()

def determine():
    X = ds[['age','purchase_count']]
    Y = ds['salary']
    return X,Y

def asle_kar (age,purchase_count):
    X,Y = determine()
    model = KNeighborsRegressor(
        n_neighbors=9
    )
    model.fit(X,Y)
    new_guy =pd.DataFrame({
        'age' : [age],
        'purchase_count' :[purchase_count]
    })
    prediction = model.predict(new_guy)
    return (f"Predicted salary: {prediction[0]:2f}")

age = int(input("enter your age : "))
purchase_count = int(input("enter your purchase_count : "))
print(asle_kar(age,purchase_count))

    
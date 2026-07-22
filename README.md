## Latest update
Improved normalization in the KNN model.
# KNN Salary Prediction

A simple Machine Learning project that predicts a person's salary based on their age and purchase count using the K-Nearest Neighbors (KNN) algorithm.

## 📌 Project Overview

In this project, I used the K-Nearest Neighbors Regressor to predict salary based on two features:

* Age
* Purchase Count

The model learns patterns from an existing dataset and uses those patterns to predict the salary of a new person.

## 🧠 Algorithm

This project uses:

**K-Nearest Neighbors Regression (KNN)**

The model uses the 9 nearest data points to make a salary prediction.

```python
KNeighborsRegressor(
    n_neighbors=9
)
```

## 🔄 How It Works

## 🔄 How It Works

The project follows these steps:

1. Remove missing values from the dataset.
2. Select `age` and `purchase_count` as input features.
3. Select `salary` as the target.
4. Normalize the input features using `MinMaxScaler`.
5. Train the KNN regression model using 9 nearest neighbors.
6. Ask the user for their age and purchase count.
7. Normalize the user's input using the same scaler.
8. Predict the user's salary.

## 📊 Features

### Input

* `age`
* `purchase_count`

### Output

* Predicted salary

Example:

```text
Enter your age: 21
Enter your purchase count: 3

Predicted salary: 8015.56
```

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* K-Nearest Neighbors Regression

## 📚 What I Learned

## 📚 What I Learned

Through this project, I practiced:

* Working with Pandas DataFrames
* Handling missing data
* Splitting features and target variables
* Using functions in Python
* Working with parameters and return values
* Normalizing data using `MinMaxScaler`
* Understanding why normalization is important for KNN
* Training a Machine Learning model
* Making predictions with KNN Regression
* Using Git and GitHub to manage projects

## 🚀 Future Improvements

Some possible improvements for this project:

* Improve the model by splitting the dataset into training and testing sets.
* Split the dataset into training and testing sets.
* Evaluate the model using metrics such as MAE and RMSE.
* Experiment with different values of `n_neighbors`.
* Visualize the relationship between the features and salary.

---

This project is part of my journey in learning Data Analysis and Machine Learning.

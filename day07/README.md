# 🚀 Day 07 - Introduction to NumPy & Machine Learning

## 🎯 Learning Objectives

Today we explored:

* NumPy Fundamentals
* Arrays and Multi-Dimensional Arrays
* Mathematical Operations using NumPy
* Relationship between Pandas and NumPy
* Introduction to Machine Learning
* Scikit-Learn Library
* Machine Learning Algorithms
* Linear Regression
* Logistic Regression
* Random Forest
* K-Means Clustering

---

# 📚 What is NumPy?

NumPy stands for:

```text
Numerical Python
```

It is the foundation library for:

* Scientific Computing
* Data Analysis
* Machine Learning
* Artificial Intelligence

Import NumPy:

```python
import numpy as np
```

---

# Why NumPy?

Traditional Python lists are powerful but become slower when handling large datasets.

NumPy provides:

✅ Faster computation

✅ Less memory usage

✅ Mathematical operations

✅ Multi-dimensional arrays

✅ Foundation for Data Science

---

# Mathematical Operations Work on Arrays

One of NumPy's biggest strengths is performing operations on entire arrays.

Example:

```python
import numpy as np

scores = np.array([10, 20, 30, 40])

print(scores + 5)
```

Output:

```text
[15 25 35 45]
```

Notice:

```text
5 is added to every element automatically.
```

---

# 1-D Array

Example:

```python
import numpy as np

scores = np.array([90, 80, 95, 70])

print(scores)
```

Output:

```text
[90 80 95 70]
```

Shape:

```python
print(scores.shape)
```

Output:

```text
(4,)
```

Meaning:

```text
4 elements in one dimension
```

---

# 2-D Array (Score Matrix)

Example:

```python
import numpy as np

scores = np.array([
    [90, 80, 95],
    [70, 85, 88]
])

print(scores)
```

Output:

```text
[[90 80 95]
 [70 85 88]]
```

Shape:

```python
print(scores.shape)
```

Output:

```text
(2, 3)
```

Meaning:

```text
2 rows
3 columns
```

---

# Multi-Dimensional Arrays

NumPy can store data in multiple dimensions.

Example:

```python
data = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
```

Shape:

```python
print(data.shape)
```

Output:

```text
(2, 2, 2)
```

Meaning:

```text
2 blocks
2 rows
2 columns
```

---

# Important NumPy Methods

## Create Array

```python
np.array([1,2,3])
```

---

## Shape

```python
arr.shape
```

Returns:

```text
Rows and Columns
```

---

## Maximum Value

```python
arr.max()
```

---

## Minimum Value

```python
arr.min()
```

---

## Sum

```python
arr.sum()
```

---

## Mean

```python
arr.mean()
```

---

# Pandas Core Library is NumPy

Important Concept:

```text
Pandas is built on top of NumPy.
```

Architecture:

```text
Python
   ↓
NumPy
   ↓
Pandas
   ↓
Data Analysis
```

Because of this:

* Pandas is fast
* Pandas supports vectorized operations
* Pandas internally uses NumPy arrays

Example:

```python
import pandas as pd

df = pd.read_csv("players.csv")

print(df.values)
```

Output:

```text
NumPy Array
```

---

# Checking Installed Packages

List all installed packages:

```bash
pip list
```

Example Output:

```text
numpy
pandas
gradio
ollama
scikit-learn
```

---

# Installing Machine Learning Library

Install Scikit-Learn:

```bash
pip install scikit-learn
```

Verify Installation:

```bash
pip show scikit-learn
```

---

# What is Machine Learning?

Machine Learning is a branch of AI that enables computers to learn patterns from data.

Instead of:

```text
Hardcoded Rules
```

the system learns from:

```text
Historical Data
```

---

# Simple Definition

```text
Machine Learning = Finding Patterns + Making Predictions
```

Example:

Historical Data:

```text
Study Hours → Marks
```

Machine Learning learns:

```text
More Study Hours → Higher Marks
```

Prediction:

```text
6 Hours Study → 85 Marks
```

---

# Machine Learning Workflow

```text
Data
 ↓
Algorithm
 ↓
Pattern Detection
 ↓
Training
 ↓
Prediction
```

---

# Machine Learning Algorithms

Algorithms are mathematical techniques used to find patterns.

Examples:

### Regression

Used for predicting numbers.

Examples:

* House Price Prediction
* Salary Prediction
* Sales Forecasting

---

### Classification

Used for predicting categories.

Examples:

* Spam or Not Spam
* Pass or Fail
* Disease Detection

---

### Clustering

Used for grouping similar data.

Examples:

* Customer Segmentation
* Product Recommendations

---

# Linear Regression

Most basic Machine Learning algorithm.

Import:

```python
from sklearn.linear_model import LinearRegression
```

Purpose:

Predict continuous values.

Example:

```text
Years of Experience → Salary
```

Sample Code:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

Examples:

* Salary Prediction
* House Price Prediction
* Revenue Forecasting

---

# Logistic Regression

Used for Classification.

Example:

```text
Email → Spam / Not Spam
```

Import:

```python
from sklearn.linear_model import LogisticRegression
```

Examples:

* Fraud Detection
* Disease Prediction
* Customer Churn Prediction

---

# Random Forest

One of the most powerful Machine Learning algorithms.

Import:

```python
from sklearn.ensemble import RandomForestClassifier
```

How it Works:

```text
Multiple Decision Trees
          ↓
Combined Decision
          ↓
Final Prediction
```

Examples:

* Loan Approval
* Risk Analysis
* Fraud Detection

---

# K-Means Clustering

Unsupervised Learning Algorithm.

Import:

```python
from sklearn.cluster import KMeans
```

Purpose:

Group similar records together.

Example:

Customer Data

```text
Customer A
Customer B
Customer C
```

Algorithm automatically creates groups.

Examples:

* Customer Segmentation
* Marketing Analysis
* Product Grouping

---

# Machine Learning vs Traditional Programming

Traditional Software:

```text
Rules + Data
      ↓
Output
```

Machine Learning:

```text
Data + Output
      ↓
Algorithm Learns Rules
      ↓
Prediction
```

---

# Real-World Applications

## Netflix

Predicts:

* Movies you may like
* Personalized recommendations

---

## Amazon

Predicts:

* Products you may buy

---

## Banking

Predicts:

* Fraudulent transactions

---

## Healthcare

Predicts:

* Disease risk

---

## Education

Predicts:

* Student performance

---

# Key Learnings

✅ NumPy is the foundation of Data Science

✅ Mathematical operations are performed efficiently on arrays

✅ Learned 1D, 2D and Multi-Dimensional Arrays

✅ Pandas internally uses NumPy

✅ Installed Scikit-Learn

✅ Machine Learning identifies patterns from data

✅ Linear Regression predicts numbers

✅ Logistic Regression predicts categories

✅ Random Forest improves prediction accuracy

✅ K-Means groups similar data

---

# 🌟 Day 07 Outcome

Successfully learned:

* NumPy Basics
* Array Operations
* Multi-Dimensional Arrays
* Pandas & NumPy Relationship
* Machine Learning Fundamentals
* Scikit-Learn Installation
* Linear Regression
* Logistic Regression
* Random Forest
* K-Means Clustering

🚀 Ready for Day 08 - Machine Learning Practical Implementation!

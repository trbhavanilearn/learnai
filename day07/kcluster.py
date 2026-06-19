from sklearn.cluster import KMeans
import numpy as np
# Feature: [[Total Money Spent]]
X_shoppers = np.array([[15], [500], [22], [650]])
kmeans = KMeans(n_clusters=2, random_state=42).fit(X_shoppers)
print(kmeans.labels_)
#pridict kmeans

print(int(kmeans.predict([[550]])[0]))
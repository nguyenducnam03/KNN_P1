from sklearn import datasets
import numpy as np
import math
import operator

def calculate_distance(p1,p2):
	dimension = len(p1)
	distance = 0
	for i in range(dimension):
		distance += (p1[i] - p2[i])**2
	return math.sqrt(distance)

def get_k_neighbors(X_train,y_train,point,k):
	distances = []
	neighbors = []

	for i in range(len(X_train)):
		distance = calculate_distance(X_train[i],point)
		distances.append((distance, y_train[i]))

	#sort by distance
	distances.sort(key=operator.itemgetter(0))
	for i in range(k):
		neighbors.append(distances[i][1])
	return neighbors

def highest_votes(neighbors_labels):
	labels_count = [0,0,0]
	for label in neighbors_labels:
		labels_count[label] += 1
	return labels_count.index(max(labels_count))

def predict(X_train,y_train,point,k):
	neighbors_labels = get_k_neighbors(X_train,y_train,point,k)
	return highest_votes(neighbors_labels)

def accuracy_score(predict,ground_truth):
	total = len(predict)
	correct_count = 0
	for i in range(total):
		if predict[i] == ground_truth[i]:
			correct_count += 1
	return correct_count/total

iris = datasets.load_iris()
#include sepal length, sepal width, petal length,petal width
#include iris.data and iris.target
#Before divide into training and predict, we need random it, using shuffle

iris_X = iris.data
iris_y = iris.target

#shuffle by index
randIndex = np.arange(iris_X.shape[0])
np.random.shuffle(randIndex)
iris_X = iris_X[randIndex]
iris_y = iris_y[randIndex]

X_train = iris_X[:100,:]
X_test = iris_X[100:,:]
y_train = iris_y[:100]
y_test = iris_y[100:]
 
y_predict = []
k = 5

for test in X_test:
	y_predict.append(predict(X_train,y_train,test,k))

acc = accuracy_score(y_predict, y_test)
print(acc)

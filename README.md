# KNN_P1
Let's continue to study about KNN

So, KNN is a machine learning algorithm very popular, although it seem rarely used (my teacher said that and also think so:D).
The different between KNN and Kmean is very clearly, the all training point on the plot, graph right? Kmean will create some random point (with number k random points), and then assign traning point into group and clustering that, after that, at any time we need to predict, Kmean only need compare to that random point, so almost time of Kmean algorithm is used for training, predict take a little time of that.
In constract, in KNN, traning point is point with label, so don't take time for training, but, when we need to predict soemthing, we need calculate all distance from that point(point prediction) to all training point, that's problem, and with number k, we'll take k point with min distance from that, so it's take so much time for prediction, so I don't recommend to using this algorithm for predict, with small number of traning point, we can do that, but when that number increase into like 1000000 or maybe more,  everytime we need to predict, it's so possible if you can't wait for that.

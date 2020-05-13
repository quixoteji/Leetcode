# Feature Engineer

## Feature Scaling and Normalization

- standardization(z-score normalization)
- min-max scaling

1. Mean centering does not affect the covariance matrix
2. Scaling of variables affect the covariance matrix
3. Standardizing affects the covariance matrix

Scaling and Normalization works for linear regression, logistic regression, svm, and neural network, and does not works for trees.

### Why we use feature scaling?
1. Gradient Descent Based Algorithms : the features requre scaled data(step size in different dimensions)
2. Distance-Based Algorithms : feature scaling makes the distances are more comparable.
3. Tree-Based Algorithms : feature scaling does not effect splitting

## Text Feature

- Bag of Words
- TF-IDF = TF(t, d) * IDF(t)
- Topic Model
- Embedding(Word2Vec)
    - CBOW (context -> word)
    - Skip-gram (word -> context)
    


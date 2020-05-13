# Model Evaluation

## Metrics

Accuracy = n-correct / n-total
Precision = true positives / (true positives + false positives)
Recall = true positives / (true positives + false negatives)

**harmonic mean of precision and recall**
f1 = 1 /(1/Precision + 1/Recall)

### P-R curve
(Precision, Recall)

### ROC curve
(FPR = FP/N, TPR = TP/T)
(stable and robust over different dateset)
AUC(0.5-1)

## Overfit vs underfit

### overcome overfit
1. More data
2. Decrease the complexity of model
3. Regularization
4. Bagging methods

### overcome underfit
1. Add more features
2. Increase the complexity of model
3. Decrease the regulization parameters

## Generative Model vs Discriminative Model

posterior = likelihood * prior

### Generative Model
- Model class-conditional pdfs and prior probabilities
- 'Generative' since sampling can generate synthetic data points
- Popular models
    - Gaussians, Naive Bayes, Mixtures of multinomials
    - Mixtures of Gaussians, Mixtures of experts, HMM
    - Sigmodial belief networks, Bayesian networks, Markov random fields

### Discriminative Model
- Directly estimate posterior probabilities
- No attempt to model underlying probability distributions
- Focus computational resources on given task-better performance
- Popular
    - Logistic regression, SVN
    - Traditional neural networks, Nearest neighbor
    - Conditional Random Fields

Discriminative Model (conditional probability distribution)
Generative Model (joint probability distribution)

## Parametric vs Non-parametric Model

- Parametric Models assume some finite set of parameters \theta.
# Lab Assignment 2 — Post-Lab Write-Up

## Overview
This lab explored three core machine learning approaches—linear regression, k-Nearest Neighbors (k-NN), and Gaussian Naive Bayes—applied to real-world datasets. The goal was to understand model behavior, preprocessing requirements, and evaluation trade-offs through hands-on implementation from scratch.


## Part 2A: Linear Regression (Wine Dataset)

### Design and Approach
Linear regression was implemented using the least-squares method to predict citric acid concentration from physicochemical features. The analysis followed an incremental feature-selection strategy, starting with two features and progressively adding more to evaluate performance improvements.

### Model and Parameters
- Model: Linear regression (closed-form solution)
- Initial features: `alcohol`, `density`
- Additional features selected based on error reduction
- Error metric: Root Mean Squared Error (RMSE)

### Evaluation Results
| Model | Features | Error |
|------|----------|-------|
| Model 1 | alcohol, density | 0.1686 |
| Model 2 | alcohol, density,volatile_acidity | 0.1320 |
| Model 3 | alcohol, density,volatile_acidity , fixed_acidity | 0.1242 |
| Full Model | all features | 0.1055 |

Plots comparing predicted vs. actual values showed tighter alignment as features were added, though diminishing returns were observed.

### Reflection
This part demonstrated how feature selection significantly impacts regression performance and highlighted the risk of overfitting when adding too many features without justification.


## Part 2B: k-Nearest Neighbors Classification

### Design and Approach
A k-NN classifier was implemented from scratch and evaluated on two datasets: Lenses and Credit Approval. The Credit dataset required extensive preprocessing due to missing values and mixed data types.

### Model and Parameters
- Distance metric: Euclidean (L2)
- Values of $k$: 1, 3, 5, 7
- Preprocessing (Credit Approval):
  - Missing value imputation
  - Categorical encoding
  - Z-score normalization for numerical features

### Evaluation Results

#### Accuracy by Dataset
| Dataset | k=1 | k=3 | k=5 | k=7 |
|--------|-----|-----|-----|-----|
| Lenses | 1.0000 | 1.0000 | 0.5000 | 0.8333 |
| Credit Approval | 0.7464 | 0.7826 | 0.8043 | 0.7971 |

### Reflection
This section emphasized the bias–variance trade-off controlled by $k$. Small $k$ values were sensitive to noise, while moderate values generalized better, especially on larger datasets.


## Part 2C: Gaussian Naive Bayes (Spam Detection)

### Design and Approach
A Gaussian Naive Bayes classifier was implemented to detect spam emails using the Spambase dataset. Feature analysis was performed to identify the most discriminative features.

### Model and Parameters
- Model: Gaussian Naive Bayes
- Assumption: Conditional independence between features
- Evaluation metrics: Accuracy, Precision, Recall, F1-score

### Evaluation Results
| Metric | Value |
|--------|-------|
| Accuracy | 0.8217 |
| Precision | 0.7233 |
| Recall | 0.9385 |
| F1-Score | 0.8170 |

#### Confusion Matrix
\[
\begin{bmatrix}
390 & 140 \\
24 & 366
\end{bmatrix}
\]

### Top 5 Discriminative Features
1. `word_freq_your`
2. `word_freq_000`
3. `word_freq_remove`
4. `char_freq_$`
5. `word_freq_hp`

### Reflection
Despite its simplifying assumptions, Naive Bayes performed well due to strong individual feature signals. This part highlighted the importance of feature distributions and interpretability in probabilistic models.


## Overall Reflection
This lab reinforced how different modeling choices require different preprocessing strategies and evaluation perspectives. Implementing algorithms from scratch deepened my understanding of their mechanics, strengths, and limitations. The experience emphasized that simple models, when well-designed and evaluated, can be surprisingly effective on real-world data.

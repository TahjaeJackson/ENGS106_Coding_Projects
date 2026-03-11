# Report for Problem set 5

## Model Design

To restore the noisy Bayes’ Theorem image, I modeled the image using a Markov Random Field (MRF) defined over a grid of pixels. Each pixel is treated as a binary variable \( z_i \in \{-1, +1\} \) representing black or white. The observed noisy image is represented as \( y_i \). Each pixel interacts with its four immediate neighbors (up, down, left, right), creating a pairwise MRF. This neighbourhood structure encourages spatial smoothness, meaning nearby pixels are encouraged to take similar values. The goal is to find a configuration of \(z\) that minimizes an energy function representing both agreement with the observed noisy image and smoothness between neighboring pixels.

## Model and Algorithm

The model is defined using the following energy function:

\[
E(z|y) = -\beta \sum_{(i,j)} z_i z_j - \eta \sum_i z_i y_i - h \sum_i z_i
\]

where:
- \( \beta \) controls the strength of interaction between neighboring pixels.
- \( \eta \) controls how strongly the model trusts the observed noisy image.
- \( h \) is a bias term encouraging pixels toward a particular sign.

Lower energy configurations correspond to more probable clean images.

### Coordinate Descent Algorithm

To minimize the energy, coordinate descent was used:

1. Initialize the estimate \(z\) as the observed noisy image \(y\).
2. Iterate through each pixel in the image.
3. For each pixel \(z_i\), compute the energy of the current state.
4. Flip the pixel value and compute the new energy.
5. Keep the flip only if it decreases the energy.
6. Repeat until no further changes occur or a maximum number of iterations is reached.

This procedure progressively reduces the global energy of the image until convergence.


## Parameter Selection

We experimented with several parameter combinations:

| β | η |
|---|---|
| 1.5 | 2.5 |
| 2.0 | 3.0 |
| 2.5 | 3.5 |
| 5.0 | 6.0 |
| 10 | 9.0 |

These parameters affect the balance between smoothing and fidelity to the observed image.

- Larger $\beta $ encourages stronger agreement between neighboring pixels, which helps remove isolated noise.
- Larger η increases trust in the observed noisy image.

## Evaluation

The algorithm successfully removed a large portion of the noise while preserving the structure of the original text.

Observations:

- Lower β values left more noise in the image.
- Higher β values produced smoother images.
- Very large values may oversmooth the image and remove fine details.

The parameter pair **β = 2.0 and η = 3.0** produced the best visual result, balancing noise removal with preservation of the handwritten structure.

The coordinate descent algorithm typically converged within 5–8 iterations, as indicated by the decreasing number of pixel updates per iteration.

## Reflection

This lab demonstrated how probabilistic graphical models can be used for image restoration. The Markov Random Field formulation naturally captures spatial relationships between pixels, allowing the algorithm to leverage neighborhood structure to remove noise.Implementing coordinate descent showed how local updates can gradually improve a global objective function. It also highlighted the importance of selecting appropriate model parameters to balance smoothing and fidelity to observed data. This approach provides an intuitive and effective method for image denoising using probabilistic modeling.
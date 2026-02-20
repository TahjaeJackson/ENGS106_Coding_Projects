# ENGS 106 – Coding Assignment 3B  
# Transformer Implementation Post-Lab Write-Up

## 1. Model Description

### Architecture

For this assignment, I implemented a Transformer-based autoregressive language model. The architecture consists of:

- Token embedding layer  
- Sinoidal positional encoding  
- Multi-head masked self-attention  
- Feedforward neural network layers  
- Residual connections  
- Layer normalization  
- Final linear projection to vocabulary size  

The attention mechanism follows the scaled dot-product formulation:

$$
Attention(Q, K, V) = softmax((QK^T) / sqrt(d_k)) V
$$

A causal mask was applied to ensure that each token only attends to previous tokens in the sequence, preserving autoregressive behavior.

### Model Parameters and Justification

The key configuration parameters used in this model include:

- Embedding dimension (`n_embd`)  
- Number of attention heads (`n_head`)  
- Context length (`context_length`)  
- Dropout rate (`dropout`)  
- Learning rate (`learning_rate`)  
- Number of training iterations (`max_iters`)

Justification of parameter choices:

- The embedding dimension controls representational capacity. A moderate dimension provides expressive power while limiting overfitting and computational cost.
- Multiple attention heads allow the model to learn diverse relational patterns across tokens simultaneously.
- The context length determines how far back the model can attend. Increasing it improves modeling capacity but increases memory and compute cost.
- Dropout was included to regularize the model and reduce overfitting.
- The Adam optimizer was selected for its stability and effectiveness in training deep neural networks.

These parameters were selected to balance computational efficiency with sufficient modeling capacity for the dataset size.

## 2. Model Evaluation

The model was trained for 2000 iterations using the Adam optimizer. Training and validation losses were monitored throughout optimization.

Final results:

- Training Loss = 1.166  
- Validation Loss = 1.078  
- Total Trainable Parameters = 10,690,625  

Both training and validation loss decreased steadily over time, indicating stable optimization and successful learning of structure in the dataset.

The validation loss was slightly lower than the training loss at convergence. This is likely due to dropout being active during training but disabled during evaluation, which can cause the evaluation loss to appear slightly lower.

The relatively small gap between training and validation loss suggests good generalization and no significant overfitting within the training window.

## 3. Reflection

This lab deepened my understanding of the internal mechanics of the Transformer architecture. Implementing attention manually clarified:

- The importance of matrix multiplication (QK^T) versus elementwise operations.
- Why scaling by sqrt(d_k) stabilizes gradients.
- How causal masking enforces autoregressive sequence modeling.
- How multi-head attention concatenates independent attention subspaces before projection.

A key takeaway was how sensitive Transformer implementations are to tensor shapes, masking, and softmax dimensions. Small mistakes in these areas can completely destabilize training. This exercise strengthened both my conceptual understanding of attention mechanisms and my practical experience working with PyTorch tensor operations.

## 4. Jupyter Notebook

The complete Jupyter Notebook containing:

- Scaled dot-product attention implementation  
- Multi-head attention module  
- Sinusoidal positional encoding  
- Transformer blocks  
- Training loop and evaluation  

is included as part of this submission.

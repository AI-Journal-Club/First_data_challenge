# Our First data challenge
This is a test. The LSU Interdisciplinary AI-JC attempting the first hands-on activity.

# Distinguishing Ancient Chinese Written Characters
- Paper: https://www.nature.com/articles/s41597-024-02933-w
- GitHub (Oracle-MNIST): https://github.com/wm-bupt/oracle-mnist

# Steps:

- Data pre-processing
  - Download the data: [from this repo](https://drive.usercontent.google.com/download?id=1gPYAOc9CTvrUQFCASW3oz30lGdKBivn5&export=download&authuser=0) - Credits: Oracle-NMIST Team
  - Look at the data (inspect)
  - Process the data
 
- Data Set preparation

- NN set up
  - brainstorm on possible architectures
  - Start with the MNIST CNN (LeCun)
  - Modify to get better performances

______________________________________

# Results
Qur final architecture and results are reported in the images below.

**Our final test accuracy** (defined as the fraction of correct predictions on the total sample) is : **90.17%** (Pure LeNet was giving 52.20%)

## Observations
- Switching from Sigmoid() to ReLU() initially caused the loss to explode to ~10⁴.
  - Root cause: images were still in uint8 format.
  - Fix: convert to float32 and normalize pixel values to the range [0,1].

- Pooling comparison: 
  - Replacing AvgPool2d with MaxPool2d degraded performance. The model ran better with AvgPool2d, so we reverted the change.

- Dropout experiments to mitigate overfitting:  
  - Dropout(0.2): produced a small improvement.
  - Dropout(0.5): significantly improved generalization — reaching ~90% validation accuracy.

## What We Did Not Try

- Data augmentation (e.g., rotations, translations, flips, noise injection)
- Deeper architecture (e.g., additional convolutional blocks or more filters). 

Both directions could further improve performance.

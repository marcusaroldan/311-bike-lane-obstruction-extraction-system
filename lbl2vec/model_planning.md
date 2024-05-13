# Model Planning: Binary Classifier w/ Unbalanced Dataset
## Word Embedding / Representation:
    - TF-IDF:
    - Word Embedding from LM:
## Classifier Algorithm:
    - k-means:
    - SMOTE: http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-14-106
    - ROSE: https://journal.r-project.org/archive/2014-1/menardi-lunardon-torelli.pdf
## Evaluation Metric:
    - AUC (Area Under Curve): https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve
    - Cohen's Kappa: "https://en.wikipedia.org/wiki/Cohen's_kappa"

### Useful Resources:
    - Learning from Imbalanced Data: http://www.ele.uri.edu/faculty/he/PDFfiles/ImbalancedLearning.pdf
    - Subsampling For Class Imbalances: http://topepo.github.io/caret/subsampling-for-class-imbalances.html

## Strategies to deal with imbalanced data:
    - Resampling: change / manipulate the dataset so that there is more balance
        - Oversampling / Sampling with replacement: add copies / instances of minority observations to rebalance the dataset
        - Undersampling: removing majority observations to rebalance the dataset
        * Will probably be better to choose oversampling because of the size of our dataset (~10_000 total observations)
    - Generating Synthetic Samples: create new minority observations to rebalance the data
        - SMOTE (Synthetic Minority Oversampling Technique) - Python Implementation (https://github.com/fmfn/UnbalancedDataset)

### Classification Model Aspects
    - Majority Class: Illegal Parking reports not related to bike lane obstructions
    - Minority Class: Illegal Parking reports related to bike lane obstructions
        - Important that model is very good at identifying minority class observations

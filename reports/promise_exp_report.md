# PROMISE_exp NFR Experiment Report

## Dataset

- Raw file: `data\raw\PROMISE_exp.arff`
- Total requirements parsed: `969`
- NFR-only requirements used: `525`
- Task: 11-class NFR subtype classification.
- Note: PROMISE_exp is single-label, so this experiment is an initial operationalization of the multi-label research idea.

## Label Distribution

| label | count |
| --- | --- |
| security | 125 |
| usability | 85 |
| operational | 77 |
| performance | 67 |
| look_and_feel | 49 |
| availability | 31 |
| maintainability | 24 |
| scalability | 22 |
| fault_tolerance | 18 |
| legal | 15 |
| portability | 12 |

## Overall Results

| model | accuracy | macro_f1 | micro_f1 | weighted_f1 |
| --- | --- | --- | --- | --- |
| majority_baseline | 0.2405 | 0.0353 | 0.2405 | 0.0933 |
| tfidf_logistic_regression | 0.6899 | 0.6344 | 0.6899 | 0.6783 |
| quantum_inspired_projection | 0.7025 | 0.6748 | 0.7025 | 0.6967 |

## Interpretation

- `accuracy`: percentage of test requirements classified into the correct NFR subtype.
- `macro_f1`: average F1 across classes; important when some NFR labels have few samples.
- `micro_f1`: global F1 across all predictions; for single-label classification it is close to accuracy.
- `weighted_f1`: F1 weighted by class size.

## Quantum-Inspired Example Explanation

- Text: The product must comply with Sarbanes-Oxley.
- True label: `legal`
- Predicted label: `legal`

| label | token/phrase | contribution |
|---|---:|---:|
| legal | comply | 0.1018 |
| legal | comply with | 0.0937 |
| legal | with | 0.0411 |
| legal | must | 0.0247 |
| legal | must comply | 0.0194 |
| legal | the | 0.0186 |
| legal | the product | 0.0092 |
| legal | product | 0.0091 |

## Per-Class Reports

### majority_baseline

```text
                 precision    recall  f1-score   support

   availability       0.00      0.00      0.00         9
fault_tolerance       0.00      0.00      0.00         5
          legal       0.00      0.00      0.00         4
  look_and_feel       0.00      0.00      0.00        15
maintainability       0.00      0.00      0.00         7
    operational       0.00      0.00      0.00        23
    performance       0.00      0.00      0.00        20
    portability       0.00      0.00      0.00         4
    scalability       0.00      0.00      0.00         7
       security       0.24      1.00      0.39        38
      usability       0.00      0.00      0.00        26

       accuracy                           0.24       158
      macro avg       0.02      0.09      0.04       158
   weighted avg       0.06      0.24      0.09       158

```

### tfidf_logistic_regression

```text
                 precision    recall  f1-score   support

   availability       0.73      0.89      0.80         9
fault_tolerance       0.50      0.20      0.29         5
          legal       0.67      0.50      0.57         4
  look_and_feel       0.70      0.47      0.56        15
maintainability       0.60      0.86      0.71         7
    operational       0.58      0.48      0.52        23
    performance       0.84      0.80      0.82        20
    portability       0.67      0.50      0.57         4
    scalability       0.71      0.71      0.71         7
       security       0.78      0.92      0.84        38
      usability       0.55      0.62      0.58        26

       accuracy                           0.69       158
      macro avg       0.67      0.63      0.63       158
   weighted avg       0.68      0.69      0.68       158

```

### quantum_inspired_projection

```text
                 precision    recall  f1-score   support

   availability       0.80      0.89      0.84         9
fault_tolerance       1.00      0.20      0.33         5
          legal       0.75      0.75      0.75         4
  look_and_feel       0.86      0.40      0.55        15
maintainability       0.83      0.71      0.77         7
    operational       0.67      0.61      0.64        23
    performance       0.83      0.75      0.79        20
    portability       1.00      0.50      0.67         4
    scalability       0.71      0.71      0.71         7
       security       0.80      0.95      0.87        38
      usability       0.43      0.62      0.51        26

       accuracy                           0.70       158
      macro avg       0.79      0.64      0.67       158
   weighted avg       0.74      0.70      0.70       158

```

# PROMISE_exp NFR Experiment Report

## Dataset

- Raw file: `data\raw\Promise+.arff`
- Total requirements parsed: `2708`
- NFR-only requirements used: `894`
- Task: 11-class NFR subtype classification.
- Note: PROMISE_exp is single-label, so this experiment is an initial operationalization of the multi-label research idea.

## Label Distribution

| label | count |
| --- | --- |
| legal | 194 |
| usability | 127 |
| security | 112 |
| performance | 96 |
| operational | 80 |
| scalability | 73 |
| portability | 64 |
| maintainability | 51 |
| availability | 40 |
| look_and_feel | 40 |
| fault_tolerance | 17 |

## Overall Results

| model | accuracy | macro_f1 | micro_f1 | weighted_f1 |
| --- | --- | --- | --- | --- |
| majority_baseline | 0.2193 | 0.0327 | 0.2193 | 0.0789 |
| tfidf_logistic_regression | 0.7100 | 0.6744 | 0.7100 | 0.7067 |
| quantum_inspired_projection | 0.6914 | 0.6821 | 0.6914 | 0.6927 |

## Interpretation

- `accuracy`: percentage of test requirements classified into the correct NFR subtype.
- `macro_f1`: average F1 across classes; important when some NFR labels have few samples.
- `micro_f1`: global F1 across all predictions; for single-label classification it is close to accuracy.
- `weighted_f1`: F1 weighted by class size.

## Quantum-Inspired Example Explanation

- Text: The choice of how to submit the VCD package to the contracting authority MUST be the one that is preferred by the economic operator.
- True label: `legal`
- Predicted label: `legal`

| label | token/phrase | contribution |
|---|---:|---:|
| legal | the | 0.0550 |
| legal | vcd | 0.0249 |
| legal | must be | 0.0187 |
| legal | must | 0.0171 |
| legal | to | 0.0160 |
| legal | package | 0.0119 |
| legal | of | 0.0116 |
| legal | economic | 0.0098 |

## Per-Class Reports

### majority_baseline

```text
                 precision    recall  f1-score   support

   availability       0.00      0.00      0.00        12
fault_tolerance       0.00      0.00      0.00         5
          legal       0.22      1.00      0.36        59
  look_and_feel       0.00      0.00      0.00        12
maintainability       0.00      0.00      0.00        15
    operational       0.00      0.00      0.00        24
    performance       0.00      0.00      0.00        29
    portability       0.00      0.00      0.00        19
    scalability       0.00      0.00      0.00        22
       security       0.00      0.00      0.00        34
      usability       0.00      0.00      0.00        38

       accuracy                           0.22       269
      macro avg       0.02      0.09      0.03       269
   weighted avg       0.05      0.22      0.08       269

```

### tfidf_logistic_regression

```text
                 precision    recall  f1-score   support

   availability       1.00      0.83      0.91        12
fault_tolerance       0.50      0.20      0.29         5
          legal       0.83      0.92      0.87        59
  look_and_feel       0.82      0.75      0.78        12
maintainability       0.53      0.60      0.56        15
    operational       0.74      0.71      0.72        24
    performance       0.62      0.45      0.52        29
    portability       0.85      0.58      0.69        19
    scalability       0.86      0.82      0.84        22
       security       0.58      0.65      0.61        34
      usability       0.56      0.71      0.63        38

       accuracy                           0.71       269
      macro avg       0.72      0.66      0.67       269
   weighted avg       0.72      0.71      0.71       269

```

### quantum_inspired_projection

```text
                 precision    recall  f1-score   support

   availability       0.90      0.75      0.82        12
fault_tolerance       0.75      0.60      0.67         5
          legal       0.88      0.90      0.89        59
  look_and_feel       0.69      0.75      0.72        12
maintainability       0.53      0.60      0.56        15
    operational       0.73      0.67      0.70        24
    performance       0.67      0.41      0.51        29
    portability       0.83      0.53      0.65        19
    scalability       0.90      0.82      0.86        22
       security       0.56      0.56      0.56        34
      usability       0.47      0.74      0.58        38

       accuracy                           0.69       269
      macro avg       0.72      0.67      0.68       269
   weighted avg       0.72      0.69      0.69       269

```

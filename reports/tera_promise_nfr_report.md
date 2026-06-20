# PROMISE_exp NFR Experiment Report

## Dataset

- Raw file: `data\raw\data\se-requirements-classification\0-datasets\tera-PROMISE NFR\nfr.arff`
- Total requirements parsed: `625`
- NFR-only requirements used: `370`
- Task: 11-class NFR subtype classification.
- Note: PROMISE_exp is single-label, so this experiment is an initial operationalization of the multi-label research idea.

## Label Distribution

| label | count |
| --- | --- |
| usability | 67 |
| security | 66 |
| operational | 62 |
| performance | 54 |
| look_and_feel | 38 |
| availability | 21 |
| scalability | 21 |
| maintainability | 17 |
| legal | 13 |
| fault_tolerance | 10 |
| portability | 1 |

## Overall Results

| model | accuracy | macro_f1 | micro_f1 | weighted_f1 |
| --- | --- | --- | --- | --- |
| majority_baseline | 0.1802 | 0.0305 | 0.1802 | 0.0550 |
| tfidf_logistic_regression | 0.7297 | 0.6998 | 0.7297 | 0.7277 |
| quantum_inspired_projection | 0.7207 | 0.6886 | 0.7207 | 0.7160 |

## Interpretation

- `accuracy`: percentage of test requirements classified into the correct NFR subtype.
- `macro_f1`: average F1 across classes; important when some NFR labels have few samples.
- `micro_f1`: global F1 across all predictions; for single-label classification it is close to accuracy.
- `weighted_f1`: F1 weighted by class size.

## Quantum-Inspired Example Explanation

- Text: The website shall protect itself from intentional abuse and notify the administrator at all occurrences.
- True label: `security`
- Predicted label: `look_and_feel`

| label | token/phrase | contribution |
|---|---:|---:|
| look_and_feel | the | 0.0392 |
| look_and_feel | the website | 0.0285 |
| look_and_feel | website | 0.0285 |
| look_and_feel | and | 0.0198 |
| look_and_feel | website shall | 0.0170 |
| look_and_feel | all | 0.0147 |
| look_and_feel | at | 0.0110 |
| look_and_feel | shall | 0.0102 |

## Per-Class Reports

### majority_baseline

```text
                 precision    recall  f1-score   support

   availability       0.00      0.00      0.00         6
fault_tolerance       0.00      0.00      0.00         3
          legal       0.00      0.00      0.00         4
  look_and_feel       0.00      0.00      0.00        12
maintainability       0.00      0.00      0.00         5
    operational       0.00      0.00      0.00        19
    performance       0.00      0.00      0.00        16
    portability       0.00      0.00      0.00         0
    scalability       0.00      0.00      0.00         6
       security       0.00      0.00      0.00        20
      usability       0.18      1.00      0.31        20

       accuracy                           0.18       111
      macro avg       0.02      0.09      0.03       111
   weighted avg       0.03      0.18      0.06       111

```

### tfidf_logistic_regression

```text
                 precision    recall  f1-score   support

   availability       1.00      1.00      1.00         6
fault_tolerance       1.00      0.33      0.50         3
          legal       1.00      0.75      0.86         4
  look_and_feel       0.64      0.75      0.69        12
maintainability       0.33      0.20      0.25         5
    operational       0.62      0.68      0.65        19
    performance       0.85      0.69      0.76        16
    portability       0.00      0.00      0.00         0
    scalability       0.62      0.83      0.71         6
       security       0.94      0.80      0.86        20
      usability       0.64      0.80      0.71        20

       accuracy                           0.73       111
      macro avg       0.70      0.62      0.64       111
   weighted avg       0.75      0.73      0.73       111

```

### quantum_inspired_projection

```text
                 precision    recall  f1-score   support

   availability       1.00      1.00      1.00         6
fault_tolerance       1.00      0.33      0.50         3
          legal       1.00      0.50      0.67         4
  look_and_feel       0.64      0.75      0.69        12
maintainability       0.50      0.20      0.29         5
    operational       0.58      0.74      0.65        19
    performance       0.79      0.69      0.73        16
    portability       0.00      0.00      0.00         0
    scalability       0.83      0.83      0.83         6
       security       0.93      0.70      0.80        20
      usability       0.63      0.85      0.72        20

       accuracy                           0.72       111
      macro avg       0.72      0.60      0.63       111
   weighted avg       0.75      0.72      0.72       111

```

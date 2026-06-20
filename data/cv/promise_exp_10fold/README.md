# PROMISE_exp 10-Fold Cross-Validation Dataset

This folder contains stratified cross-validation splits for the PROMISE_exp NFR 11-class dataset.

## Files

- `fold_assignments.csv`: all samples with their assigned fold.
- `fold_summary.csv`: train/test row counts for each fold.
- `fold_label_distribution.csv`: label distribution in each test fold.
- `fold_01/train.csv`, `fold_01/test.csv`, ..., `fold_10/train.csv`, `fold_10/test.csv`: ready-to-run train/test splits.

## How to Use

For fold 1:

```text
train: data/cv/promise_exp_10fold/fold_01/train.csv
test : data/cv/promise_exp_10fold/fold_01/test.csv
```

Repeat for folds 1 to 10, then average the metrics.

## Fold Summary

| fold | train_rows | test_rows | train_labels | test_labels |
| --- | --- | --- | --- | --- |
| 1 | 472 | 53 | 11 | 11 |
| 2 | 472 | 53 | 11 | 11 |
| 3 | 472 | 53 | 11 | 11 |
| 4 | 472 | 53 | 11 | 11 |
| 5 | 472 | 53 | 11 | 11 |
| 6 | 473 | 52 | 11 | 11 |
| 7 | 473 | 52 | 11 | 11 |
| 8 | 473 | 52 | 11 | 11 |
| 9 | 473 | 52 | 11 | 11 |
| 10 | 473 | 52 | 11 | 11 |

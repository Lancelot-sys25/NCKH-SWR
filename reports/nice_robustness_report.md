# NICE Robustness and Explainability Comparison Report

## Setup

- Dataset: `data\raw\PROMISE-relabeled-NICE.csv`
- Split: same 70/30 train-test seed and internal validation protocol as the single-split experiment.
- Deletion comparison: contrastive projection intrinsic contributions versus SVM TF-IDF coefficient contributions.
- Bootstrap: paired bootstrap over held-out test requirements for Macro-F1 differences.

## Deletion Comparison Summary

| explainer | top_k | random_trials | evaluated_label_assignments | mean_base_score | mean_top_deleted_score | mean_random_deleted_score | mean_top_score_drop | mean_random_score_drop | drop_ratio_top_vs_random |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| contrastive_projection_intrinsic | 3 | 50 | 158 | 0.4786 | 0.4481 | 0.4727 | 0.0305 | 0.0059 | 5.1366 |
| svm_tfidf_coefficients | 3 | 50 | 158 | 0.4925 | 0.4058 | 0.4713 | 0.0867 | 0.0212 | 4.0892 |

## Paired Bootstrap Summary

| comparison | iterations | observed_macro_f1_difference | ci95_low | ci95_high | bootstrap_p_two_sided |
| --- | --- | --- | --- | --- | --- |
| hybrid_quantum_svm_fusion_vs_tfidf_linear_svm | 2000 | 0.0071 | -0.0094 | 0.0229 | 0.4070 |
| hybrid_quantum_svm_fusion_vs_tfidf_logistic_regression | 2000 | 0.0010 | -0.0217 | 0.0223 | 0.9820 |
| hybrid_quantum_svm_fusion_vs_quantum_contrastive_projection | 2000 | 0.0816 | 0.0330 | 0.1250 | 0.0000 |

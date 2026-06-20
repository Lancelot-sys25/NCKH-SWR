# Quantum-Inspired NFR Classification Research Project

De tai: **Explainable Quantum-Inspired Multi-label Classification of Non-Functional Requirements**

Project nay la khung nghien cuu va thuc nghiem cho huong ap dung mo hinh quantum-inspired vao Requirements Engineering, tap trung vao phan loai yeu cau phi chuc nang (NFR) va giai thich ket qua phan loai.

## Muc tieu

Xay dung va danh gia mot mo hinh bieu dien requirement nhu mot semantic state. Mo hinh tinh muc do lien quan cua requirement voi cac nhan NFR nhu security, performance, usability, availability, maintainability, operational, portability, scalability.

## Cau truc thu muc

```text
quantum_re_nfr_project/
  data/
    raw/                      # Du lieu goc
    processed/                # Du lieu da xu ly
  docs/                       # De cuong, ke hoach, outline paper
  reports/                    # Bao cao ket qua thuc nghiem
  scripts/                    # Script chay demo va experiment
  src/quantum_re_nfr/         # Source code chinh
  tests/                      # Test
  pyproject.toml
  requirements.txt
  README.md
```

## Cai dat

May nay da co san moi truong ao `.venv`. Neu mo PowerShell tai thu muc project, chay:

```powershell
cd D:\ProjectSWR\quantum_re_nfr_project
.\.venv\Scripts\Activate.ps1
```

Neu can cai lai tu dau:

```powershell
cd D:\ProjectSWR\quantum_re_nfr_project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## Chay demo voi du lieu mau

```powershell
python scripts\run_quantum_inspired.py --sample
python scripts\run_baseline.py --sample
python -m pytest tests
```

## Chay thuc nghiem that voi PROMISE_exp

Dataset da duoc tai vao:

```text
data/raw/PROMISE_exp.arff
```

Chay lai toan bo experiment:

```powershell
python scripts\run_promise_experiment.py
```

Ket qua duoc ghi vao:

```text
reports/promise_exp_report.md
reports/promise_exp_metrics.csv
data/processed/promise_exp_nfr_11class.csv
```

## Dataset cross-validation

Bo du lieu 10-fold cross-validation da duoc tao tai:

```text
data/cv/promise_exp_10fold
```

Ben trong moi fold co:

```text
fold_01/train.csv
fold_01/test.csv
...
fold_10/train.csv
fold_10/test.csv
```

Cac file tong hop:

```text
data/cv/promise_exp_10fold/fold_assignments.csv
data/cv/promise_exp_10fold/fold_summary.csv
data/cv/promise_exp_10fold/fold_label_distribution.csv
```

Neu muon tao lai dataset cross-validation:

```powershell
python scripts\create_cv_dataset.py
```

## Ket qua thuc nghiem hien tai

Experiment hien tai dung bai toan **11-class NFR subtype classification** tren PROMISE_exp.

| model | accuracy | macro_f1 | micro_f1 | weighted_f1 |
| --- | ---: | ---: | ---: | ---: |
| majority_baseline | 0.2405 | 0.0353 | 0.2405 | 0.0933 |
| tfidf_logistic_regression | 0.6899 | 0.6344 | 0.6899 | 0.6783 |
| quantum_inspired_projection | 0.7025 | 0.6748 | 0.7025 | 0.6967 |

Doc bao cao chi tiet tai:

```text
reports/promise_exp_report.md
```

## Y nghia ket qua

- `accuracy`: ti le requirement duoc phan loai dung.
- `macro_f1`: F1 trung binh tren tung nhan NFR, rat quan trong khi du lieu mat can bang.
- `micro_f1`: F1 tong the tren toan bo mau test.
- `weighted_f1`: F1 co tinh den so luong mau cua tung nhan.

Trong lan chay hien tai, prototype `quantum_inspired_projection` dat ket qua cao hon baseline `tfidf_logistic_regression` mot chut. Day la ket qua ban dau, chua du de ket luan khoa hoc manh; de viet paper can chay them cross-validation, them baseline SVM/Transformer, va ablation study.

## Ghi chu nghien cuu

PROMISE_exp la dataset single-label. Vi vay experiment nay la buoc khoi dau cho bai toan NFR subtype classification. De dung dung de tai multi-label, buoc tiep theo nen bo sung NICE/PROMISE_exp co explanation hoac tao mapping multi-label co kiem chung.

## Thuc nghiem dung de tai multi-label voi NICE

Dataset NICE da duoc tai vao:

```text
data/raw/PROMISE-relabeled-NICE.csv
```

Dataset nay co cac cot nhan nhi phan cho tung lop NFR, vi vay phu hop hon voi de tai:

```text
Explainable Quantum-Inspired Multi-label Classification of Non-Functional Requirements
```

Chay mot lan train/validation/test:

```powershell
python scripts\run_nice_multilabel_experiment.py
```

Ket qua duoc ghi vao:

```text
reports/nice_multilabel_report.md
reports/nice_multilabel_metrics.csv
data/processed/nice_multilabel_nfr.csv
```

Ket qua hien tai:

| model | threshold | micro_f1 | macro_f1 | hamming_loss | LRAP |
| --- | ---: | ---: | ---: | ---: | ---: |
| label_frequency_baseline | 0.05 | 0.2221 | 0.2166 | 0.8751 | 0.4183 |
| tfidf_logistic_regression | 0.45 | 0.6299 | 0.5266 | 0.0901 | 0.7861 |
| tfidf_linear_svm | 0.45 | 0.6212 | 0.5205 | 0.0877 | 0.7843 |
| quantum_inspired_projection | 0.85 | 0.6076 | 0.5618 | 0.0980 | 0.7694 |

Trong split don nay, quantum-inspired co `macro_f1` cao nhat, nhung Logistic/SVM van tot hon o `micro_f1`, `hamming_loss`, va `LRAP`.

## 5-fold cross-validation voi NICE

Chay:

```powershell
python scripts\run_nice_cv_experiment.py
```

Ket qua duoc ghi vao:

```text
reports/nice_cv_report.md
reports/nice_cv_summary.csv
reports/nice_cv_fold_results.csv
```

Ket qua trung binh 5-fold hien tai:

| model | micro_f1_mean | macro_f1_mean | hamming_loss_mean | LRAP_mean |
| --- | ---: | ---: | ---: | ---: |
| tfidf_linear_svm | 0.6821 | 0.6049 | 0.0764 | 0.8056 |
| tfidf_logistic_regression | 0.6787 | 0.5977 | 0.0759 | 0.7990 |
| quantum_inspired_projection | 0.5931 | 0.5490 | 0.1096 | 0.7830 |
| label_frequency_baseline | 0.2328 | 0.2083 | 0.7927 | 0.4059 |

Ket luan trung thuc: prototype quantum-inspired projection hien tai **chua tot hon SVM/Logistic tren 5-fold cross-validation**. Day la ket qua quan trong: project da co pipeline thuc nghiem dung, nhung mo hinh quantum can cai tien them truoc khi co the ket luan la tot hon baseline.

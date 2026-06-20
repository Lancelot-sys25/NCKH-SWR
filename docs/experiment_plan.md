# Experiment Plan

## Giai đoạn 1: Chuẩn hóa dữ liệu

1. Tải dataset PROMISE/NICE.
2. Chuẩn hóa cột `text`.
3. Chuẩn hóa taxonomy nhãn NFR.
4. Chia train/validation/test theo cùng seed.
5. Kiểm tra mất cân bằng nhãn.

## Giai đoạn 2: Baseline

Baseline tối thiểu:

- TF-IDF + One-vs-Rest Logistic Regression
- TF-IDF + One-vs-Rest Linear SVM
- Random Forest multi-label

Baseline nâng cao:

- BERT multi-label
- RoBERTa multi-label
- DistilBERT multi-label
- LLM zero-shot/few-shot

## Giai đoạn 3: Quantum-inspired model

Phiên bản ban đầu:

- TF-IDF hoặc embedding làm vector đầu vào.
- Chuẩn hóa vector thành semantic state.
- Học label projection matrix.
- Tính xác suất nhãn bằng squared projection amplitude.

Phiên bản mở rộng:

- Thêm interference matrix giữa các nhãn.
- Thêm context projection theo nhóm NFR.
- Thêm explainability score theo token/feature contribution.

## Giai đoạn 4: Đánh giá

Metric chính:

- Micro-F1
- Macro-F1
- Hamming loss
- Label Ranking Average Precision

Metric phụ:

- Per-label F1
- Confusion giữa các nhãn gần nhau
- Stability under random seed

## Giai đoạn 5: Ablation study

So sánh:

- Không interference
- Có interference
- Không context projection
- Có context projection
- TF-IDF input
- Embedding input

## Giai đoạn 6: Viết paper

Các phần cần có:

- Problem motivation
- Quantum-inspired formulation
- Dataset and baseline
- Experiment setup
- Results
- Ablation study
- Explainability case study
- Threats to validity


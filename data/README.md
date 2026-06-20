# Data Guide

Không commit trực tiếp dataset nếu license không cho phép.

## Dataset nên tải

1. NICE: Non-Functional Requirements Identification, Classification, and Explanation
2. PROMISE / Tera-PROMISE NFR
3. PROMISE_exp
4. Software Requirements Classification merged datasets

## Định dạng CSV chuẩn cho project

File xử lý nên có dạng:

```csv
id,text,security,performance,usability,reliability,maintainability,portability,operational,scalability
REQ_001,"The system shall encrypt user passwords.",1,0,0,0,0,0,0,0
```

Trong đó:

- `id`: mã requirement
- `text`: nội dung requirement
- Các cột còn lại: nhãn đa lớp, giá trị `0` hoặc `1`


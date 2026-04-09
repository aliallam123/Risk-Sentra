Ground truth for **Scope & Deliverables** contains **8 risks**. 

### Ground truth list

1. Integration scope growth beyond baseline
2. Finance DD delay compressing Build/SIT
3. Data migration backlog & poor data quality
4. Management reserve depletion
5. Programme FTE shortfall
6. Deemed acceptance reduces QA rigour
7. German e-invoicing regulatory dependency
8. Regional readiness below threshold

---

# Model output

**Extracted = 5**

### Correct matches

| Model Risk                | Ground Truth |
| ------------------------- | ------------ |
| Data migration complexity | ✔ SD-03      |
| Finance DD delay          | ✔ SD-02      |
| Integration scope creep   | ✔ SD-01      |
| Regional change readiness | ✔ SD-08      |

**Correct = 4**

---

### False positives

Not in this document’s ground truth:

* SI resource quality and retention

**False = 1**

---

### Missing risks

Ground truth risks not detected:

* Management reserve depletion
* Programme FTE shortfall
* Deemed acceptance reduces QA rigour
* German e-invoicing dependency

**Missing = 4**

---

# Evaluation row

| Document             | True | Extracted | Correct | Missing | False |
| -------------------- | ---- | --------- | ------- | ------- | ----- |
| Scope & Deliverables | 8    | 5         | 4       | 4       | 1     |

---

# Metrics

Precision
4 / 5 = **0.80**

Recall
4 / 8 = **0.50**

F1
≈ **0.62**

---


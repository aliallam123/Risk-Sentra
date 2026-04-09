Ground truth for **PID** contains **8 risks**. 

### Ground truth list

1. Data migration complexity and reconciliation failures
2. Finance Detailed Design delay compressing Build/SIT
3. Integration scope creep beyond baseline
4. Management reserve depletion risk
5. FTE shortfall (–5 resources)
6. Optimistic programme RAG reporting
7. Low regional change readiness (Germany/Singapore)
8. Unformalised SI cost overrun risk

---

# Model output

**Extracted = 6**

### Correct matches

| Model Risk                | Ground Truth |
| ------------------------- | ------------ |
| Data migration complexity | ✔ PID-01     |
| Finance DD delay          | ✔ PID-02     |
| Integration scope creep   | ✔ PID-03     |
| Regional change readiness | ✔ PID-07     |

**Correct = 4**

---

### False positives

Not in ground truth:

* SI resource retention
* Replacement consultants not onboarded

**False = 2**

---

### Missing risks

Ground truth risks not detected:

* Management reserve depletion
* FTE shortfall
* Optimistic programme RAG reporting
* SI cost overrun risk

**Missing = 4**

---

# Evaluation row

| Document | True | Extracted | Correct | Missing | False |
| -------- | ---- | --------- | ------- | ------- | ----- |
| PID      | 8    | 6         | 4       | 4       | 2     |

---

# Metrics

Precision
4 / 6 = **0.67**

Recall
4 / 8 = **0.50**

F1
≈ **0.57**

---

Ground truth for the **PID** contains **8 risks (PID-01 → PID-08)**. 

Your model extracted **5 risks**.

---

# Correct matches

| Model Output                                 | Ground Truth |
| -------------------------------------------- | ------------ |
| Poor legacy data quality / migration backlog | ✔ PID-01     |
| Delay in Finance Detailed Design             | ✔ PID-02     |
| Increase in integration scope                | ✔ PID-03     |
| Shortage of SI resources                     | ✔ PID-05     |
| Regional readiness below threshold           | ✔ PID-07     |

**Correct = 5**

---

# False positives

None.

**False = 0**

---

# Missing risks

Ground truth risks not detected:

* PID-04 Management reserve depletion risk
* PID-06 Optimistic programme RAG reporting
* PID-08 SI cost overrun risk

**Missing = 3**

---

# Experiment 2 result

| Document | True | Extracted | Correct | Missing | False |
| -------- | ---- | --------- | ------- | ------- | ----- |
| PID      | 8    | 5         | 5       | 3       | 0     |

---

# Metrics

Precision
5 / 5 = **1.00**

Recall
5 / 8 = **0.63**

F1
≈ **0.77**

---

Continue with the **same prompt** for the remaining documents.

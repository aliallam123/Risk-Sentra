For the **Scope & Deliverables document**:

Ground truth contains **8 risks (SD-01 → SD-08)**. 

Your model extracted **4 risks**.

---

# Correct matches

| Model Output                  | Ground Truth |
| ----------------------------- | ------------ |
| Increase in Integration Scope | ✔ SD-01      |
| Finance Delivery delay        | ✔ SD-02      |
| Management reserve reduced    | ✔ SD-04      |
| Staffing shortfall            | ✔ SD-05      |

**Correct = 4**

---

# False positives

None.

**False = 0**

---

# Missing risks

Ground truth risks not detected:

* SD-03 Data migration backlog
* SD-06 Deemed acceptance governance risk
* SD-07 German e-invoicing dependency
* SD-08 Regional readiness below threshold

**Missing = 4**

---

# Experiment 2 result

| Document             | True | Extracted | Correct | Missing | False |
| -------------------- | ---- | --------- | ------- | ------- | ----- |
| Scope & Deliverables | 8    | 4         | 4       | 4       | 0     |

---

# Metrics

Precision
4 / 4 = **1.00**

Recall
4 / 8 = **0.50**

F1
≈ **0.67**

---

Experiment 2 is now **fully complete for all 6 documents**.

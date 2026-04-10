Ground truth for the **Business Case** contains **8 risks (BC-01 → BC-08)**. 

Your model output extracted **2 risks**.

---

# Correct matches

| Model Risk                | Ground Truth |
| ------------------------- | ------------ |
| Integration scope creep   | ✔ BC-03      |
| Data migration complexity | ✔ BC-04      |

**Correct = 2**

---

# False positives

None.

**False = 0**

---

# Missing risks

Ground truth risks not detected:

* BC-01 Management reserve depletion before Month 24
* BC-02 SI forecast exceeds baseline by £800k
* BC-05 Finance DD delay compresses schedule
* BC-06 Benefits realisation plan not baselined
* BC-07 Assumption of no further scope growth may prove invalid
* BC-08 Over-optimistic payback period

**Missing = 6**

---

# Evaluation row (Experiment 2 – Haiku)

| Document      | True | Extracted | Correct | Missing | False |
| ------------- | ---- | --------- | ------- | ------- | ----- |
| Business Case | 8    | 2         | 2       | 6       | 0     |

---

# Metrics

Precision
2 / 2 = **1.00**

Recall
2 / 8 = **0.25**

F1
≈ **0.40**

---

# What this tells you

Claude Haiku is:

* **very precise**
* but **missing most risks**

Meaning it only detects **very obvious risks**.

This becomes useful later when you compare it with **Claude Sonnet**, which should detect more **implicit risks**.

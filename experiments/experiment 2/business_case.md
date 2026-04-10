Comparison with the **Business Case ground truth**:

Ground truth contains **8 risks (BC-01 → BC-08)**. 

---

# Correct matches

| Model Output                               | Ground Truth                                  |
| ------------------------------------------ | --------------------------------------------- |
| Integration complexity higher than planned | ✔ BC-03 Integration scope creep               |
| Delay in Finance Detailed Design recovery  | ✔ BC-05 Finance DD delay                      |
| Consumption of management reserve          | ✔ BC-01 Management reserve depletion          |
| Scope growth beyond the current plan       | ✔ BC-07 Assumption of no further scope growth |

**Correct = 4**

---

# False positives

| Model Output                      | Reason                            |
| --------------------------------- | --------------------------------- |
| Resource shortfall in the program | Not in Business Case ground truth |

**False = 1**

---

# Missing risks

Ground truth risks not detected:

* BC-02 SI forecast exceeds baseline by £800k
* BC-04 Data migration complexity threatens benefits realisation
* BC-06 Benefits realisation plan not formally baselined
* BC-08 Over-optimistic payback period

**Missing = 4**

---

# Experiment 2 results (No Retrieval)

| Document      | True | Extracted | Correct | Missing | False |
| ------------- | ---- | --------- | ------- | ------- | ----- |
| Business Case | 8    | 5         | 4       | 4       | 1     |

---

# Metrics

Precision
4 / 5 = **0.80**

Recall
4 / 8 = **0.50**

F1
≈ **0.62**

---

# Important insight for your dissertation

Compared to your **Experiment 1 baseline**, the model:

* detected **more risks**
* but introduced **hallucination**

This supports your methodology hypothesis that **removing retrieval increases noise and reduces precision**.

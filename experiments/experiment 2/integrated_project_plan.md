Ground truth for the **Integrated Project Plan** contains **5 risks (IPP-01 → IPP-05)**.

Your model extracted **2 risks**.

---

# Correct matches

| Model Output                        | Ground Truth           |
| ----------------------------------- | ---------------------- |
| Delay in Finance Detailed Design    | ✔ Finance DD delay     |
| Potential delay in overall timeline | ✔ schedule compression |

**Correct = 2**

---

# False positives

None.

**False = 0**

---

# Missing risks

Ground truth risks not detected:

* Data migration complexity risk
* Integration scope creep
* Change readiness risk

**Missing = 3**

---

# Experiment 2 results

| Document                | True | Extracted | Correct | Missing | False |
| ----------------------- | ---- | --------- | ------- | ------- | ----- |
| Integrated Project Plan | 5    | 2         | 2       | 3       | 0     |

---

# Metrics

Precision
2 / 2 = **1.00**

Recall
2 / 5 = **0.40**

F1
≈ **0.57**

---

Continue running **the same prompt for the remaining documents** in Playground.

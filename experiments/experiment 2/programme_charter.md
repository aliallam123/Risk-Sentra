This output corresponds to the **Programme Charter**.

Ground truth contains **15 risks (GR-01 → GR-15)**. 

Your model extracted **8 risks**.

---

# Correct matches

| Model Output                        | Ground Truth |
| ----------------------------------- | ------------ |
| Legacy data migration complexity    | ✔ GR-01      |
| Finance DD delay                    | ✔ GR-02      |
| Integration scope increase          | ✔ GR-03      |
| Regional readiness below threshold  | ✔ GR-04      |
| SI resource retention issues        | ✔ GR-05      |
| Workday HR feed delay               | ✔ GR-14      |
| German e-invoicing regulation delay | ✔ GR-12      |
| Finance BPO availability constraint | ✔ GR-11      |

**Correct = 8**

---

# False positives

None.

**False = 0**

---

# Missing risks

Ground truth risks not detected:

* GR-06 optimistic programme RAG reporting
* GR-07 management reserve depletion and cost overrun
* GR-08 CIO sponsor disengagement
* GR-09 benefits realisation plan not baselined
* GR-10 missing internal audit sign-off
* GR-13 data migration recruitment vacancy
* GR-15 end-user training plan not published

**Missing = 7**

---

# Experiment 2 result

| Document          | True | Extracted | Correct | Missing | False |
| ----------------- | ---- | --------- | ------- | ------- | ----- |
| Programme Charter | 15   | 8         | 8       | 7       | 0     |

---

# Metrics

Precision
8 / 8 = **1.00**

Recall
8 / 15 = **0.53**

F1
≈ **0.69**

---

You have now run **Experiment 2 on all Category 1 artefacts**, so this experiment is essentially **complete**.

This output corresponds to the **SoW document**.

Ground truth contains **15 risks (SR-01 → SR-15)**. 

Your model extracted **8 risks**.

---

# Correct matches

| Model Output                                  | Ground Truth |
| --------------------------------------------- | ------------ |
| Integration scope increase                    | ✔ SR-02      |
| Finance Detailed Design delay                 | ✔ SR-03      |
| SI resource shortfall                         | ✔ SR-06      |
| Poor legacy data quality / migration backlog  | ✔ SR-01      |
| Quality plan not published                    | ✔ SR-05      |
| External dependency (German e-invoicing spec) | ✔ SR-11      |

**Correct = 6**

---

# False positives

| Model Output                        | Reason                                            |
| ----------------------------------- | ------------------------------------------------- |
| Stakeholder availability constraint | Not a defined SoW risk                            |
| Regional readiness below threshold  | Appears in other artefacts but not SoW answer key |

**False = 2**

---

# Missing risks

Ground truth risks not detected:

* SR-04 Deemed acceptance clause risk
* SR-07 Amendment approval governance breach
* SR-08 T&M change request incentive risk
* SR-09 Lack of resource-level transparency
* SR-10 Warranty clock risk
* SR-12 Mutual dependency / schedule relief risk
* SR-13 Unnamed leads for key services
* SR-14 Assumption management gap
* SR-15 Rate card escalation risk

**Missing = 9**

---

# Experiment 2 result

| Document | True | Extracted | Correct | Missing | False |
| -------- | ---- | --------- | ------- | ------- | ----- |
| SoW      | 15   | 8         | 6       | 9       | 2     |

---

# Metrics

Precision
6 / 8 = **0.75**

Recall
6 / 15 = **0.40**

F1
≈ **0.52**

---

You are now **very close to finishing Experiment 2**.
Just run the prompt on the **remaining Category 1 artefacts** and record the same metrics.

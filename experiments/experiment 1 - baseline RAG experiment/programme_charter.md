Ground truth for **Programme Charter** contains **15 risks**. 

---

# Model output

**Extracted = 6**

### Correct matches

| Model Risk                                     | Ground Truth |
| ---------------------------------------------- | ------------ |
| Data cleansing backlog / data migration issues | ✔ GR-01      |
| Finance Detailed Design delay                  | ✔ GR-02      |
| Regional change readiness below threshold      | ✔ GR-04      |
| SI resource retention issues                   | ✔ GR-05      |
| No local change managers                       | ✔ GR-11      |

**Correct = 5**

---

### False positives

Not present as a defined risk in the ground truth:

* BPO availability constrained

**False = 1**

---

### Missing risks

Ground truth risks not detected (10):

* Integration scope creep
* Programme RAG misrepresentation
* Management reserve depletion
* CIO low attendance at governance
* Benefits plan not baselined
* Audit sign-off missing
* German e-invoicing dependency
* Data migration recruitment vacancy
* Workday HR feed delay
* End-user training not published

**Missing = 10**

---

# Evaluation row

| Document          | True | Extracted | Correct | Missing | False |
| ----------------- | ---- | --------- | ------- | ------- | ----- |
| Programme Charter | 15   | 6         | 5       | 10      | 1     |

---

# Metrics

Precision
5 / 6 = **0.83**

Recall
5 / 15 = **0.33**

F1
≈ **0.47**

--

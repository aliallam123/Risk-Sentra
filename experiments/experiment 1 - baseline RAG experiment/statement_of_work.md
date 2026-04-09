Ground truth for this **SoW artefact** contains **15 risks (SR-01 → SR-15)**. 

Your model output extracted **5 risks**.

---

# Correct matches

| Model Risk                    | Ground Truth |
| ----------------------------- | ------------ |
| Integration scope increase    | ✔ SR-02      |
| Finance Detailed Design delay | ✔ SR-03      |
| Data migration complexity     | ✔ SR-01      |

**Correct = 3**

---

# False positives

Not present in the SoW ground truth:

* Regional change readiness (this belongs to another artefact)
* Programme budget £18–25m

**False = 2**

---

# Missing risks

Ground truth risks not detected:

* SR-04 Deemed acceptance risk
* SR-05 Programme Quality Plan overdue
* SR-06 SI resource shortfall enforcement failure
* SR-07 Amendment approval hierarchy breach
* SR-08 Uncapped change request incentives
* SR-09 Lack of resource-level transparency
* SR-10 Warranty period tied to deemed acceptance
* SR-11 German e-invoicing dependency
* SR-12 Client responsibilities failures / schedule relief risk
* SR-13 Unnamed workstream leads
* SR-14 No process for assumption revalidation
* SR-15 Rate card escalation not formalised

**Missing = 12**

---

# Evaluation row

| Document | True | Extracted | Correct | Missing | False |
| -------- | ---- | --------- | ------- | ------- | ----- |
| SoW      | 15   | 5         | 3       | 12      | 2     |

---

# Metrics

Precision
3 / 5 = **0.60**

Recall
3 / 15 = **0.20**

F1
≈ **0.30**

---

# Important observation for your dissertation

This result demonstrates a **key baseline weakness**:

* The model retrieved **risks from other artefacts** (e.g., change readiness).
* It **missed most implicit contractual risks**.

This supports your argument that **baseline RAG struggles with complex contractual documents**.

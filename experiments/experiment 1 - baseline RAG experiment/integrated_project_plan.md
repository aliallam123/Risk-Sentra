Ground truth for **Integrated Project Plan** contains **8 risks**:

1. Finance DD delay compressing Build/SIT phases
2. Integration scope growth affecting timeline
3. Optimistic overall RAG vs underlying delays
4. Management reserve depletion before Wave 2
5. FTE shortfall affecting milestone recovery
6. Testing phase compression risk
7. Regulatory dependency (German e-invoicing)
8. Change readiness below threshold in Wave 1 regions

(from the answer key file) 

---

# Model output

**Extracted = 12**

Key matches:

| Model Risk                             | Ground Truth Match |
| -------------------------------------- | ------------------ |
| Finance DD delay compress Build/SIT    | ✔ IPP-01           |
| Integration scope creep                | ✔ IPP-02           |
| Change readiness below threshold       | ✔ IPP-08           |
| Cleansing backlog growing; 1 FTE short | ✔ IPP-05           |

**Correct = 4**

---

# False positives

These do **not exist in the ground truth**:

* Data migration complexity
* SI resource retention
* Finance BPO availability
* Extract reconciliation failures
* Programme Quality Plan overdue
* Workday dependency
* No local change managers
* Finance workstream lead availability

**False = 8**

Most came from **other artefacts in the KB**.

---

# Missing risks

Ground truth risks not detected:

* Optimistic RAG vs delays
* Management reserve depletion
* Testing phase compression
* Regulatory dependency (German e-invoicing)

**Missing = 4**

---

# Evaluation row

| Document                | True | Extracted | Correct | Missing | False |
| ----------------------- | ---- | --------- | ------- | ------- | ----- |
| Integrated Project Plan | 8    | 12        | 4       | 4       | 8     |

---

# Metrics

Precision
4 / 12 = **0.33**

Recall
4 / 8 = **0.50**

F1
≈ **0.40**

---

# Next prompt (PID document)

Run this next:

```
Analyse the PID document only.

Identify all delivery or governance risks present in the PID artefact.

Ignore risks from other artefacts such as the Business Case, Integrated Project Plan, Programme Charter, Scope and Deliverables, or Statement of Work.

For each risk return:

Risk: <short description>
Risk Type: <Explicit or Implicit>
Evidence: "<exact text from the document>"
```

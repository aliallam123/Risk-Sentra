I checked your output against the ground truth.

Ground truth risks in **Business Case** = **8**. 

### Ground truth list

1. Management reserve depletion before Month 24
2. SI forecast exceeds baseline by £800k
3. Integration scope creep increases cost base
4. Data migration complexity threatens benefits realisation
5. Finance DD delay compresses schedule
6. Benefits realisation plan not formally baselined
7. Assumption of no further scope growth may prove invalid
8. Over-optimistic payback period dependent on full benefit realisation

---

# Model output (5)

1. Data migration complexity
2. Finance DD delay compresses schedule
3. Integration scope creep
4. Regional change readiness
5. SI resource quality and retention

---

# Correct matches

These **match the ground truth**:

* Data migration complexity
* Finance DD delay compresses schedule
* Integration scope creep

**Correct = 3**

---

# False positives

These **do not exist in the Business Case ground truth**:

* Regional change readiness
* SI resource retention

**False = 2**

These came from **another artefact in the KB**.

---

# Missing risks

Ground truth risks the model **missed**:

1. Management reserve depletion
2. SI forecast exceeds baseline by £800k
3. Benefits realisation plan not baselined
4. Scope growth assumption invalid
5. Over-optimistic payback period

**Missing = 5**

---

# Your evaluation row

| Document      | True | Extracted | Correct | Missing | False |
| ------------- | ---- | --------- | ------- | ------- | ----- |
| Business Case | 8    | 5         | 3       | 5       | 2     |

---

# Metrics

Precision
3 / 5 = **0.60**

Recall
3 / 8 = **0.375**

F1
≈ **0.46**

---

# Important insight for your dissertation

This result shows two things:

1. **RAG retrieval noise** (risks from other artefacts)
2. **Implicit risk detection weakness**

This directly supports the evaluation design in your methodology where extraction precision and recall are measured against the benchmark corpus. 

---

Next step:
Run the **same process for the next document (Integrated Project Plan)**.

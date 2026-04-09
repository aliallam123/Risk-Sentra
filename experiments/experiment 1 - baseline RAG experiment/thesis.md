
---

# Experiment 1: Baseline Retrieval-Augmented Risk Extraction

## Objective

The objective of Experiment 1 was to establish a **baseline performance benchmark** for automated delivery risk extraction using a **Retrieval-Augmented Generation (RAG) pipeline**.

The experiment evaluates whether a lightweight large language model can identify delivery and governance risks embedded within consulting project artefacts without specialised tuning or optimisation.

This baseline serves two purposes:

1. To measure the **initial effectiveness of the system architecture**.
2. To provide a **reference point against which later system improvements can be compared**.

The experiment therefore represents the **default behaviour of the system before any optimisation techniques are introduced**.

---

# System Configuration

The baseline experiment was implemented using **Amazon Bedrock**.

The system architecture consisted of the following components:

### Knowledge Base

A **Bedrock Knowledge Base** was created containing the project artefacts used for risk extraction.

Documents were stored in **Amazon S3** and automatically indexed into a **vector embedding store** through the Bedrock Knowledge Base ingestion pipeline.

Each artefact was chunked and embedded to enable semantic retrieval during query execution.

Only **unlabelled artefacts (Output A files)** were ingested into the Knowledge Base.

The corresponding **ground truth risk labels (Output B files)** were intentionally excluded to prevent evaluation leakage.

---

### Language Model

The generation model used in the baseline experiment was:

**Claude 3 Haiku**

The model was selected due to:

* low token cost
* fast response latency
* compatibility with Bedrock Knowledge Bases

Although more capable models exist, Haiku was chosen to maintain a **low-cost and lightweight implementation**, consistent with the project constraints.

---

### Retrieval Pipeline

The system followed a standard **RAG pipeline** consisting of:

1. User query submitted to the system
2. Semantic search performed across the vector store
3. Top-k document chunks retrieved
4. Retrieved content passed to the LLM
5. LLM generates a response based on the retrieved context

The model was instructed to **extract risks only from the retrieved search results**.

---

# Dataset Used

The experiment was conducted on artefacts from **Category 1: Governance and Initiation**.

These artefacts represent early-stage programme documentation where delivery risks often appear implicitly.

The documents analysed included:

* Business Case
* Integrated Project Plan
* Project Initiation Document (PID)
* Programme Charter
* Scope and Deliverables

In addition, a **Statement of Work artefact** was used to observe system behaviour on a longer contractual document.

Each artefact had a corresponding **ground truth risk register** produced during dataset preparation.

These registers defined the **expected risks that the model should identify**.

---

# Experimental Procedure

For each artefact the following process was executed:

1. The artefact was ingested into the Bedrock Knowledge Base.
2. A risk extraction prompt was issued to the RAG system.
3. The model retrieved relevant document chunks through vector search.
4. Claude 3 Haiku generated a list of detected risks.
5. The generated risks were manually compared with the ground truth risk register.

The model was required to output:

* a short risk description
* whether the risk was explicit or implicit
* supporting textual evidence from the document

---

# Evaluation Method

Performance was evaluated by comparing model outputs with the **ground truth risk labels**.

Three outcome categories were recorded:

### Correct Risk

A risk correctly identified by the model that matches a ground truth entry.

### Missing Risk

A risk present in the ground truth but not identified by the model.

### False Positive

A risk produced by the model that does not appear in the ground truth dataset.

---

# Metrics

From these counts three performance metrics were calculated.

### Precision

Precision measures how many extracted risks were actually correct.

Precision = Correct Risks / Extracted Risks

---

### Recall

Recall measures how many of the true risks the system successfully detected.

Recall = Correct Risks / Ground Truth Risks

---

### F1 Score

The F1 score provides a balanced measure of precision and recall.

F1 = 2 × (Precision × Recall) / (Precision + Recall)

---

# Results Summary

Across the evaluated artefacts, the baseline system demonstrated **moderate precision but relatively low recall**.

Typical observations included:

* The model correctly identified several **explicit risks** present in the text.
* However, it frequently **failed to detect implicit risks** requiring contextual reasoning.
* Some outputs included **false positives retrieved from other artefacts in the knowledge base**.
* Performance degraded on **long contractual documents**, where risk signals were embedded across multiple sections.

The experiment therefore demonstrates that while baseline RAG can detect obvious risks, it struggles with **complex, implicit, or cross-referenced risk conditions**.

---

# Key Observations

Several important behavioural patterns were identified during the experiment.

### Cross-Document Retrieval Noise

Because the Knowledge Base contained multiple artefacts, the retrieval stage sometimes returned chunks from **unrelated documents**.

This occasionally caused the model to generate risks that belonged to a different artefact.

---

### Difficulty Detecting Implicit Risks

Many project risks are not explicitly labelled as risks in documents.

Instead, they emerge from **inferred conditions**, such as:

* schedule compression
* governance gaps
* contractual inconsistencies
* dependency failures

The baseline model struggled to infer these risks without stronger prompting.

---

### Long Document Complexity

Contractual artefacts such as Statements of Work contain risk signals distributed across:

* assumptions
* observations
* commercial terms
* governance structures

The model often retrieved only small fragments of these sections, preventing it from identifying the full risk context.

---

# Baseline Experiment Conclusion

Experiment 1 establishes the **baseline capability of the Risk Sentra system**.

The results indicate that a simple RAG architecture using a lightweight model can identify some delivery risks, but the approach has significant limitations:

* limited ability to infer implicit risks
* retrieval contamination across documents
* difficulty analysing long artefacts
* reduced recall performance

These findings justify the need for **further experimentation and system improvements**, which are explored in the subsequent experiments.

Future experiments investigate whether modifications such as **prompt engineering, retrieval constraints, or improved document targeting** can improve extraction accuracy relative to this baseline.

---

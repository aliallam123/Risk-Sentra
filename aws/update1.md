# Risk Sentra Prototype Progress Log

## Project Goal

The goal of the Risk Sentra prototype is to build an AI-assisted system capable of analysing unstructured programme documentation and extracting candidate risks with supporting evidence. The system is designed to convert narrative artefacts into structured risk insights while preserving provenance and enabling human review. This aligns directly with the dissertation aim of creating a governance-aware AI assistant that operates upstream of formal risk registers.

The prototype implementation uses AWS services including Amazon S3, Amazon Bedrock Knowledge Bases, vector embeddings, and a foundation model to simulate the analytical pipeline described in the methodology.

---

# Phase 1 — Cloud Environment Setup

The project environment was set up within AWS using the **Europe (London) region (eu-west-2)** to ensure compatibility with available Bedrock models and to minimise latency.

The following cloud infrastructure components were configured:

### S3 Storage Bucket

A dedicated S3 bucket was created to store the synthetic benchmark dataset used for testing the system.

Bucket name:

risk-sentra-prototype-ali

The bucket was configured with:

* Block public access enabled
* Bucket owner enforced object ownership
* Default server-side encryption (SSE-S3)
* Versioning disabled for simplicity

This bucket acts as the **document repository for the Risk Sentra prototype**.

---

# Phase 2 — Data Organisation

The synthetic dataset generated earlier in the project was uploaded to S3.

The data was organised according to the artefact taxonomy defined in the dissertation.

Current structure:

```
risk-sentra
   ├── Category 1 - Governance & Initiation
   │      ├── category1-data
   │      └── category1-labels
   │
   ├── Category 2 - Status & Reporting
   │      ├── category2-data
   │      └── category2-labels
```

Only the **data folders** are used by the AI system.

The **label folders contain the ground-truth answer keys** used later for evaluation and benchmarking.

Examples of uploaded documents include:

* Statement of Work
* Scope and Deliverables
* Programme Charter
* Integrated Project Plan
* Programme Dashboard
* Business Case
* Project Initiation Document (PID)

These documents simulate the type of unstructured artefacts typically encountered in programme governance environments.

---

# Phase 3 — Knowledge Base Creation (Bedrock)

To enable retrieval-based document analysis, an **Amazon Bedrock Knowledge Base** was created.

Knowledge base name:

risk-sentra-kb

The knowledge base connects directly to the S3 document repository.

Configuration details:

Data source type
Amazon S3

S3 URI
s3://risk-sentra-prototype-ali/risk-sentra/

Parsing strategy
Amazon Bedrock default parser

Chunking strategy
Default chunking (~300 tokens)

Embeddings model
Titan Text Embeddings v2

Vector store
Amazon OpenSearch Serverless

The embeddings model converts document text into vector representations, which are stored inside the OpenSearch vector database. This enables semantic search across the document corpus.

---

# Phase 4 — Data Ingestion

The knowledge base was synchronised with the S3 bucket.

During ingestion the system:

1. Parsed the documents
2. Extracted text content
3. Split documents into chunks
4. Generated vector embeddings
5. Stored vectors in OpenSearch

Some files were ignored during ingestion because they were unsupported formats (for example certain .docx and .xlsx files). This did not prevent the system from functioning, as the primary text-based documents were successfully indexed.

The ingestion process effectively created a **semantic index of the document corpus**.

---

# Phase 5 — Retrieval Testing

The knowledge base was tested using the Bedrock interface with the following configuration:

Retrieval mode
Retrieval and Response Generation

Foundation model
Claude 3 Haiku

This configuration allows the system to perform the following pipeline:

Query → Retrieve relevant document chunks → Send retrieved context to the model → Generate an answer.

Initial test prompts confirmed that the system was successfully retrieving document segments from the knowledge base.

---

# Phase 6 — Risk Extraction Prompt Engineering

Custom prompts were designed to simulate the analytical behaviour of the Risk Sentra system.

The model was instructed to:

* analyse retrieved programme documentation
* identify both explicit and implicit risks
* extract evidence sentences
* return the source document

Example prompt used:

"You are a programme risk analysis assistant. Analyse the retrieved project governance and initiation documents. Identify potential project risks mentioned or implied in the documentation. For each risk provide risk description, whether the risk is explicit or implicit, evidence from the document, and source document name."

This prompt operationalises the **risk identification stage described in the dissertation methodology**.

---

# Phase 7 — First Successful Risk Extraction

The system successfully extracted multiple candidate risks from the dataset.

Examples returned by the system include:

Explicit risks:

* Data migration complexity caused by poor legacy data quality
* Finance detailed design delays impacting the programme timeline
* Integration scope creep due to additional interfaces
* Regional change readiness below threshold
* SI resource departures and replacement delays

Implicit risks:

* Business process owner availability constraints
* Data reconciliation failures during extraction
* Data cleansing backlog due to insufficient staffing

Each risk was accompanied by supporting evidence from the source document, demonstrating traceability between the output and the underlying text.

---

# Phase 8 — Prototype Behaviour Achieved

At this stage the system is successfully performing the core functionality envisioned in the dissertation:

Document ingestion
→ semantic retrieval
→ model reasoning
→ candidate risk extraction.

This replicates the conceptual architecture described earlier in the methodology section.

The working pipeline can be summarised as:

S3 document storage
→ Bedrock Knowledge Base
→ Vector embeddings (Titan v2)
→ OpenSearch semantic retrieval
→ Claude model reasoning
→ Risk extraction output.

---

# Current Status

The prototype can now:

* ingest programme documentation
* retrieve relevant document segments
* identify explicit and implicit risks
* provide evidence supporting each risk

This represents a functioning **AI-assisted risk identification system** consistent with the Risk Sentra concept.

---

# Next Planned Steps

The remaining development tasks include:

Implementing structured risk register outputs

Adding taxonomy classification (T1–T10 categories)

Running controlled benchmark tests against the answer keys

Calculating evaluation metrics including precision, recall, and F1 score

Generating screenshots and demonstrations for the dissertation and final presentation.

---

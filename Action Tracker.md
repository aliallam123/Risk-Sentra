# Risk Sentra Build Tracker

## Phase 1 - S3 upload and document organisation
- [ ] Create an AWS S3 bucket for the project
- [ ] Create a clean folder structure inside the bucket
- [ ] Decide final naming convention for all synthetic artefacts
- [ ] Rename files so every document has a unique document ID
- [ ] Upload all synthetic artefacts to S3
- [ ] Create a master index file for all uploaded documents
- [ ] Add metadata fields we want to track for each document
- [ ] Verify all files are visible in S3 and correctly grouped
- [ ] Take screenshots of the bucket, folders, and uploaded files for the dissertation

## Phase 2 - Ground truth and benchmark prep
- [ ] Finalise the answer key / ground truth for each document
- [ ] Make sure each answer key includes expected risks
- [ ] Label each risk as explicit or implicit
- [ ] Map each risk to the T1 to T10 taxonomy
- [ ] Record source location for each embedded risk
- [ ] Store answer keys in a separate clean folder
- [ ] Create a benchmark version number for the corpus
- [ ] Take screenshots of sample synthetic documents and answer keys

## Phase 3 - Bedrock setup
- [ ] Confirm Bedrock model access is enabled in the AWS account
- [ ] Check which Bedrock models are available in the region
- [ ] Pick the first model to test for extraction
- [ ] Pick the embedding model for the knowledge base
- [ ] Take screenshots of Bedrock model access and enabled models

## Phase 4 - Knowledge Base creation
- [ ] Create a Bedrock Knowledge Base
- [ ] Connect the Knowledge Base to the S3 bucket as the data source
- [ ] Configure chunking settings
- [ ] Decide whether to use default Bedrock-managed retrieval first
- [ ] Start initial ingestion / sync job
- [ ] Confirm documents are indexed successfully
- [ ] Test a few simple retrieval queries in the console
- [ ] Check whether retrieved chunks look sensible
- [ ] Take screenshots of Knowledge Base config, sync status, and retrieval tests

## Phase 5 - Extraction design
- [ ] Define the output schema for a candidate risk
- [ ] Decide the exact output fields for each extracted risk
- [ ] Finalise the T1 to T10 taxonomy list and definitions
- [ ] Write the first extraction prompt
- [ ] Add rules to stop unsupported / hallucinated risks
- [ ] Add rules for explicit vs implicit classification
- [ ] Add rules for source evidence and provenance fields
- [ ] Add rules for taxonomy-constrained output only

## Phase 6 - Structured output pipeline
- [ ] Set up a Python script or notebook to call Bedrock
- [ ] Retrieve relevant chunks from the Knowledge Base
- [ ] Pass retrieved evidence into the model
- [ ] Enforce structured JSON output
- [ ] Validate returned JSON
- [ ] Save raw model outputs for logging
- [ ] Convert valid outputs into a clean risk register table
- [ ] Take screenshots of code, JSON outputs, and early extracted risks

## Phase 7 - Risk register generation
- [ ] Create a consolidated risk register format
- [ ] Add columns for risk ID, title, statement, taxonomy, confidence, source document, source segment, explicit/implicit
- [ ] Deduplicate repeated risks across chunks
- [ ] Decide how to merge very similar risks
- [ ] Export final register to CSV or Excel
- [ ] Create a small sample register for screenshots

## Phase 8 - Executive summary generation
- [ ] Write a second prompt that summarises the final risk register
- [ ] Generate an executive summary from the structured register, not raw documents
- [ ] Check clarity, traceability, and usefulness
- [ ] Save example summary outputs
- [ ] Take screenshots of register plus summary

## Phase 9 - Logging and reproducibility
- [ ] Log model name and version
- [ ] Log prompt version
- [ ] Log chunk size
- [ ] Log retrieval settings
- [ ] Log taxonomy version
- [ ] Log benchmark corpus version
- [ ] Log date/time of each run
- [ ] Save all logs in a simple CSV or JSON file
- [ ] Take screenshots of logs for the dissertation

## Phase 10 - Evaluation
- [ ] Compare extracted risks against the answer key
- [ ] Calculate precision
- [ ] Calculate recall
- [ ] Calculate F1
- [ ] Calculate taxonomy alignment accuracy
- [ ] Check provenance completeness
- [ ] Check provenance sufficiency
- [ ] Split results by explicit vs implicit risks
- [ ] Save results in tables and charts
- [ ] Take screenshots of evaluation outputs

## Phase 11 - Ablation / comparison tests
- [ ] Run test with chunk size option 1
- [ ] Run test with chunk size option 2
- [ ] Compare results
- [ ] Run test with stricter taxonomy control vs looser prompt
- [ ] Compare results
- [ ] Keep only the comparisons we can explain clearly in the dissertation

## Phase 12 - Guardrails and governance
- [ ] Decide whether to add Bedrock Guardrails for the prototype
- [ ] If yes, test contextual grounding checks
- [ ] Document how hallucination risk is reduced
- [ ] Document limits of the prototype
- [ ] Take screenshots if Guardrails are used

## Phase 13 - Demo readiness
- [ ] Prepare one clean end-to-end demo dataset
- [ ] Run the full pipeline from retrieval to register
- [ ] Save the best working example
- [ ] Record exact demo steps so they can be repeated live
- [ ] Prepare screenshots in the order they appear in the dissertation
- [ ] Prepare for a later video demo

## Phase 14 - Dissertation evidence pack
- [ ] Architecture diagram
- [ ] S3 screenshots
- [ ] Bedrock Knowledge Base screenshots
- [ ] Retrieval screenshots
- [ ] Example prompt and schema screenshots
- [ ] Example candidate risk outputs
- [ ] Example risk register
- [ ] Example executive summary
- [ ] Benchmark results tables
- [ ] Error analysis examples
- [ ] Final appendix evidence list

# Risk Sentra – Knowledge Base Initial Retrieval Test

## Objective

Validate that the Amazon Bedrock Knowledge Base can retrieve programme artefacts and that the model can detect delivery risks from the retrieved content.

This experiment tests the first working version of the Risk Sentra pipeline:

S3 → Bedrock Knowledge Base → Claude 3 Haiku → Risk Extraction

---

## Test Document

Source artefact:

Programme Charter – Atlas ERP Transformation

Ground truth labels are provided in the **Output B – Ground Truth Risk Answer Key**.

Ground truth risk count:

15 embedded risks

---

## Query Used

Extract delivery risks from the document.
List each risk on a separate line.
Do not explain anything.


---

## Model Output

Detected risks:

1. Data migration complexity – legacy data quality significantly below expectations.
2. Finance Detailed Design delay may compress Build and SIT phases.
3. Integration scope creep due to new interfaces added post-HLD.
4. Regional change readiness below target threshold.
5. SI resource quality and retention concerns due to consultant departures.

---

## Evaluation

Ground truth risks: **15**

Model detected risks: **5**

Recall calculation:

Recall = extracted / ground truth
Recall = 5 / 15
Recall = 0.33


Recall result:

**33%**

---

## Observations

- The Knowledge Base retrieval is functioning correctly.
- Claude 3 Haiku successfully identifies several explicit risks.
- Many implicit contractual and governance risks were not detected.
- The model appears stronger at detecting operational delivery risks than governance or contractual risks.

---

## Next Steps

- Improve extraction prompt design.
- Test retrieval with different chunk sizes.
- Introduce structured JSON extraction.
- Evaluate implicit risk detection separately.

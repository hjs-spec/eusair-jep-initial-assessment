# Case 2: Cross-Border Medical Diagnosis (High-Risk AI)

## Scenario Overview

This case demonstrates a cross-border medical diagnosis service involving multiple AI agents across the EU, with implications for patient safety, data governance, and clinical accountability.

**Participants**:
- **France**: AP-HP Hospital preliminary diagnosis AI (high-risk AI under Annex III)
- **Germany**: Charité Research Institute rare disease analysis AI (specialized medical AI)
- **Italy**: Biobank genetic data service (GDPR-sensitive data source)
- **France**: Specialist physician (human oversight, final diagnosis)

**Flow**:
```
Patient presents with symptoms
    ↓
French Hospital AI (Agent A) performs preliminary analysis
    ↓
Agent A delegates rare disease analysis to German Charité AI (Agent B)
    ↓
Agent B delegates genetic data retrieval to Italian Biobank (External)
    ↓
Agent A synthesizes results and recommends referral
    ↓
French specialist physician (Human) reviews and finalizes diagnosis
```

## Regulatory Context (EU AI Act)

| Article | Requirement | Relevance to This Case |
|---------|-------------|------------------------|
| **Annex III, Art. 5** | Medical AI is high-risk | Diagnosis AI falls under Annex III (medical devices) |
| **Art. 10** | Data governance | Genetic data from Italy must comply with GDPR + AI Act |
| **Art. 11** | Technical documentation | All AI models must maintain versioned documentation |
| **Art. 14** | Human oversight | Physician must have meaningful oversight of AI recommendations |
| **Art. 52** | Transparency | Patient has right to know how diagnosis was reached |

## Accountability Challenge

If a rare disease is misdiagnosed and the patient suffers harm:

- Was the French hospital AI's initial assessment wrong?
- Did the German Charité AI's rare disease model have a bias?
- Was the Italian biobank's genetic data inaccurate or outdated?
- Did the French physician fail to properly review the AI's recommendation?

Without cross-system accountability, the hospital, research institute, biobank, and physician can all deflect responsibility. With JEP, the complete diagnostic chain is recorded and verifiable.

## JEP Implementation

```
judge(APHP_AI, {version: "3.2", authority: "preliminary-diagnosis", clinical_context: "neurology"})
    → delegate(Charite_AI, {purpose: "rare-disease-analysis", confidence_threshold: 0.85})
    → delegate(Biobank, {purpose: "genetic-data-retrieval", consent_id: "GDPR-2026-0042", data_types: ["rare-genetic-markers"]})
    → terminate(Physician, {diagnosis: "multiple-sclerosis", confidence: 0.92, notes: "Confirmed MRI findings"})
```

## Evidence Location

- Input scenario: `scenario.json`
- Expected JEP receipt: `expected-receipt.json`
- Mapping to EU AI Act: `mapping.md`
- Run script: `run.py`
- Verification: `verify.sh`
```

---

# 📁 eusair-demo/case2-healthcare/scenario.json

```json
{
  "case_id": "eusair-case2-healthcare-001",
  "title": "Cross-Border Rare Disease Diagnosis",
  "description": "A patient with complex neurological symptoms is diagnosed through collaboration between French, German, and Italian medical AI systems.",
  
  "actors": [
    {
      "id": "aphp-diagnosis-ai",
      "type": "high-risk-ai",
      "jurisdiction": "France",
      "organization": "AP-HP Hôpitaux de Paris",
      "version": "3.2",
      "model_hash": "0x7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e",
      "clinical_domain": "general_neurology",
      "certification": "CE-MDR-Class-IIb"
    },
    {
      "id": "charite-rare-disease-ai",
      "type": "specialized-medical-ai",
      "jurisdiction": "Germany",
      "organization": "Charité - Universitätsmedizin Berlin",
      "version": "2.4",
      "model_hash": "0x4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f",
      "clinical_domain": "rare_neurological_disorders",
      "training_data_hash": "0x9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d"
    },
    {
      "id": "italian-biobank",
      "type": "genetic-data-service",
      "jurisdiction": "Italy",
      "organization": "Telethon Network of Genetic Biobanks",
      "version": "api-v2",
      "endpoint": "genetic-markers/retrieve",
      "iso_certification": "ISO 20387:2023"
    },
    {
      "id": "specialist-physician",
      "type": "human",
      "jurisdiction": "France",
      "name": "Dr. Sophie Martin",
      "role": "Neurology Specialist",
      "license": "FR-MED-87654",
      "hospital": "AP-HP Pitié-Salpêtrière"
    }
  ],
  
  "patient_data": {
    "patient_id": "EU-PAT-2026-0184",
    "age": 34,
    "gender": "female",
    "symptoms": [
      "progressive_muscle_weakness",
      "visual_disturbances",
      "fatigue"
    ],
    "symptom_onset": "2026-01-15",
    "previous_conditions": "none_significant",
    "country_of_treatment": "France",
    "consent_id": "GDPR-2026-0042",
    "consent_date": "2026-02-01"
  },
  
  "execution_flow": [
    {
      "step": 1,
      "actor": "specialist-physician",
      "action": "initial_consultation",
      "timestamp": "2026-03-05T14:00:00Z",
      "notes": "Patient presents with neurological symptoms. Ordering AI-assisted analysis."
    },
    {
      "step": 2,
      "actor": "aphp-diagnosis-ai",
      "action": "receive_patient_data",
      "timestamp": "2026-03-05T14:05:00Z",
      "input": "patient_data",
      "preliminary_findings": "Possible demyelinating condition, requires rare disease rule-out"
    },
    {
      "step": 3,
      "actor": "aphp-diagnosis-ai",
      "action": "delegate",
      "to": "charite-rare-disease-ai",
      "purpose": "rare_disease_analysis",
      "confidence_threshold": 0.85,
      "timestamp": "2026-03-05T14:05:30Z",
      "clinical_context": "suspected multiple sclerosis vs. rare genetic disorders"
    },
    {
      "step": 4,
      "actor": "charite-rare-disease-ai",
      "action": "delegate",
      "to": "italian-biobank",
      "purpose": "genetic_marker_retrieval",
      "genetic_markers_requested": ["HLA-DRB1", "MOG", "AQP4"],
      "consent_id": "GDPR-2026-0042",
      "timestamp": "2026-03-05T14:05:45Z"
    },
    {
      "step": 5,
      "actor": "italian-biobank",
      "action": "verify_consent",
      "consent_valid": true,
      "timestamp": "2026-03-05T14:05:50Z"
    },
    {
      "step": 6,
      "actor": "italian-biobank",
      "action": "return_genetic_data",
      "data": {
        "HLA-DRB1": "positive for MS-associated alleles",
        "MOG": "negative",
        "AQP4": "negative",
        "additional_findings": "No rare genetic variants detected"
      },
      "data_hash": "0x2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a",
      "timestamp": "2026-03-05T14:06:15Z"
    },
    {
      "step": 7,
      "actor": "charite-rare-disease-ai",
      "action": "analyze_with_genetic_data",
      "timestamp": "2026-03-05T14:06:30Z",
      "analysis_duration_ms": 850,
      "findings": {
        "rare_diseases_ruled_out": ["leukodystrophy", "mitochondrial_disorder"],
        "likely_condition": "multiple_sclerosis",
        "confidence": 0.89
      }
    },
    {
      "step": 8,
      "actor": "charite-rare-disease-ai",
      "action": "return_analysis",
      "to": "aphp-diagnosis-ai",
      "results": {
        "primary_diagnosis": "multiple_sclerosis",
        "confidence": 0.89,
        "supporting_evidence": ["HLA-DRB1 positive", "clinical presentation consistent"],
        "differential_diagnoses": [
          {"condition": "neuromyelitis_optica", "confidence": 0.12},
          {"condition": "acute_disseminated_encephalomyelitis", "confidence": 0.08}
        ]
      },
      "timestamp": "2026-03-05T14:06:35Z"
    },
    {
      "step": 9,
      "actor": "aphp-diagnosis-ai",
      "action": "synthesize_findings",
      "timestamp": "2026-03-05T14:06:45Z",
      "synthesized_recommendation": {
        "primary_diagnosis": "multiple_sclerosis",
        "confidence": 0.87,
        "recommended_action": "refer_to_specialist_for_confirmation",
        "suggested_tests": ["MRI brain and spine", "lumbar puncture"]
      }
    },
    {
      "step": 10,
      "actor": "specialist-physician",
      "action": "review_findings",
      "timestamp": "2026-03-06T09:30:00Z",
      "review_notes": "Reviewed AI analysis and genetic data. Consistent with MS presentation."
    },
    {
      "step": 11,
      "actor": "specialist-physician",
      "action": "order_additional_tests",
      "tests_ordered": ["MRI brain with contrast", "evoked potentials"],
      "timestamp": "2026-03-06T09:35:00Z"
    },
    {
      "step": 12,
      "actor": "specialist-physician",
      "action": "finalize_diagnosis",
      "timestamp": "2026-03-08T11:00:00Z",
      "diagnosis": "multiple_sclerosis",
      "diagnosis_code": "ICD-10 G35",
      "confidence": 0.95,
      "notes": "MRI confirmed demyelinating lesions. Started on disease-modifying therapy.",
      "informed_patient": true
    }
  ],
  
  "final_outcome": {
    "diagnosis": "multiple_sclerosis",
    "diagnosis_date": "2026-03-08",
    "responsible_actor": "specialist-physician",
    "contributing_ais": ["aphp-diagnosis-ai", "charite-rare-disease-ai", "italian-biobank"],
    "patient_notified": true,
    "jep_receipt": "expected-receipt.json"
  }
}
```

---

# 📁 eusair-demo/case2-healthcare/mapping.md

```markdown
# EU AI Act Mapping: Case 2 - Cross-Border Medical Diagnosis

| Article | Requirement | How JEP Addresses It | Evidence |
|---------|-------------|----------------------|----------|
| **Annex III, Art. 5** | Medical AI is high-risk | Both AP-HP and Charité AIs identified as high-risk in `judge` primitives | `scenario.json` - actors[0].type, actors[1].type |
| **Art. 10** | Data governance | Genetic data retrieval includes consent verification and data hashing | `scenario.json` - step 4 (consent_id), step 6 (data_hash) |
| **Art. 11** | Technical documentation | All AI versions and model hashes recorded | `scenario.json` - actors[0].version, actors[0].model_hash |
| **Art. 14** | Human oversight | Physician makes final diagnosis after reviewing AI recommendations | `scenario.json` - step 12, physician finalizes |
| **Art. 52** | Transparency | Complete diagnostic trail available in JEP receipt | `expected-receipt.json` - full event chain |

## Detailed Mapping

### Annex III, Article 5: Medical Devices
Both the French hospital AI and German research AI fall under the scope of medical device regulations. JEP records their certification status (`CE-MDR-Class-IIb`) and version history, providing auditable evidence of regulatory compliance.

### Article 10: Data Governance
The Italian Biobank's genetic data retrieval includes explicit consent verification (GDPR-2026-0042) and cryptographic hashing of the returned data. This ensures that:
- Data was used with proper consent
- Data integrity can be verified
- Any subsequent data breach can be traced

### Article 14: Human Oversight
The French specialist physician:
- Reviews all AI recommendations (step 10)
- Orders additional tests before finalizing (step 11)
- Makes the final diagnosis with their own clinical judgment (step 12)

The JEP receipt proves that human oversight was exercised meaningfully, not just as a rubber stamp.

### Article 52: Transparency
If the patient requests information about how their diagnosis was reached, the hospital can provide the JEP receipt showing:
- Which AI systems contributed to the analysis (France, Germany)
- What genetic data was used (Italy)
- What confidence levels each AI assigned
- Who made the final decision (Dr. Martin)
- When each step occurred

This satisfies both the AI Act's transparency requirements and GDPR's right to explanation.
```

---

# 📁 eusair-demo/case2-healthcare/run.py

```python
#!/usr/bin/env python3
"""
Run Case 2: Cross-Border Medical Diagnosis
"""

import json
import sys
from pathlib import Path

# Add JEP core to path
sys.path.append(str(Path(__file__).parent.parent.parent / "src"))

from aip_jep.compliance_demo import process_scenario
from aip_jep.crypto import sign_receipt

def main():
    # Load scenario
    with open("scenario.json", "r") as f:
        scenario = json.load(f)
    
    print(f"\n{'='*60}")
    print(f"Running Case 2: {scenario['title']}")
    print(f"{'='*60}\n")
    
    print(f"Description: {scenario['description']}")
    print(f"\nActors involved:")
    for actor in scenario['actors']:
        print(f"  - {actor['id']} ({actor['type']}, {actor['jurisdiction']})")
    
    print(f"\nPatient: Age {scenario['patient_data']['age']}, {scenario['patient_data']['gender']}")
    print(f"Symptoms: {', '.join(scenario['patient_data']['symptoms'])}")
    
    # Process the scenario using JEP
    print(f"\n{'→'*40}")
    print("Processing with JEP...")
    print(f"{'→'*40}")
    
    receipt = process_scenario(scenario)
    
    # Add cryptographic signature
    signed_receipt = sign_receipt(receipt)
    
    # Save expected receipt
    with open("expected-receipt.json", "w") as f:
        json.dump(signed_receipt, f, indent=2)
    
    print(f"\n✓ JEP Receipt generated and saved to expected-receipt.json")
    print(f"\nFinal diagnosis: {scenario['final_outcome']['diagnosis']}")
    print(f"Diagnosed by: {scenario['final_outcome']['responsible_actor']}")
    print(f"Contributing AI systems: {', '.join(scenario['final_outcome']['contributing_ais'])}")
    
    print(f"\n{'='*60}")
    print("Case 2 completed successfully")
    print(f"{'='*60}\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

---

# 📁 eusair-demo/case2-healthcare/verify.sh

```bash
#!/bin/bash
# Verification script for Case 2

echo "=========================================="
echo "Verifying Case 2: Cross-Border Medical Diagnosis"
echo "=========================================="

# Check if expected receipt exists
if [ ! -f "expected-receipt.json" ]; then
    echo "❌ expected-receipt.json not found. Run run.py first."
    exit 1
fi

# Run JEP verification
python3 ../../src/aip_jep/verify_sandbox.py --receipt expected-receipt.json

if [ $? -eq 0 ]; then
    echo "✅ Case 2 verification passed"
else
    echo "❌ Case 2 verification failed"
    exit 1
fi

# Additional healthcare-specific verification
echo ""
echo "Healthcare compliance checks:"
echo "------------------------------"

# Check if consent was verified
if grep -q "verify_consent" scenario.json; then
    echo "✅ GDPR consent verification found"
else
    echo "⚠️  GDPR consent verification not found"
fi

# Check if physician final diagnosis recorded
if grep -q "finalize_diagnosis" scenario.json; then
    echo "✅ Human oversight (physician) recorded"
else
    echo "⚠️  Human oversight not clearly recorded"
fi

echo ""
echo "=========================================="
```

---

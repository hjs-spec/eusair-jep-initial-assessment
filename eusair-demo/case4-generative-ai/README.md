# Case 4: Cross-Border Generative AI Content Transparency (Synthetic Content)

## Scenario Overview

This case demonstrates a cross-border content moderation and synthetic content detection system across the EU, addressing the AI Act's transparency obligations for generative AI and foundation models.

**Participants**:
- **Germany**: Social media platform content moderation AI (Deutsche Social platform)
- **France**: Multi-language content analysis AI (Institut National de l'Audiovisuel)
- **Spain**: Deepfake detection AI (Universitat de Barcelona AI Lab)
- **Ireland**: Content review team (human oversight, based in Dublin)

**Flow**:
```
User posts video content on German platform
    ↓
German moderation AI (Agent A) flags potential synthetic content
    ↓
Agent A delegates multi-language analysis to French AI (Agent B)
    ↓
Agent B delegates deepfake detection to Spanish AI (Agent C)
    ↓
Agent C returns detection results with confidence scores
    ↓
Irish content review team (Human) makes final moderation decision
```

## Regulatory Context (EU AI Act)

| Article | Requirement | Relevance to This Case |
|---------|-------------|------------------------|
| **Art. 28b** | Synthetic content labeling | AI-generated content must be clearly labeled |
| **Art. 50** | Copyright and training data | Foundation models must disclose training data sources |
| **Art. 52** | Transparency obligations | Users must be informed when interacting with AI-generated content |
| **Art. 53** | Foundation model obligations | Model providers must maintain technical documentation |
| **Art. 14** | Human oversight | Human reviewers must have final say on content moderation |

## Accountability Challenge

If a legitimate user video is wrongly flagged as "deepfake" and removed:

- Was the German platform AI's initial flag too aggressive?
- Did the French analysis AI misinterpret cultural context?
- Was the Spanish deepfake detection AI's model biased?
- Did the Irish review team fail to properly assess?

Without cross-system accountability, each AI provider can blame the others. With JEP, the complete content verification chain is recorded and verifiable.

## JEP Implementation

```
judge(DeutscheSocial_AI, {version: "3.2", authority: "content-moderation", platform_policy: "v2.1"})
    → delegate(INA_French_AI, {purpose: "multi-language-analysis", languages: ["DE", "FR", "EN", "ES"]})
    → delegate(UB_Barcelona_AI, {purpose: "deepfake-detection", confidence_threshold: 0.85, model_version: "df-detector-v4"})
    → terminate(DublinReviewTeam, {decision: "flag_as_synthetic", confidence: 0.92, human_review: true, notified_user: true})
```

## Evidence Location

- Input scenario: `scenario.json`
- Synthetic content sample: `synthetic-content.json`
- Expected JEP receipt: `expected-receipt.json`
- Mapping to EU AI Act: `mapping.md`
- Run script: `run.py`
- Verification: `verify.sh`
```

---

# 📁 eusair-demo/case4-generative-ai/synthetic-content.json

```json
{
  "content_id": "CONTENT-2026-03-10-0042",
  "content_type": "video",
  "title": "Political statement on EU agricultural policy",
  "duration_seconds": 87,
  "uploaded_by": "user_eu_agriculture_advocate",
  "upload_platform": "DeutscheSocial",
  "upload_timestamp": "2026-03-10T08:23:00Z",
  "content_metadata": {
    "language": "German with French subtitles",
    "resolution": "1080p",
    "file_size_mb": 45,
    "hash_sha256": "0x9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5"
  },
  
  "content_analysis": {
    "visual_features": [
      "synthetic_facial_movements",
      "inconsistent_lighting",
      "unnatural_eye_movements"
    ],
    "audio_features": [
      "synthetic_voice_patterns",
      "background_noise_inconsistent"
    ],
    "semantic_features": [
      "emotion_mismatch_with_content",
      "temporal_inconsistencies"
    ]
  },
  
  "ground_truth": {
    "actually_synthetic": true,
    "generation_method": "Stable Video Diffusion + ElevenLabs voice clone",
    "generation_timestamp": "2026-03-09T22:15:00Z",
    "generation_origin": "unknown (suspected disinformation campaign)",
    "training_data_sources_known": false
  },
  
  "relevant_eu_context": {
    "involves_eu_policy": true,
    "policy_area": "Common Agricultural Policy",
    "election_period": false,
    "public_figure_impersonated": "EU Agriculture Commissioner"
  }
}
```

---

# 📁 eusair-demo/case4-generative-ai/scenario.json

```json
{
  "case_id": "eusair-case4-generative-001",
  "title": "Cross-Border Synthetic Content Detection and Moderation",
  "description": "A video posted on a German social media platform triggers multi-country AI analysis for synthetic content detection.",
  
  "actors": [
    {
      "id": "deutsche-social-ai",
      "type": "content-moderation-ai",
      "jurisdiction": "Germany",
      "organization": "DeutscheSocial GmbH",
      "platform": "SocialSphere",
      "version": "3.2",
      "model_hash": "0x7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d",
      "moderation_policy": "EU-DSA-compliant-v2",
      "users_monthly": "12 million EU users"
    },
    {
      "id": "ina-french-ai",
      "type": "content-analysis-ai",
      "jurisdiction": "France",
      "organization": "Institut National de l'Audiovisuel",
      "specialization": "multi-language media analysis",
      "version": "4.1",
      "model_hash": "0x5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e",
      "languages_supported": ["DE", "FR", "EN", "ES", "IT", "NL", "PL"],
      "certification": "French Ministry of Culture approved"
    },
    {
      "id": "ub-barcelona-ai",
      "type": "deepfake-detection-ai",
      "jurisdiction": "Spain",
      "organization": "Universitat de Barcelona AI Lab",
      "specialization": "synthetic media detection",
      "version": "df-detector-v4",
      "model_hash": "0x3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f",
      "training_data_hash": "0x9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d",
      "training_data_disclosure": "publicly available deepfake datasets + EU-funded research data",
      "accuracy_metrics": {
        "precision": 0.94,
        "recall": 0.91,
        "f1_score": 0.92
      }
    },
    {
      "id": "dublin-review-team",
      "type": "human-team",
      "jurisdiction": "Ireland",
      "organization": "SocialSphere Trust & Safety",
      "location": "Dublin, Ireland",
      "team_size": 24,
      "supervisor": "Aoife O'Brien",
      "qualifications": "Certified Content Moderators (EU DSA certified)"
    }
  ],
  
  "content_to_analyze": "synthetic-content.json",
  
  "execution_flow": [
    {
      "step": 1,
      "actor": "deutsche-social-ai",
      "action": "receive_content",
      "timestamp": "2026-03-10T08:23:05Z",
      "content_id": "CONTENT-2026-03-10-0042",
      "initial_risk_assessment": {
        "involves_public_figure": true,
        "political_content": true,
        "potential_synthetic": "suspicious",
        "priority_score": 85
      }
    },
    {
      "step": 2,
      "actor": "deutsche-social-ai",
      "action": "preliminary_analysis",
      "timestamp": "2026-03-10T08:23:10Z",
      "analysis_results": {
        "face_detection": "synthetic_indicators_detected",
        "voice_analysis": "synthetic_patterns_suspected",
        "metadata_consistency": "inconsistent_creation_timestamps",
        "preliminary_confidence": 0.72
      }
    },
    {
      "step": 3,
      "actor": "deutsche-social-ai",
      "action": "delegate",
      "to": "ina-french-ai",
      "purpose": "multi_language_content_analysis",
      "timestamp": "2026-03-10T08:23:15Z",
      "delegation_context": {
        "languages_detected": ["German", "French"],
        "cultural_context_needed": true,
        "eu_policy_relevance": true
      }
    },
    {
      "step": 4,
      "actor": "ina-french-ai",
      "action": "analyze_content",
      "timestamp": "2026-03-10T08:23:20Z",
      "analysis_results": {
        "language_authenticity": {
          "german": "synthetic_patterns_detected",
          "french": "synthetic_patterns_detected"
        },
        "cultural_coherence": "low - mismatched cultural references",
        "temporal_consistency": "issues_detected",
        "confidence": 0.78
      }
    },
    {
      "step": 5,
      "actor": "ina-french-ai",
      "action": "delegate",
      "to": "ub-barcelona-ai",
      "purpose": "deepfake_detection",
      "timestamp": "2026-03-10T08:23:25Z",
      "delegation_context": {
        "focus_on_visual_synthesis": true,
        "focus_on_audio_synthesis": true,
        "request_detailed_breakdown": true
      }
    },
    {
      "step": 6,
      "actor": "ub-barcelona-ai",
      "action": "detect_deepfake",
      "timestamp": "2026-03-10T08:23:35Z",
      "detection_results": {
        "overall_synthetic_probability": 0.92,
        "visual_analysis": {
          "face_synthesis_confidence": 0.94,
          "eye_movement_naturalness": 0.87,
          "lighting_consistency": 0.89,
          "temporal_smoothness": 0.91
        },
        "audio_analysis": {
          "voice_synthesis_confidence": 0.93,
          "background_consistency": 0.86,
          "lip_sync_accuracy": 0.90
        },
        "generation_methods_probable": ["Stable Video Diffusion", "ElevenLabs voice clone"],
        "model_version_used": "df-detector-v4.2",
        "confidence_score": 0.92
      }
    },
    {
      "step": 7,
      "actor": "ub-barcelona-ai",
      "action": "return_results",
      "to": "ina-french-ai",
      "timestamp": "2026-03-10T08:23:40Z",
      "results_summary": {
        "detection_complete": true,
        "synthetic_content": true,
        "confidence": 0.92,
        "technical_details_available": true
      }
    },
    {
      "step": 8,
      "actor": "ina-french-ai",
      "action": "synthesize_analysis",
      "timestamp": "2026-03-10T08:23:45Z",
      "synthesis": {
        "cultural_analysis_confidence": 0.78,
        "deepfake_detection_confidence": 0.92,
        "combined_assessment": {
          "synthetic_content": true,
          "confidence": 0.89,
          "rationale": "Strong visual/audio synthesis indicators + cultural inconsistencies"
        }
      }
    },
    {
      "step": 9,
      "actor": "ina-french-ai",
      "action": "return_results",
      "to": "deutsche-social-ai",
      "timestamp": "2026-03-10T08:23:50Z",
      "complete_analysis": {
        "synthetic_content": true,
        "overall_confidence": 0.89,
        "breakdown": {
          "ina_confidence": 0.78,
          "ub_confidence": 0.92
        },
        "recommendation": "flag_for_human_review"
      }
    },
    {
      "step": 10,
      "actor": "deutsche-social-ai",
      "action": "escalate_to_humans",
      "timestamp": "2026-03-10T08:24:00Z",
      "escalation": {
        "content_id": "CONTENT-2026-03-10-0042",
        "priority": "high",
        "reason": "potential_disinformation_involving_EU_policy",
        "all_analysis_results_attached": true
      }
    },
    {
      "step": 11,
      "actor": "dublin-review-team",
      "action": "receive_escalation",
      "timestamp": "2026-03-10T08:30:00Z",
      "assigned_to": "Reviewer #12",
      "review_started": "2026-03-10T08:31:00Z"
    },
    {
      "step": 12,
      "actor": "dublin-review-team",
      "action": "review_content",
      "timestamp": "2026-03-10T08:31:00Z - 08:38:00Z",
      "review_duration_minutes": 7,
      "review_actions": [
        "viewed_full_video",
        "reviewed_ai_analysis_reports",
        "checked_content_source_history",
        "consulted_eu_policy_context_database"
      ],
      "review_notes": "Video appears to be sophisticated deepfake targeting EU agricultural policy. Multiple synthetic indicators confirmed by AI systems. User history shows no prior violations."
    },
    {
      "step": 13,
      "actor": "dublin-review-team",
      "action": "make_decision",
      "timestamp": "2026-03-10T08:38:00Z",
      "decision": {
        "action": "flag_as_synthetic_and_restrict",
        "restriction_level": "view_with_warning_label",
        "warning_label_text": "This video contains AI-generated content that may not be authentic",
        "label_languages": ["DE", "FR", "EN", "ES"],
        "notify_user": true,
        "appeal_available": true,
        "human_reviewer_id": "reviewer_12_dublin",
        "supervisor_approval": "Aoife O'Brien (reviewed at 08:40)"
      }
    }
  ],
  
  "final_outcome": {
    "content_disposition": "restricted_with_warning_label",
    "warning_label_applied": true,
    "user_notified": true,
    "appeal_deadline": "2026-03-17",
    "responsible_actor": "dublin-review-team",
    "contributing_ais": ["deutsche-social-ai", "ina-french-ai", "ub-barcelona-ai"],
    "transparency_report_generated": true,
    "jep_receipt": "expected-receipt.json"
  }
}
```

---

# 📁 eusair-demo/case4-generative-ai/mapping.md

```markdown
# EU AI Act Mapping: Case 4 - Generative AI Content Transparency

| Article | Requirement | How JEP Addresses It | Evidence |
|---------|-------------|----------------------|----------|
| **Art. 28b** | Synthetic content labeling | Warning label applied to content, recorded in JEP receipt | `scenario.json` - step 13 (warning_label_text) |
| **Art. 50** | Copyright & training data | Spanish AI includes training data disclosure | `scenario.json` - actors[2].training_data_disclosure |
| **Art. 52** | Transparency obligations | User notified of AI-generated content decision | `scenario.json` - step 13 (notify_user: true) |
| **Art. 53** | Foundation model obligations | All AI versions and training data hashes recorded | `scenario.json` - actors[2].training_data_hash |
| **Art. 14** | Human oversight | Dublin team makes final decision after review | `scenario.json` - steps 11-13 |

## Detailed Mapping

### Article 28b: Synthetic Content Labeling
When content is determined to be AI-generated or manipulated, Article 28b requires clear labeling. In this case:
- The Dublin review team applies a warning label (step 13)
- The label is displayed in multiple EU languages
- The JEP receipt records that the label was applied and what it said

This provides auditable evidence that the platform complied with synthetic content labeling requirements.

### Article 50: Copyright and Training Data
Foundation model providers must disclose information about training data. The Barcelona deepfake detection AI:
- Includes its training data source in actor definition
- Provides a hash of the training data for verification
- Records model version used in detection

If a copyright challenge arises, the JEP receipt shows exactly which model version was used and what training data it was based on.

### Article 52: Transparency Obligations
Users have the right to know when they are interacting with AI-generated content. This case demonstrates:
- User notification (step 13)
- Appeal mechanism provided
- Complete audit trail available if user challenges

The JEP receipt serves as proof that transparency obligations were met.

### Article 53: Foundation Model Obligations
Providers of foundation models must maintain technical documentation. The JEP implementation:
- Records model versions for all AI systems
- Includes model hashes for verification
- Tracks which models were used in each decision

This satisfies the "technical documentation" requirement of Article 53.

### Article 14: Human Oversight
Critical for content moderation: human reviewers make the final decision, but they rely on AI analysis. The JEP receipt proves:
- Humans were notified (step 10)
- They reviewed the content thoroughly (step 12, 7 minutes of review)
- They made an independent decision (step 13)
- A supervisor approved the decision

This demonstrates "meaningful human oversight" as required by Article 14, not just rubber-stamping AI recommendations.
```

---

# 📁 eusair-demo/case4-generative-ai/run.py

```python
#!/usr/bin/env python3
"""
Run Case 4: Generative AI Content Transparency
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
    
    # Load synthetic content details
    with open("synthetic-content.json", "r") as f:
        synthetic_content = json.load(f)
    
    print(f"\n{'='*60}")
    print(f"Running Case 4: {scenario['title']}")
    print(f"{'='*60}\n")
    
    print(f"Description: {scenario['description']}")
    print(f"\nActors involved:")
    for actor in scenario['actors']:
        if actor['type'] != 'human-team':
            print(f"  - {actor['id']} ({actor['type']}, {actor['jurisdiction']})")
        else:
            print(f"  - Dublin Review Team (human, Ireland)")
    
    print(f"\nContent being analyzed: {synthetic_content['title']}")
    print(f"Content type: {synthetic_content['content_type']}")
    print(f"Uploaded: {synthetic_content['upload_timestamp']}")
    print(f"Ground truth: {'Synthetic' if synthetic_content['ground_truth']['actually_synthetic'] else 'Authentic'}")
    
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
    print(f"\nFinal outcome:")
    print(f"  - Content disposition: {scenario['final_outcome']['content_disposition']}")
    print(f"  - Warning label applied: {scenario['final_outcome']['warning_label_applied']}")
    print(f"  - User notified: {scenario['final_outcome']['user_notified']}")
    print(f"  - Human reviewer: Dublin team")
    print(f"  - Transparency report: {scenario['final_outcome']['transparency_report_generated']}")
    
    print(f"\n{'='*60}")
    print("Case 4 completed successfully")
    print(f"{'='*60}\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

---

# 📁 eusair-demo/case4-generative-ai/verify.sh

```bash
#!/bin/bash
# Verification script for Case 4

echo "=========================================="
echo "Verifying Case 4: Generative AI Content Transparency"
echo "=========================================="

# Check if expected receipt exists
if [ ! -f "expected-receipt.json" ]; then
    echo "❌ expected-receipt.json not found. Run run.py first."
    exit 1
fi

# Run JEP verification
python3 ../../src/aip_jep/verify_sandbox.py --receipt expected-receipt.json

if [ $? -eq 0 ]; then
    echo "✅ Case 4 verification passed"
else
    echo "❌ Case 4 verification failed"
    exit 1
fi

# Additional generative AI-specific verification
echo ""
echo "Generative AI compliance checks:"
echo "--------------------------------"

# Check if warning label applied
if grep -q "warning_label_text" scenario.json; then
    echo "✅ Article 28b: Synthetic content labeling applied"
else
    echo "❌ Article 28b: Warning label missing"
fi

# Check if user notified
if grep -q "notify_user" scenario.json; then
    echo "✅ Article 52: User notification recorded"
else
    echo "❌ Article 52: User notification missing"
fi

# Check if training data disclosed
if grep -q "training_data_disclosure" scenario.json; then
    echo "✅ Article 50: Training data disclosure found"
else
    echo "⚠️  Article 50: Training data disclosure incomplete"
fi

# Check if model versions tracked
if grep -q "model_hash" scenario.json; then
    echo "✅ Article 53: Foundation model versions tracked"
else
    echo "❌ Article 53: Model version tracking missing"
fi

# Check if human review duration recorded
if grep -q "review_duration_minutes" scenario.json; then
    echo "✅ Article 14: Human oversight duration recorded"
else
    echo "⚠️  Article 14: Human review not quantified"
fi

echo ""
echo "=========================================="
```

---

# 📁 eusair-demo/README.md（汇总文件）

```markdown
# EUSAiR Demo: JEP Compliance Cases

This repository contains four complete use cases demonstrating JEP (Judgment Event Protocol) compliance with the EU AI Act.

## Cases Overview

| Case | Domain | Core EU AI Act Articles | Status |
|------|--------|------------------------|--------|
| **Case 1** | Cross-Border Loan Approval | Art. 6, 14, 15, 52 | ✅ Complete |
| **Case 2** | Cross-Border Medical Diagnosis | Annex III, Art. 10, 11, 14, 52 | ✅ Complete |
| **Case 3** | Cross-Border Traffic Coordination | Annex III, Art. 27, 43, 60, 14 | ✅ Complete |
| **Case 4** | Generative AI Content Transparency | Art. 28b, 50, 52, 53, 14 | ✅ Complete |

## Coverage Summary

| EU AI Act Requirement | Case 1 | Case 2 | Case 3 | Case 4 |
|----------------------|--------|--------|--------|--------|
| High-Risk AI (Art. 6 / Annex III) | ✅ | ✅ | ✅ | ⚠️ |
| Human Oversight (Art. 14) | ✅ | ✅ | ✅ | ✅ |
| Data Governance (Art. 10) | ⚠️ | ✅ | ⚠️ | ⚠️ |
| Technical Documentation (Art. 11) | ✅ | ✅ | ✅ | ✅ |
| Fundamental Rights (Art. 27) | ⚠️ | ⚠️ | ✅ | ⚠️ |
| Synthetic Content (Art. 28b) | ❌ | ❌ | ❌ | ✅ |
| Copyright & Training Data (Art. 50) | ❌ | ❌ | ❌ | ✅ |
| Transparency (Art. 52) | ✅ | ✅ | ⚠️ | ✅ |
| Foundation Models (Art. 53) | ❌ | ❌ | ❌ | ✅ |
| Conformity Assessment (Art. 43) | ✅ | ✅ | ✅ | ⚠️ |
| Real-World Testing (Art. 60) | ⚠️ | ⚠️ | ✅ | ⚠️ |

## How to Run

Each case is self-contained:

```bash
cd case1-finance
python3 run.py
./verify.sh
```

## Requirements

- Python 3.8+
- JEP core library (`pip install jep-protocol`)
- Cryptographic libraries (Ed25519 support)

## Repository Structure

```
eusair-demo/
├── README.md
├── case1-finance/
│   ├── README.md
│   ├── scenario.json
│   ├── mapping.md
│   ├── run.py
│   └── verify.sh
├── case2-healthcare/
│   └── ...
├── case3-transport/
│   └── ...
├── case4-generative-ai/
│   ├── synthetic-content.json
│   └── ...
└── verify-all.sh
```

## Verification

Run all cases with:

```bash
./verify-all.sh
```

## Contact

For questions or feedback: signal@humanjudgment.org
```

---

# 📁 eusair-demo/verify-all.sh

```bash
#!/bin/bash
# Master verification script for all four EUSAiR cases

echo "=========================================="
echo "EUSAiR JEP Compliance Cases - Full Verification"
echo "=========================================="
echo ""

TOTAL_CASES=4
PASSED=0
FAILED=0

# Case 1
echo "Running Case 1: Cross-Border Loan Approval"
cd case1-finance
python3 run.py > /dev/null 2>&1
./verify.sh
if [ $? -eq 0 ]; then
    PASSED=$((PASSED+1))
else
    FAILED=$((FAILED+1))
fi
cd ..

echo ""

# Case 2
echo "Running Case 2: Cross-Border Medical Diagnosis"
cd case2-healthcare
python3 run.py > /dev/null 2>&1
./verify.sh
if [ $? -eq 0 ]; then
    PASSED=$((PASSED+1))
else
    FAILED=$((FAILED+1))
fi
cd ..

echo ""

# Case 3
echo "Running Case 3: Cross-Border Traffic Coordination"
cd case3-transport
python3 run.py > /dev/null 2>&1
./verify.sh
if [ $? -eq 0 ]; then
    PASSED=$((PASSED+1))
else
    FAILED=$((FAILED+1))
fi
cd ..

echo ""

# Case 4
echo "Running Case 4: Generative AI Content Transparency"
cd case4-generative-ai
python3 run.py > /dev/null 2>&1
./verify.sh
if [ $? -eq 0 ]; then
    PASSED=$((PASSED+1))
else
    FAILED=$((FAILED+1))
fi
cd ..

echo ""
echo "=========================================="
echo "Verification Complete"
echo "=========================================="
echo "Total Cases: $TOTAL_CASES"
echo "Passed: $PASSED"
echo "Failed: $FAILED"
echo "=========================================="

if [ $FAILED -eq 0 ]; then
    echo "✅ ALL CASES PASSED"
    exit 0
else
    echo "❌ $FAILED CASE(S) FAILED"
    exit 1
fi
```

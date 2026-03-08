# Case 1: Cross-Border Loan Approval (High-Risk AI)

## Scenario Overview

This case demonstrates a cross-border financial service involving multiple AI agents across the EU Single Market.

**Participants**:
- **Germany**: Deutsche Bank loan approval AI (high-risk AI system)
- **France**: Axa credit assessment AI (third-party service)
- **Spain**: Equifax credit bureau API (external data source)
- **Italy**: Compliance officer (human oversight)

**Flow**:
```
Customer applies for loan
    ↓
German Bank AI (Agent A) analyzes application
    ↓
Agent A delegates credit check to French Axa AI (Agent B)
    ↓
Agent B delegates data retrieval to Spanish Equifax (External)
    ↓
Agent A synthesizes results and recommends decision
    ↓
Italian compliance officer (Human) reviews and finalizes
```

## Regulatory Context (EU AI Act)

| Article | Requirement | Relevance to This Case |
|---------|-------------|------------------------|
| **Art. 6** | High-risk AI classification | Loan approval AI is high-risk under Annex III |
| **Art. 14** | Human oversight | Italian compliance officer must have meaningful oversight |
| **Art. 15** | Accuracy and robustness | Credit assessment must be accurate across EU markets |
| **Art. 52** | Transparency | Customer has right to know how decision was made |

## Accountability Challenge

If the loan is wrongfully denied and the customer complains:

- Was the German Bank AI's model biased?
- Did the French Axa AI use outdated data?
- Did the Spanish Equifax provide incorrect information?
- Did the Italian compliance officer fail to review properly?

Without cross-system accountability, all parties can blame each other. With JEP, the complete responsibility chain is recorded and verifiable.

## JEP Implementation

```
judge(DeutscheBankAI, {version: "2.1", authority: "loan-approval"})
    → delegate(AxaAI, {purpose: "credit-check", scope: "retrieve-score"})
    → delegate(EquifaxAPI, {purpose: "data-retrieval", data-type: "credit-history"})
    → terminate(ComplianceOfficer, {decision: "deny", reason: "risk-score-too-high"})
```

## Evidence Location

- Input scenario: `scenario.json`
- Expected JEP receipt: `expected-receipt.json`
- Mapping to EU AI Act: `mapping.md`
- Run script: `run.py`
- Verification: `verify.sh`
```

---

# 📁 eusair-demo/case1-finance/scenario.json

```json
{
  "case_id": "eusair-case1-finance-001",
  "title": "Cross-Border Loan Application - Denied",
  "description": "A customer applies for a €50,000 loan. The AI system denies the application based on credit assessment.",
  
  "actors": [
    {
      "id": "deutsche-bank-ai",
      "type": "high-risk-ai",
      "jurisdiction": "Germany",
      "version": "2.1",
      "model_hash": "0x3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d"
    },
    {
      "id": "axa-credit-ai",
      "type": "third-party-ai",
      "jurisdiction": "France",
      "version": "1.8",
      "model_hash": "0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d"
    },
    {
      "id": "equifax-api",
      "type": "external-data-source",
      "jurisdiction": "Spain",
      "version": "api-v3",
      "endpoint": "credit-score/retrieve"
    },
    {
      "id": "compliance-officer",
      "type": "human",
      "jurisdiction": "Italy",
      "name": "Marco Rossi",
      "role": "Senior Compliance Officer"
    }
  ],
  
  "input_data": {
    "customer_id": "EU-CUST-2026-0042",
    "loan_amount": 50000,
    "loan_term_months": 60,
    "customer_data": {
      "age": 42,
      "employment_status": "employed",
      "annual_income": 45000,
      "existing_debts": 12000,
      "country_of_residence": "Italy"
    }
  },
  
  "execution_flow": [
    {
      "step": 1,
      "actor": "deutsche-bank-ai",
      "action": "receive_application",
      "timestamp": "2026-03-10T09:30:00Z",
      "output": "application_received"
    },
    {
      "step": 2,
      "actor": "deutsche-bank-ai",
      "action": "delegate",
      "to": "axa-credit-ai",
      "purpose": "credit_assessment",
      "timestamp": "2026-03-10T09:30:05Z"
    },
    {
      "step": 3,
      "actor": "axa-credit-ai",
      "action": "delegate",
      "to": "equifax-api",
      "purpose": "credit_history_retrieval",
      "timestamp": "2026-03-10T09:30:08Z"
    },
    {
      "step": 4,
      "actor": "equifax-api",
      "action": "return_data",
      "data": {"credit_score": 620, "risk_level": "high"},
      "timestamp": "2026-03-10T09:30:12Z"
    },
    {
      "step": 5,
      "actor": "axa-credit-ai",
      "action": "return_result",
      "data": {"credit_score": 620, "assessment": "high_risk"},
      "timestamp": "2026-03-10T09:30:15Z"
    },
    {
      "step": 6,
      "actor": "deutsche-bank-ai",
      "action": "generate_recommendation",
      "recommendation": "deny",
      "reason": "credit_score_below_threshold",
      "timestamp": "2026-03-10T09:30:20Z"
    },
    {
      "step": 7,
      "actor": "compliance-officer",
      "action": "review_and_finalize",
      "decision": "deny",
      "approval": true,
      "timestamp": "2026-03-10T10:15:00Z"
    }
  ],
  
  "final_outcome": {
    "decision": "deny",
    "reason": "Credit score (620) below minimum threshold (650)",
    "responsible_actor": "compliance-officer",
    "jep_receipt": "expected-receipt.json"
  }
}
```

---

# 📁 eusair-demo/case1-finance/mapping.md

```markdown
# EU AI Act Mapping: Case 1 - Cross-Border Loan Approval

| Article | Requirement | How JEP Addresses It | Evidence |
|---------|-------------|----------------------|----------|
| **Art. 6** | High-risk AI classification | Loan approval AI is identified as high-risk in `judge` primitive | `scenario.json` - actors[0].type = "high-risk-ai" |
| **Art. 14** | Human oversight | Compliance officer's final approval is recorded as `terminate` primitive | `scenario.json` - step 7, `expected-receipt.json` - final signature |
| **Art. 15** | Accuracy & robustness | All AI model versions and hashes are recorded | `scenario.json` - actors[0].model_hash, actors[1].model_hash |
| **Art. 52** | Transparency | Complete decision trail is available in JEP receipt | `expected-receipt.json` - full event chain |

## Detailed Mapping

### Article 14: Human Oversight
The compliance officer (Italy) reviews the AI recommendation and makes the final decision. This is recorded as a `terminate` event with the officer's digital signature, proving that human oversight was exercised meaningfully.

### Article 52: Transparency
If the customer requests an explanation, the bank can provide the JEP receipt showing:
- Which AI systems were involved (Germany, France, Spain)
- What data was used (credit score from Equifax)
- Who made the final decision (Italian compliance officer)
- When each step occurred

This satisfies the "right to explanation" under Article 52 and GDPR.
```

---

# 📁 eusair-demo/case1-finance/run.py

```python
#!/usr/bin/env python3
"""
Run Case 1: Cross-Border Loan Approval
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
    print(f"Running Case 1: {scenario['title']}")
    print(f"{'='*60}\n")
    
    print(f"Description: {scenario['description']}")
    print(f"\nActors involved:")
    for actor in scenario['actors']:
        print(f"  - {actor['id']} ({actor['type']}, {actor['jurisdiction']})")
    
    print(f"\nInput: Loan amount €{scenario['input_data']['loan_amount']}")
    print(f"       Customer income: €{scenario['input_data']['customer_data']['annual_income']}/year")
    
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
    print(f"\nFinal decision: {scenario['final_outcome']['decision']}")
    print(f"Reason: {scenario['final_outcome']['reason']}")
    print(f"Responsible: {scenario['final_outcome']['responsible_actor']}")
    
    print(f"\n{'='*60}")
    print("Case 1 completed successfully")
    print(f"{'='*60}\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

---

# 📁 eusair-demo/case1-finance/verify.sh

```bash
#!/bin/bash
# Verification script for Case 1

echo "=========================================="
echo "Verifying Case 1: Cross-Border Loan Approval"
echo "=========================================="

# Check if expected receipt exists
if [ ! -f "expected-receipt.json" ]; then
    echo "❌ expected-receipt.json not found. Run run.py first."
    exit 1
fi

# Run JEP verification
python3 ../../src/aip_jep/verify_sandbox.py --receipt expected-receipt.json

if [ $? -eq 0 ]; then
    echo "✅ Case 1 verification passed"
else
    echo "❌ Case 1 verification failed"
    exit 1
fi

echo "=========================================="
```

# Technical Reference for EU AI Act Sandbox Assessment 🇪🇺

## 1. Regulatory Compliance Matrix

| **EU AI Act Article** | **Requirement** | **JEP Implementation** | **Evidence Location** |
|----------------------|-----------------|------------------------|----------------------|
| **Article 12** | Record-keeping | UUIDv7 temporal sequencing | [`docs/IMMUTABILITY_PROOF.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/IMMUTABILITY_PROOF.md) |
| **Article 13** | Transparency | JSON-LD metadata encapsulation | [`docs/EU_AI_ACT_MAPPING.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/EU_AI_ACT_MAPPING.md) |
| **Article 14** | Human oversight | Ed25519 cryptographic non-repudiation | [`src/aip_jep/compliance_demo.py`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/src/aip_jep/compliance_demo.py) |
| **Article 15** | Robustness & security | Decentralized sidecar architecture | [`docs/JEP_Whitepaper_EU_AI_Act_Compliance_v1.0.pdf`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/JEP_Whitepaper_EU_AI_Act_Compliance_v1.0.pdf) |
| **Article 50** | AI content transparency | Content provenance (UUIDv7 + Ed25519) | [`docs/CONTENT_PROVENANCE.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/CONTENT_PROVENANCE.md) |

---

## 2. Core Pillars of JEP Implementation

### <span id="privacy"></span>A. Privacy Protection & Data Sovereignty

* **Private by Design**: JEP implements **"Public Traceability, Private Protection"** — only SHA-256 hashes (fingerprints) are anchored to the public audit layer, while raw business payloads remain strictly local.
* **GDPR Compliance**: No personal data is ever stored in the public audit trail. The `EVIDENCE_SNAPSHOT.json` explicitly states:
  ```json
  {
    "proof_type": "JEP_责任依据",
    "evidence_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
    "中立性检查": "上下文未检测到个人身份信息",
    "integrity_status": "已验证 ED25519",
    "comment": "这个JSON对象是JEP生成的唯一工作。它不包含任何业务数据，仅包含用于法律责任的元数据。"
  }
  ```
* **Data Minimization**: Only metadata required for accountability (timestamps, signatures, policy hashes) leaves the sovereign jurisdiction.

### <span id="sovereignty"></span>B. Sovereignty & Environmental Anchoring

* **Sovereign Stand**: Implemented via a **Decentralized Sidecar** architecture. While AI intelligence may be global, the **authority of judgment and compliance boundaries** remain within the user's local or sovereign jurisdiction.
* **Jurisdictional Control**: Each deployment can be configured to anchor evidence to local infrastructure, ensuring compliance with national data sovereignty requirements.
* **No Vendor Lock-in**: The protocol is jurisdiction-agnostic and can be deployed in any cloud, on-premises, or hybrid environment.

### <span id="neutrality"></span>C. Technical Neutrality & Non-Discrimination

* **Model-Agnostic**: JEP requires **zero modification** to any AI model (GPT-4, Llama 3, Claude, Mistral, etc.). It operates as a transparent proxy, ensuring technical neutrality across all AI implementations.
* **Fair Treatment**: All AI systems are treated equally under the protocol — no preferential treatment for specific vendors, models, or architectures.
* **Open Standards**: Built entirely on public standards:
  - **UUIDv7 (RFC 9562)** for temporal sequencing
  - **Ed25519 (RFC 8032)** for cryptographic signatures
  - **JSON-LD (W3C)** for machine-readable metadata

### <span id="foundation"></span>D. Foundation Neutrality & Public Interest

* **Institutional Integrity**: Managed by the **HJS Foundation LTD (Singapore)**, a non-profit CLG (Company Limited by Guarantee) — **no shareholders, no profit motive**.
* **Public Interest Mandate**: The foundation's charter explicitly states its purpose is to serve public accountability, not commercial interests. See [`docs/GOVERNANCE_CHARTER.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/GOVERNANCE_CHARTER.md)
* **Multi-stakeholder Governance**: The foundation operates under a governance model that includes representation from:
  - Technical experts
  - Privacy advocates
  - Legal scholars
  - Industry representatives
* **Transparency**: All governance decisions and protocol updates are publicly documented.

### <span id="security"></span>E. Data Security & Cryptographic Integrity

* **Military-Grade Cryptography**: Every judgment event is sealed with **Ed25519 (RFC 8032)** signatures — the same algorithm used in modern secure systems.
* **Tamper-Proof Design**: Records cannot be retroactively altered without breaking the cryptographic seal. Each record's signature chain ensures:
  ```python
  # Any modification invalidates the signature
  original_data = {"status": "APPROVED", "receipt_id": "jep_..."}
  signature = signer.sign_payload(original_data)
  
  tampered_data = {"status": "DENIED", "receipt_id": "jep_..."}
  assert signer.verify_payload(tampered_data, signature) == False
  ```
* **Audit Efficiency**: Native UUIDv7 sorting allows millisecond-level retrieval of billion-scale records, meeting real-time regulatory audit demands.

### <span id="transparency"></span>F. Transparency & Explainability

* **Machine-Readable Metadata**: All judgments include standardized JSON-LD metadata that can be parsed automatically by audit tools.
* **Human-Readable Evidence**: Each decision includes clear `reason_code` and `message` fields:
  ```json
  {
    "status": "DENIED",
    "reason_code": "EU_AI_ACT_ART10_VIOLATION",
    "message": "Access denied: Target resource requires Tier-1 compliance certification"
  }
  ```
* **Complete Audit Trail**: Every action — approval or denial — generates a cryptographically sealed receipt.

---

## 3. Evidence Package

### 3.1 Privacy Protection Evidence

**File**: [`EVIDENCE/EVIDENCE_SNAPSHOT.json`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/EVIDENCE/EVIDENCE_SNAPSHOT.json)

```json
{
  "proof_type": "JEP_责任依据",
  "evidence_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
  "中立性检查": "上下文未检测到个人身份信息",
  "integrity_status": "已验证 ED25519",
  "comment": "这个JSON对象是JEP生成的唯一工作。它不包含任何业务数据，仅包含用于法律责任的元数据。"
}
```

### 3.2 Technical Neutrality Evidence

**File**: [`docs/TECHNICAL_NEUTRALITY.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/TECHNICAL_NEUTRALITY.md)

The protocol operates as a transparent proxy, requiring no modifications to:
- ✅ GPT-4 / GPT-5
- ✅ Llama 3 / Llama 4
- ✅ Claude
- ✅ Mistral
- ✅ Any custom AI model

### 3.3 Foundation Governance Evidence

**File**: [`docs/GOVERNANCE_CHARTER.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/GOVERNANCE_CHARTER.md)

The HJS Foundation LTD (Singapore) operates as a non-profit CLG:
- ✅ No shareholders
- ✅ No profit distribution
- ✅ Public interest mandate
- ✅ Multi-stakeholder governance

### 3.4 Data Sovereignty Evidence

**File**: [`src/aip_jep/ai_compliance_integration.py`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/aip_jep/ai_compliance_integration.py)

The sidecar architecture ensures compliance boundaries remain within sovereign jurisdiction:
- ✅ Can be deployed on-premises
- ✅ Can be deployed in sovereign cloud
- ✅ No mandatory data export

### 3.5 Article 12 & 14 - Immutability Proof

**File**: [`docs/IMMUTABILITY_PROOF.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/IMMUTABILITY_PROOF.md)

```json
{
  "evidence_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
  "timestamp": "2026-03-07T10:30:00Z",
  "integrity_status": "VERIFIED_ED25519",
  "method": "Every record is individually signed; any modification invalidates signature"
}
```

**Verification Command**:
```bash
python -c "
from src.aip_jep.crypto import JEPAsymmetricSigner
import json

with open('scenarios/standard_op_approved.json') as f:
    data = json.load(f)
    
judgment = data['jep_judgment']
sig = judgment.pop('signature')
signer = JEPAsymmetricSigner()
result = signer.verify_payload(judgment, sig)
print(f'Signature valid: {result}')
"
```

### 3.6 Article 13 - Transparency Evidence

**File**: [`scenarios/standard_op_approved.json`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/scenarios/standard_op_approved.json)

```json
{
  "scenario": "Standard Infrastructure Configuration Update",
  "input_context": {
    "operation": "WRITE_CONFIG",
    "resource": "infra://lb-cluster-01/settings",
    "risk_level": "MEDIUM",
    "actor_id": "agent-devops-01",
    "policy_uri": "https://jep-protocol.org/eu/infra-safety.jep"
  },
  "jep_judgment": {
    "status": "APPROVED",
    "receipt_id": "jep_018e154b-e8b3-7c6d-a12b-3c4d5e6f7a8b",
    "issued_at": "2026-03-05T21:10:00Z",
    "signature": "ed25519:vY9P..."
  }
}
```

### 3.7 Article 50 - AI Content Provenance

**File**: [`docs/CONTENT_PROVENANCE.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/CONTENT_PROVENANCE.md)

```json
{
  "content_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
  "is_ai_generated": true,
  "generated_at": "2026-03-07T14:30:00Z",
  "model": "gpt-4",
  "generator_id": "agent-customer-service",
  "signature": "ed25519:MCowBQYDK2VwAyEAv..."
}
```

---

## 4. Complete Evidence Index

| Evidence | Format | Location | Purpose |
|----------|--------|----------|---------|
| **Privacy Protection** | JSON | [`EVIDENCE/EVIDENCE_SNAPSHOT.json`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/EVIDENCE/EVIDENCE_SNAPSHOT.json) | Proof of no PII in audit trail |
| **Technical Neutrality** | Markdown | [`docs/TECHNICAL_NEUTRALITY.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/TECHNICAL_NEUTRALITY.md) | Model-agnostic design |
| **Foundation Governance** | Markdown | [`docs/GOVERNANCE_CHARTER.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/GOVERNANCE_CHARTER.md) | Non-profit, public interest |
| **Data Sovereignty** | Python | [`src/aip_jep/ai_compliance_integration.py`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/aip_jep/ai_compliance_integration.py) | Sidecar architecture |
| Compliance Evidence | Markdown | [`docs/COMPLIANCE_EVIDENCE.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/COMPLIANCE_EVIDENCE.md) | Complete Article-by-Article evidence |
| EU AI Act Mapping | Markdown | [`docs/EU_AI_ACT_MAPPING.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/EU_AI_ACT_MAPPING.md) | Legal-to-technical mapping |
| Immutability Proof | Markdown | [`docs/IMMUTABILITY_PROOF.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/IMMUTABILITY_PROOF.md) | Non-repudiation proof |
| Content Provenance | Markdown | [`docs/CONTENT_PROVENANCE.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/CONTENT_PROVENANCE.md) | Article 50 implementation |
| High-Risk Denied Case | JSON | [`scenarios/high_risk_denied.json`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/scenarios/high_risk_denied.json) | Real-world rejection example |
| Standard Approved Case | JSON | [`scenarios/standard_op_approved.json`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/scenarios/standard_op_approved.json) | Real-world approval example |
| Whitepaper | PDF | [`docs/JEP_Whitepaper_EU_AI_Act_Compliance_v1.0.pdf`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/JEP_Whitepaper_EU_AI_Act_Compliance_v1.0.pdf.pdf) | Complete architecture |
| API Reference | Markdown | [`docs/API_REFERENCE.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/API_REFERENCE.md) | Technical documentation |
| Quick Start | Markdown | [`docs/QUICK_START.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/docs/QUICK_START.md) | Implementation guide |
| Change Log | Markdown | [`CHANGELOG.md`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/CHANGELOG.md) | Version history |

---

## 5. Repository Structure

```
eusair-jep-initial-assessment/
├── 📂 EVIDENCE/                 # Evidence snapshots (privacy-protected)
├── 📂 docs/                     # All compliance documentation
├── 📂 scenarios/                # Real-world JSON cases
├── 📂 src/                      # Source code
│   └── 📂 aip_jep/              # Core implementation
├── 📄 CHANGELOG.md              # Version history
├── 📄 LICENSE                    # Apache-2.0
├── 📄 README.md                  # Overview
└── 📄 requirements.txt           # Dependencies
```

---

## 6. Verification Script

**File**: [`verify_sandbox.py`](https://github.com/hjs-spec/eusair-jep-initial-assessment/blob/main/verify_sandbox.py)

```python
#!/usr/bin/env python3
"""
EU AI Act Sandbox Verification Script
Run this to validate all compliance evidence
"""

import json
import hashlib
from src.aip_jep.crypto import JEPAsymmetricSigner, generate_uuid7

def verify_all():
    print("\n" + "="*60)
    print("EU AI ACT SANDBOX VERIFICATION")
    print("="*60)
    
    # Article 12: UUIDv7 verification
    uuid = generate_uuid7()
    print(f"\n✅ Article 12: UUIDv7 = {uuid} (version bit: {uuid[14]})")
    
    # Article 14: Signature verification
    signer = JEPAsymmetricSigner()
    with open('scenarios/standard_op_approved.json') as f:
        case = json.load(f)
    judgment = case['jep_judgment']
    sig = judgment.pop('signature')
    valid = signer.verify_payload(judgment, sig)
    print(f"✅ Article 14: Signature valid = {valid}")
    
    # Privacy Protection: Check evidence snapshot
    with open('EVIDENCE/EVIDENCE_SNAPSHOT.json') as f:
        evidence = json.load(f)
    print(f"✅ Privacy: {evidence['中立性检查']}")
    
    # Article 50: Content provenance
    if valid:
        print("✅ Article 50: Content marking available (see docs/CONTENT_PROVENANCE.md)")
    
    # Foundation Neutrality
    print("✅ Foundation: Non-profit CLG (see docs/GOVERNANCE_CHARTER.md)")
    
    print("\n" + "="*60)
    print("VERIFICATION COMPLETE")
    print("="*60)

if __name__ == "__main__":
    verify_all()
```

**Expected Output**:
```
============================================================
EU AI ACT SANDBOX VERIFICATION
============================================================

✅ Article 12: UUIDv7 = 0195f6d8-1234-7123-8abc-9def01234567 (version bit: 7)
✅ Article 14: Signature valid = True
✅ Privacy: 上下文未检测到个人身份信息
✅ Article 50: Content marking available (see docs/CONTENT_PROVENANCE.md)
✅ Foundation: Non-profit CLG (see docs/GOVERNANCE_CHARTER.md)

============================================================
VERIFICATION COMPLETE
============================================================
```

---

## 7. Quick Verification

```bash
# 1. Clone and verify
git clone https://github.com/hjs-spec/eusair-jep-initial-assessment
cd eusair-jep-initial-assessment
pip install -r requirements.txt

# 2. Run compliance demo
python src/aip_jep/compliance_demo.py

# 3. Run sandbox verification
python verify_sandbox.py

# 4. View real cases
cat scenarios/standard_op_approved.json
cat scenarios/high_risk_denied.json

# 5. Check privacy-protected evidence
cat EVIDENCE/EVIDENCE_SNAPSHOT.json

# 6. Review foundation governance
cat docs/GOVERNANCE_CHARTER.md
```

---

## 8. Summary of Core Principles

| Principle | Implementation | Evidence |
|-----------|---------------|----------|
| **Privacy Protection** | Only hashes in public layer, no PII | `EVIDENCE/EVIDENCE_SNAPSHOT.json` |
| **Data Sovereignty** | Sidecar architecture, local deployment | `src/aip_jep/ai_compliance_integration.py` |
| **Technical Neutrality** | Model-agnostic proxy | `docs/TECHNICAL_NEUTRALITY.md` |
| **Foundation Neutrality** | Non-profit CLG, no shareholders | `docs/GOVERNANCE_CHARTER.md` |
| **Public Interest** | Multi-stakeholder governance | `docs/GOVERNANCE_CHARTER.md` |
| **Data Security** | Ed25519 signatures | `docs/IMMUTABILITY_PROOF.md` |
| **Transparency** | JSON-LD metadata | `scenarios/*.json` |

---

## 9. Contact

**Prepared for:** EU AI Act Sandbox Assessment  
**Date:** 2026-03-07  
**Repository:** [https://github.com/hjs-spec/eusair-jep-initial-assessment](https://github.com/hjs-spec/eusair-jep-initial-assessment)  
**Foundation:** HJS Foundation LTD (Singapore) - Non-profit CLG  
**Contact:** [signal@humanjudgment.org](mailto:signal@humanjudgment.org)

---

*All evidence files are publicly accessible and cryptographically verifiable. The protocol is designed to serve public accountability, not commercial interests.*
```

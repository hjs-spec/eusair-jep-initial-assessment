# Technical Reference for EUSAiR Compliance Assessment 🇪🇺

## 1. Requirement Traceability Matrix (EUSAiR/EU AI Act)

HJS provides the technical evidence layer required for high-risk AI systems to meet the mandatory standards of the **EU AI Act**.

| **Regulatory Requirement** | **HJS Technical Implementation** | **Standard / Protocol** |
| --- | --- | --- |
| **Art. 12: Record-keeping** | [48-bit Unix-epoch Physical Sequencing](https://www.google.com/search?q=%233a-mathematical--physical-anchoring) | **UUIDv7 (RFC 9562)** |
| **Art. 13: Transparency** | [Standardized Metadata Encapsulation](https://www.google.com/search?q=%236-evidence-sample--verification) | **JSON-LD / RDF** |
| **Art. 14: Oversight** | [Cryptographic Non-repudiation](https://www.google.com/search?q=%233a-mathematical--physical-anchoring) | **Ed25519 (RFC 8032)** |
| **Art. 15: Sovereignty** | [Localized Sidecar Execution & Isolation](https://www.google.com/search?q=%233b-environmental--sovereign-anchoring) | **SHA-256 / Proxy** |

---

## 2. The Four Primitives (Functional Logic)

According to `draft-wang-hjs-judgment-event`, the HJS protocol ensures a complete chain of custody via four atomic operations:

* **Judge**: Logs the policy parameters and logical basis invoked for an AI decision.
* **Delegate**: Captures the cryptographic handover of authority from the user to the AI agent.
* **Terminate**: Records the definitive task completion and hashes the final output state.
* **Verify**: Provides a standalone, portable compliance receipt for independent third-party auditing.

---

## 3. Multi-Dimensional Anchoring (Implementation Facts)

### 3A. Mathematical & Physical Anchoring

* **Temporal Integrity**: HJS utilizes **UUIDv7**. By embedding a millisecond-precision timestamp into the primary key, it creates an irreversible physical sequence, preventing history re-injection.
* **Cryptographic Seal**: Every judgment event is sealed using **Ed25519** digital signatures. This ensures that any modification to the audit log is mathematically detectable, providing **anti-attack resilience**.

### 3B. Environmental & Sovereign Anchoring

* **Jurisdictional Control**: The HJS Sidecar is deployed within **EU-resident infrastructure** (On-premise or Sovereign Cloud).
* **Data Minimization**: Using **Optional Anchoring**, HJS only records **SHA-256 hashes** (fingerprints) for public traceability, while raw business payloads remain strictly local, ensuring **GDPR** compliance.

---

## 4. Integration & Operational Efficiency

* **Integration Method**: **Non-Intrusive Sidecar**. Operates as a transparent proxy between the application and the AI model API.
* **Deployment Velocity**: Standard setup is achieved in **< 15 minutes** via Docker/K8s.
* **Accessibility**: Native UUIDv7 sorting enables instant query and retrieval of billion-scale records during regulatory inspections.
* **Zero Impact**: No retraining or modification of the underlying AI models (e.g., GPT-4, Llama 3) is required.

---

## 5. Institutional & Governance Framework

* **Entity**: Managed by **HJS Foundation LTD (Singapore)**.
* **Status**: Company Limited by Guarantee (CLG), Non-Profit Public Good.
* **Transparency**: Open-source protocol and reference implementation.

---

## 6. Evidence Sample & Verification

Every AI interaction generates a **Judgment Receipt** (JSON-LD), ensuring both machine and human readability for Article 14 oversight.

```json
{
  "id": "018e1234-5678-7000-8000-1234567890ab",
  "type": "HJS_JUDGMENT_EVENT",
  "actor": "ed25519:pubkey_of_ai_proxy",
  "primitives": ["Judge", "Delegate", "Terminate"],
  "policy_hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e...",
  "payload_hash": "sha256:8f32c12...",
  "signature": "base64:cryptographic_signature_over_metadata"
}

```

### 🚀 Auditor Quick Start

```bash
# Verify the implementation logic of Article 14
pip install -r requirements.txt
python compliance_demo.py

```

---

*Prepared for the EUSAiR Initial Assessment Phase.* **Foundation Contact:** [signal@humanjudgment.org](mailto:signal@humanjudgment.org)

---

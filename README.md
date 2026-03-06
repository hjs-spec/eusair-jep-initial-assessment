# Technical Reference for EUSAiR Compliance Assessment 🇪🇺

## 1. Regulatory Compliance Mapping

This matrix provides a direct bridge between the legal mandates of the **EU AI Act** and the engineering facts of the HJS Protocol.

| **EU AI Act Clause** | **Regulatory Requirement** | **HJS Technical Implementation (View Logic)** | **Verification Evidence (Open File)** |
| --- | --- | --- | --- |
| **Article 12** | **Record-keeping** | [Physical Temporal Sequencing via UUIDv7] | [IMMUTABILITY_PROOF.md](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/IMMUTABILITY_PROOF.md) |
| **Article 13** | **Transparency** | [Standardized Metadata Encapsulation (JSON-LD)] | [EU_AI_ACT_MAPPING.md](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/EU_AI_ACT_MAPPING.md) |
| **Article 14** | **Human Oversight** | [Cryptographic Non-repudiation via Ed25519] | **[compliance_demo.py](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/compliance_demo.py)** |
| **Article 15** | **Robustness & Security** | [Decentralized Sidecar for Local Sovereignty] | **[HJS_Whitepaper.pdf](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/docs/HJS_Whitepaper_EU_AI_Act_Compliance_v1.0.pdf)** |

---

## 2. Core Pillars of HJS Implementation

### <span id="physical"></span>A. Mathematical & Physical Anchoring

* **Physical Fact**: Utilizing **UUIDv7 (RFC 9562)** to bind AI events to an irreversible physical timeline. This ensures native chronological ordering and prevents history re-injection.
* **Mathematical Fact**: Every judgment event is sealed with **Ed25519 (RFC 8032)** signatures. This ensures **Anti-Attack Resilience**; records cannot be retroactively altered without breaking the cryptographic seal.
* **Audit Efficiency**: Native UUIDv7 sorting allows databases to perform millisecond-level retrieval of billion-scale records, meeting real-time regulatory audit demands.

### <span id="sovereign"></span>B. Sovereignty & Environmental Anchoring

* **Sovereign Stand**: Implemented via a **Decentralized Sidecar** architecture. While AI intelligence may be global, the **authority of judgment and compliance boundaries** remain within the user’s local or sovereign jurisdiction.
* **Optional Anchoring**: Supports "Public Traceability, Private Protection." Only **SHA-256 hashes** (fingerprints) are anchored to the public audit layer, while raw business payloads remain strictly local, ensuring full **GDPR** compliance.

### <span id="integration"></a>C. Engineering Velocity & Integration

* **Non-Intrusive Integration**: Operates as a transparent proxy. It requires **zero modification** to existing AI models (e.g., GPT-5, Llama 3) or core business logic.
* **Deployment Time**: Standard production environment setup is achieved in **< 15 minutes** via Docker or Kubernetes.
* **Zero Overhead**: Minimal latency impact, ensuring compliance does not compromise AI performance.

### <a name="primitives"></a>D. Accountability Primitives

* **The Four Primitives**: Following `draft-wang-hjs-judgment-event`, HJS establishes accountability through **Judge, Delegate, Terminate, and Verify** operations.
* **Institutional Integrity**: Managed by the **HJS Foundation LTD (Singapore)**, a non-profit CLG.

---

### <span id="transparency"></span>3. Evidence Sample & Data Structure

Example of a **Judgment Receipt** compliant with Article 13 requirements:

```json
{
  "id": "018e1234-5678-7000-8000-1234567890ab", // Physical time-sequence index
  "type": "HJS_JUDGMENT_EVENT",
  "actor": "ed25519:pubkey_of_ai_proxy",
  "primitives": ["Judge", "Delegate", "Terminate"],
  "policy_hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e...",
  "payload_hash": "sha256:8f32c12... (Payload remains in local sovereignty)",
  "signature": "base64:cryptographic_signature_over_metadata"
}

```

---

## 4. Compliance Artifacts

* 📄 **[IMMUTABILITY_PROOF.md](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/IMMUTABILITY_PROOF.md)**: Proof of non-repudiation.
* 📄 **[EU_AI_ACT_MAPPING.md](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/EU_AI_ACT_MAPPING.md)**: Regulatory field mapping.
* 💻 **[compliance_demo.py](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/compliance_demo.py)**: Live execution of Article 14 oversight.
* 📕 **[HJS_Whitepaper_v1.0.pdf](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/docs/HJS_Whitepaper_EU_AI_Act_Compliance_v1.0.pdf)**: Complete architectural reference.

---

## 🚀 Auditor Quick Start

```bash
# Verify the implementation logic in seconds
pip install -r requirements.txt
python compliance_demo.py

```

---

*Prepared for the EUSAiR Initial Assessment Phase.* **Foundation Contact:** [signal@humanjudgment.org](mailto:signal@humanjudgment.org)

---

# Technical Reference for EUSAiR Compliance Assessment 🇪🇺

## 1. Regulatory Compliance Mapping

Based on the mandatory requirements for High-Risk AI systems under the **EU AI Act**, HJS provides the following technical implementations:

| **EU AI Act Clause** | **Regulatory Requirement** | **HJS Technical Implementation (Click to view)** | **Verification Evidence** |
| --- | --- | --- | --- |
| **Article 12** | **Record-keeping** | [Physical Temporal Sequencing via UUIDv7](https://www.google.com/search?q=%23physical) | [Technical Proof](https://www.google.com/search?q=./IMMUTABILITY_PROOF.md) |
| **Article 13** | **Transparency** | [Standardized Metadata Encapsulation (JSON-LD)](https://www.google.com/search?q=%23transparency) | [Mapping Guide](https://www.google.com/search?q=./EU_AI_ACT_MAPPING.md) |
| **Article 14** | **Human Oversight** | [Cryptographic Non-repudiation via Ed25519](https://www.google.com/search?q=%23physical) | **[Live Demo](https://www.google.com/search?q=./compliance_demo.py)** |
| **Article 15** | **Robustness & Security** | [Decentralized Sidecar for Local Sovereignty](https://www.google.com/search?q=%23sovereign) | **[Whitepaper](https://www.google.com/search?q=./docs/HJS_Whitepaper_v1.0.pdf)** |

---

## 2. Core Pillars of HJS Implementation

### <a name="physical"></a>A. Mathematical & Physical Anchoring

* **Physical Fact**: Utilizing **UUIDv7 (RFC 9562)** to bind AI events to an irreversible physical timeline. This ensures native chronological ordering and prevents history re-injection or manipulation.
* **Mathematical Fact**: Every judgment event is sealed with **Ed25519 (RFC 8032)** signatures. This ensures **Anti-Attack Resilience**; records cannot be retroactively altered without breaking the cryptographic seal.
* **Audit Efficiency**: Native UUIDv7 sorting allows databases to perform millisecond-level retrieval of billion-scale records, meeting real-time regulatory audit demands.

### <a name="sovereign"></a>B. Sovereignty & Environmental Anchoring

* **Sovereign Stand**: Implemented via a **Decentralized Sidecar** architecture. While AI intelligence may be global, the **authority of judgment and compliance boundaries** remain within the user’s local or sovereign jurisdiction.
* **Optional Anchoring**: Supports "Public Traceability, Private Protection." Only **SHA-256 hashes** (fingerprints) are anchored to the public audit layer, while raw business payloads remain strictly local, ensuring full **GDPR** compliance.

### <a name="integration"></a>C. Engineering Velocity & Integration

* **Non-Intrusive Integration**: Operates as a transparent proxy. It requires **zero modification** to existing AI models (e.g., GPT-4, Llama 3) or core business logic.
* **Deployment Time**: Standard production environment setup is achieved in **< 15 minutes** via Docker or Kubernetes.
* **Frictionless Compliance**: By converting complex legal clauses (Art. 12-15) into a simple technical plug-in, HJS significantly lowers the barrier for enterprise compliance.

### <a name="primitives"></a>D. Accountability Primitives & Public Good

* **The Four Primitives**: Following `draft-wang-hjs-judgment-event`, HJS establishes accountability through **Judge, Delegate, Terminate, and Verify** operations.
* **Institutional Integrity**: Managed by the **HJS Foundation LTD (Singapore)**, a non-profit Company Limited by Guarantee (CLG). The protocol is open-source and serves as a neutral global infrastructure.

---

### <a name="transparency"></a>3. Evidence Sample & Transparency

Example of a **Judgment Receipt** compliant with Article 13 requirements:

```json
{
  "id": "018e1234-5678-7000-8000-1234567890ab", // Physical time-based unique index
  "type": "HJS_JUDGMENT_EVENT",
  "actor": "ed25519:pubkey_of_ai_proxy",
  "primitives": ["Judge", "Delegate", "Terminate"],
  "policy_hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e...",
  "payload_hash": "sha256:8f32c12... (Payload remains local)",
  "signature": "base64:cryptographic_signature_over_metadata"
}

```

---

## 4. Compliance Artifacts

* 📄 **[EU_AI_ACT_MAPPING.md](https://www.google.com/search?q=./EU_AI_ACT_MAPPING.md)**: Detailed clause-by-clause mapping.
* 💻 **[compliance_demo.py](https://www.google.com/search?q=./compliance_demo.py)**: Live execution script for Article 14 verification.
* 📂 **[Scenario Sandbox](https://www.google.com/search?q=./scenarios/)**: Simulation environment for regulatory "Approve/Reject" flows.
* 📕 **[Technical Whitepaper (PDF)](https://www.google.com/search?q=./docs/HJS_Whitepaper_v1.0.pdf)**: Comprehensive architectural reference.

---

## 🚀 Auditor Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the compliance generator (Verifies Article 14)
python compliance_demo.py

```

---

*Prepared for the EUSAiR Initial Assessment Phase.* **Foundation Contact:** [signal@humanjudgment.org](mailto:signal@humanjudgment.org)

---

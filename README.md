# EUSAiR Initial Assessment: HJS Protocol Implementation 🇪🇺

## 1. Regulatory Compliance Mapping (EU AI Act)

HJS provides the technical implementation layer required for high-risk AI systems under the European AI Act:

| **EU AI Act Clause** | **Regulatory Requirement** | **HJS Technical Implementation** | **Verification Evidence** |
| --- | --- | --- | --- |
| **Article 12** | **Record-keeping** | Chronological sequencing via **UUIDv7 (RFC 9562)** | [Technical Proof](https://www.google.com/search?q=./IMMUTABILITY_PROOF.md) |
| **Article 13** | **Transparency** | Standardized metadata wrapper (**JSON-LD/RDF**) | [Mapping Guide](https://www.google.com/search?q=./EU_AI_ACT_MAPPING.md) |
| **Article 14** | **Human Oversight** | Non-repudiation via **Ed25519 Cryptographic Signatures** | **[Live Demo](https://www.google.com/search?q=./compliance_demo.py)** |
| **Article 15** | **Security & Robustness** | **Decentralized Sidecar** for localized sovereignty | **[Whitepaper (PDF)](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/docs/HJS_Whitepaper_EU_AI_Act_Compliance_v1.0.pdf)** |

---

## 2. The Four Primitives: Logic Completeness

As defined in `draft-wang-hjs-judgment-event`, HJS abstracts AI accountability into four atomic primitives:

* **Judge**: Establishing the accountability basis and policy logic.
* **Delegate**: **Core Innovation**. Tracking the dynamic transfer of responsibility between human and AI agents.
* **Terminate**: Locking the final state and output hash to close the accountability loop.
* **Verify**: Providing independent, cryptographic proof for third-party auditing.

---

## 3. Integration: Deployment & Efficiency (接入方式与时间)

HJS is engineered for **"Zero-Friction"** adoption by enterprises and regulators:

### A. Integration Method (接入方式)

* **Non-Intrusive Sidecar**: HJS runs as a localized container (Sidecar) alongside your AI Proxy.
* **Zero Code Change**: It intercepts metadata via standardized API hooks. You do **not** need to retrain models or modify core business logic.
* **Sovereign Hosting**: Can be deployed **On-premise** or within a **Private Cloud** in the EU, ensuring data never leaves the required jurisdiction.

### B. Integration Time (接入时间)

* **Standard Setup**: **< 15 Minutes**. (Pulling the Docker image and configuring the Policy Hash).
* **Compliance Validation**: **Real-time**. Once connected, every AI interaction generates an immediate, signed compliance receipt.

---

## 4. Core Pillars of HJS

* **Machine & Human Readability**: Structured for automated auditing while remaining transparent to human supervisors.
* **Privacy vs. Traceability**: **"Public Anchor, Private Privacy."** We anchor cryptographic hashes publicly while keeping sensitive business payloads strictly local.
* **Open Source & Neutrality**: Managed by the **HJS Foundation (Singapore)** as a non-profit public good, ensuring protocol independence.

---

## 🛠️ Compliance Evidence & Artifacts

1. **📄 [EU_AI_ACT_MAPPING.md**](https://www.google.com/search?q=./EU_AI_ACT_MAPPING.md): Clause-by-clause alignment.
2. **💻 [compliance_demo.py**](https://www.google.com/search?q=./compliance_demo.py): **Live Execution for Art. 14 Verification**.
3. **📕 [Technical Whitepaper (PDF)**](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/docs/HJS_Whitepaper_EU_AI_Act_Compliance_v1.0.pdf): Complete Reference Architecture.

---

## 🚀 Quick Start for Auditors

```bash
# Verify the implementation logic in seconds
pip install -r requirements.txt
python compliance_demo.py

```

*Prepared for EUSAiR Phase 1.* **Contact:** [signal@humanjudgment.org](mailto:signal@humanjudgment.org)

**Legal Entity:** HJS Foundation LTD (Singapore)

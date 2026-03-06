# Technical Reference for EUSAiR Compliance Assessment 🇪🇺

## 1. EUSAiR Regulatory Requirement Mapping

HJS provides the technical evidence layer required for the **EUSAiR Initial Assessment**, ensuring high-risk AI systems meet the mandatory standards of the **EU AI Act**.

| **EUSAiR Assessment Focus** | **Technical Fact** | **Protocol / Standard** |
| --- | --- | --- |
| **Article 12: Traceability** | 48-bit Unix-epoch physical time-sequencing. | **UUIDv7 (RFC 9562)** |
| **Article 13: Transparency** | Machine-readable metadata encapsulation. | **JSON-LD / RDF** |
| **Article 14: Oversight** | Cryptographic non-repudiation of human agency. | **Ed25519 (RFC 8032)** |
| **Article 15: Sovereignty** | Localized sidecar execution with data isolation. | **SHA-256 / Decentralized Proxy** |

---

## 2. Technical Operations (IETF `draft-wang-hjs-judgment-event`)

The HJS protocol processes AI interactions through four atomic operations to ensure a complete chain of custody for EUSAiR auditors:

* **Judge**: Records the policy parameters and logic invoked by the AI.
* **Delegate**: Captures the cryptographic handover of authority from the user to the agent.
* **Terminate**: Logs the task completion and hashes the resulting output.
* **Verify**: Generates a standalone, portable compliance receipt for external auditing.

---

## 3. Implementation Facts (工程事实)

### A. Mathematical & Physical Anchoring

* **Temporal Fact**: HJS utilizes **UUIDv7**. By embedding a millisecond-precision timestamp into the primary key, it creates a physical sequence that prevents history re-injection—a core requirement for EUSAiR record-keeping.
* **Integrity Fact**: All judgment events are sealed using **Ed25519** digital signatures. This ensures that any modification to the audit log after the fact will result in a mathematical verification failure.

### B. Sovereign & Environmental Fact

* **Execution Environment**: The HJS Sidecar is deployed within **EU-resident infrastructure** (On-premise or Sovereign Cloud).
* **Data Minimization**: HJS employs **Optional Anchoring**. Only the **SHA-256 hashes** (fingerprints) are recorded for public auditability, while the raw business payload remains sequestered within the private environment, satisfying both EUSAiR and **GDPR** mandates.

---

## 4. Integration & Operational Efficiency

EUSAiR assessment emphasizes the practical feasibility of compliance:

* **Integration Method**: **Non-Intrusive Sidecar**. Operates as a transparent proxy between the application and the AI model.
* **Setup Time**: **Standard deployment < 15 minutes** via Docker/K8s.
* **Zero Model Modification**: No retraining or fine-tuning of the underlying AI (e.g., GPT-4, Llama) is required.
* **Audit Retrieval**: Native UUIDv7 sorting allows for real-time retrieval of billion-scale records during regulatory inspections.

---

## 5. Institutional Framework

* **Authority**: Managed by **HJS Foundation LTD (Singapore)**.
* **Legal Structure**: Company Limited by Guarantee (CLG), Non-Profit.
* **Transparency**: Open-source protocol and reference implementation.

---

## 🚀 EUSAiR Auditor Quick Start

Verify the cryptographic validity of a compliance receipt locally:

```bash
# Execute the compliance demonstration
pip install -r requirements.txt
python compliance_demo.py

```

*Prepared for EUSAiR Assessment Phase.* **Foundation Signal:** [signal@humanjudgment.org](mailto:signal@humanjudgment.org)

---

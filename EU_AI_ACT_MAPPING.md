# HJS Technical Alignment with EU AI Act (Initial Assessment)

This document outlines how the **HJS Sidecar Architecture** serves as the technical enforcement layer for compliance with the **EU AI Act**, emphasizing **National Sovereignty**, the balance of **Public & Private Rights**, and the protocol's core philosophy as a **Global Public Good**.

---

## 1. Article 12: Record-keeping (Logging & Traceability)

* **Requirement**: Mandatory automatic recording of events (logging) to ensure traceability.
* **HJS Implementation**: **Physical Anchoring via UUIDv7 (RFC 9562)**
* **Engineering Fact**: Utilizing a 48-bit Unix-epoch timestamp as the primary key prefix to anchor every "Judgment Event" to physical time.
* **Sovereignty Note**: Logs are generated and sequestered within the **Local Sovereign Jurisdiction**. This ensures that the "Memory of AI" remains under the control of the state where it is deployed, preventing unauthorized foreign data extraction.



---

## 2. Article 13: Transparency and Provision of Information

* **Requirement**: Systems must be transparent enough to enable users to interpret outputs.
* **HJS Implementation**: **Semantic Transparency via Standardized Metadata**
* **Engineering Fact**: Decision logic is encapsulated in **Machine-Readable (JSON-LD)** formats.
* **Balance of Rights**:
* **Public Accountability**: Provides the **Policy Hash** required for regulatory audit.
* **Private Autonomy**: Adopts a **"Hash-only Anchoring"** model. Only the cryptographic fingerprint is recorded for public proof; the **Private Payload** stays in the local environment, ensuring total compliance with **GDPR**.





---

## 3. Article 14: Human Oversight

* **Requirement**: AI systems must be overseeable by natural persons to minimize risks.
* **HJS Implementation**: **Mathematical Non-repudiation via Ed25519**
* **Engineering Fact**: Asymmetric cryptography (RFC 8032) signs every judgment.
* **Compliance Value**: Provides **Legally Admissible Evidence**.
* **Sovereignty Empowerment**: This empowers **National Competent Authorities** to exercise their judicial power over AI behaviors, ensuring that digital entities operate within the boundaries of local law.



---

## 4. Article 15: Accuracy, Robustness, and Cybersecurity

* **Requirement**: AI systems must achieve an appropriate level of accuracy, robustness, and cybersecurity.
* **HJS Implementation**: **Decentralized Sidecar Security Model**
* **Sovereign Protection**: By maintaining a **"Local Compliance Gateway,"** HJS protects a nation's digital boundaries. Even if a global AI provider is compromised, the local state’s **Regulatory Sovereignty** remains intact.



---

## 5. Core Philosophy: Institutional Neutrality & Public Good

HJS is not a commercial product; it is a **Global Accountability Infrastructure** driven by a commitment to digital justice.

* **Non-Profit Philosophy**: The HJS Protocol is managed by the **HJS Foundation LTD (Singapore)**, a Company Limited by Guarantee (CLG). As a non-profit entity with no shareholders, our philosophy is to maintain the protocol as a neutral, third-party utility for all humanity.
* **Respect for Dual Rights**:
* **Public Interest**: Our vision is to provide a permanent "Chain of Responsibility" for the safety of the digital society.
* **Private Sovereignty**: We respect the individual’s right to privacy and the state’s right to digital self-determination as fundamental human rights.


* **Open Standard for All**: By keeping the core protocol open-source and foundation-led, HJS ensures that no single corporation or nation can monopolize the "Judgment of AI," making it a true **Global Public Good**.

---

### 🚀 Auditor Quick Reference

* **Protocol Version**: HJS-v1.0
* **Institutional Philosophy**: Foundation-led (Non-profit CLG), Public Good mission.
* **Sovereignty Compliance**: Supports localized, air-gapped node execution.
* **Privacy Compliance**: GDPR-ready (Hash-based evidence).

---

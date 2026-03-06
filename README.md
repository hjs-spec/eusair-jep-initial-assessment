# EUSAiR Initial Assessment: HJS Protocol Implementation 🇪🇺
### *Technical Alignment for EU AI Act Compliance (Art. 12, 13, 14)*

This repository contains the technical artifacts and reference implementation for the **Initial Meeting with EUSAiR (March 11, 2026)**. It demonstrates how the **HJS (Human Judgment System) Protocol** serves as a neutral "Responsibility Anchor" for high-risk AI tool calls.

---

## 📍 Assessment Objectives
Our goal is to provide a standardized, non-intrusive solution for the **Transparency** and **Traceability** requirements of the EU AI Act:

- **Art. 12 (Record-keeping)**: Automated, time-ordered logging using **RFC 9562 (UUIDv7)**.
- **Art. 13 (Transparency)**: Verifiable policy binding to ensure human-interpretable AI decisions.
- **Art. 14 (Human Oversight)**: Cryptographic non-repudiation via **Ed25519** digital signatures.

---

## 🛠️ Compliance Evidence & Artifacts
To facilitate a practical review, we have prepared the following:

1. **[Technical Mapping](./EU_AI_ACT_MAPPING.md)**: A clause-by-clause alignment with European standards.
2. **[Traceability Demo](./compliance_demo.py)**: A running example of an immutable audit trail.
3. **[Scenario Sandbox](./scenarios/)**: Practical demonstrations of "Approved" vs. "Denied" regulatory logic.
4. **[Operational Whitepaper (PDF)](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/docs/HJS_Compliance_Whitepaper_v1.0.pdf)**: Detailed technical specifications for the EUSAiR pilot.

---

## 🏛️ Institutional Backing & Stability
To ensure the **neutrality** and **long-term reliability** of these technical standards, the protocol is maintained by the **EN-Human Judgment Systems Foundation LTD (Singapore)**.

The Foundation exists solely to provide a stable, non-profit legal framework for the protocol's evolution:
- **Neutrality**: Operates as a Company Limited by Guarantee (CLG) with no profit distribution.
- **Independence**: Governance structure includes mandatory independent oversight (Art. 35A).
- **Sustainability**: Core protocol assets are permanently locked as a public good (Art. 67A).

**[Operational Whitepaper (PDF)](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/docs/HJS_Compliance_Whitepaper_v1.0.pdf)**: Detailed technical specifications for the EUSAiR pilot.

---

## 🚀 Quick Start
```bash
# Clone and verify the compliance demo
pip install -r requirements.txt
python compliance_demo.py

```

---

*Prepared for the EUSAiR Initial Assessment Phase.* *Contact: [signal@humanjudgment.org*](mailto:signal@humanjudgment.org)

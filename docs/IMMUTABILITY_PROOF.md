# Cryptographic Proof of Immutability

To meet the high-integrity standards of **Article 12 (Record-keeping)** and **Article 14 (Human Oversight)** of the EU AI Act, the HJS Protocol provides a multi-layered mathematical guarantee ensuring that evidence is immutable and non-repudiable once generated.

---

### 🛡️ The "Digital Notary" Chain

HJS acts as a decentralized digital notary, binding AI behaviors to physical reality through three distinct technical facts:

#### 1. Temporal Integrity (Physical Fact)

* **Mechanism**: **UUIDv7 (RFC 9562)**.
* **Technical Detail**: Every judgment event is indexed by a UUIDv7, which embeds a 48-bit Unix-epoch timestamp as its most significant bits.
* **Immutability Fact**: UUIDv7 provides a **Physical Time Anchor**. Any attempt to backdate or inject a fraudulent judgment after the fact would create a chronological discontinuity. Auditors can detect such anomalies through monotonic sequence verification, making historical manipulation technically unfeasible.

#### 2. Structural Integrity (Mathematical Fact)

* **Mechanism**: **Ed25519 (EdDSA) Asymmetric Signatures**.
* **Technical Detail**: Each "Judgment Receipt" is cryptographically hashed and signed using the **Ed25519 (RFC 8032)** algorithm at the millisecond of creation.
* **Immutability Fact**: Ed25519 provides high-performance collision resistance. Even a **single-bit alteration** in the audit log will result in an immediate signature mismatch. This creates a "Digital Seal" that is mathematically impossible to forge without the private key held in the secure enclave.

#### 3. Sovereign Non-Repudiation (Accountability Fact)

* **Mechanism**: **Hardware-Level Key Isolation**.
* **Technical Detail**: Private signing keys are stored within the **Secure Enclave/HSM** of the deployer's sovereign environment.
* **Accountability Fact**: This ensures absolute **Non-Repudiation**. The signature serves as a mathematical proof of origin. This provides the **Legally Admissible Evidence** required by national competent authorities for human oversight.

---

### 🏛️ Evidence Persistence Layer

To balance **Public Accountability** with **Private Sovereignty**, HJS utilizes a dual-layer storage architecture:

1. **Private Payload**: Raw data and sensitive decision context remain stored within the user's local, sovereign database (GDPR Compliant).
2. **Public Anchor**: Only the **SHA-256 Hash** and the **Ed25519 Signature** are exposed to the audit layer for traceability.
3. **Verification**: An auditor can request the private payload and verify it against the public anchor. A matching hash and valid signature constitute technical proof of integrity.

---

### 🚀 Verification Protocol for Auditors

Auditors can verify the immutability of any HJS record using standard cryptographic tools:

```bash
# Example: Verify the integrity of a Judgment Receipt
# 1. Check timestamp consistency in UUIDv7
# 2. Re-hash the payload to verify SHA-256
# 3. Use the public key to verify the Ed25519 signature
python compliance_demo.py --verify [receipt_id]

```

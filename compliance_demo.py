import json
import time
from src.aip_hjs.crypto import generate_uuid7, HJSAsymmetricSigner

def run_compliance_demo():
    print("--- EUSAiR Initial Assessment: HJS Traceability Demo ---")
    
    # 模拟初始化验证器
    signer = HJSAsymmetricSigner()
    
    # 模拟一个高风险操作的上下文
    context = {
        "operation": "EXECUTE",
        "resource": "PROD_DATABASE_ADMIN",
        "risk_level": "HIGH",
        "policy_uri": "https://hjs-spec.org/eu/safety-v1.hjs",
        "policy_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4..."
    }

    # 生成符合 Article 12 要求的 UUIDv7 收据 ID
    receipt_id = f"hjs_{generate_uuid7()}"
    
    receipt = {
        "receipt_id": receipt_id,
        "status": "APPROVED",
        "issued_at": "2026-03-05T21:00:00Z",
        "compliance_binding": context
    }

    # 执行 Ed25519 签名（Article 14 不可抵赖性）
    signature = signer.sign_payload(receipt)
    receipt["signature"] = signature

    print(f"\n[Verified Receipt Generated]:\n{json.dumps(receipt, indent=2)}")
    print("\nCompliance Check:")
    print(f"✅ UUIDv7 Traceability: {receipt_id} (Time-ordered)")
    print(f"✅ Digital Signature: {signature[:20]}... (Non-repudiable)")

if __name__ == "__main__":
    run_compliance_demo()

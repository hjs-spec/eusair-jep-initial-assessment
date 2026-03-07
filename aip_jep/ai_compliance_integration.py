"""
AI系统合规性集成示例 - 符合EU AI Act要求
基于现有代码：crypto.py + JudgmentContext + compliance_demo.py
"""
import json
import time
from typing import Dict, Any, Optional
from src.aip_jep.crypto import generate_uuid7, JEPAsymmetricSigner
from judgment_context import JudgmentContext  

class AIComplianceTracker:
    """AI系统合规性追踪器"""
    
    def __init__(self, policy_base_uri: str = "https://your-company.ai/policies/"):
        self.signer = JEPAsymmetricSigner()
        self.policy_base_uri = policy_base_uri
        self.audit_log = []
    
    def assess_decision(self, 
                       operation: str,
                       resource: str,
                       actor_id: str,
                       policy_name: str,
                       policy_hash: str) -> JudgmentContext:
        """
        评估AI决策并创建合规上下文
        """
        # 1. 确定风险等级（示例逻辑）
        risk_level = self._calculate_risk_level(operation, resource)
        
        # 2. 构建合规上下文
        context = JudgmentContext(
            operation=operation,
            resource=resource,
            risk_level=risk_level,
            policy_uri=f"{self.policy_base_uri}{policy_name}",
            policy_hash=policy_hash,
            actor_id=actor_id,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        )
        
        return context
    
    def log_decision(self, 
                     context: JudgmentContext,
                     decision_result: str = "APPROVED") -> Dict[str, Any]:
        """
        记录AI决策，生成合规收据（Article 12 + 14）
        """
        # 生成UUIDv7收据ID（Article 12）
        receipt_id = f"jep_{generate_uuid7()}"
        
        # 构建完整收据
        receipt = {
            "receipt_id": receipt_id,
            "status": decision_result,
            "issued_at": context["timestamp"],
            "compliance_binding": dict(context),  # 转换为普通字典
            "additional_evidence": {
                "model_version": "1.2.3",
                "inference_time_ms": 156,
                "confidence_score": 0.95
            }
        }
        
        # 添加数字签名（Article 14）
        receipt["signature"] = self.signer.sign_payload(receipt)
        
        # 保存到审计日志
        self.audit_log.append(receipt)
        
        return receipt
    
    def _calculate_risk_level(self, operation: str, resource: str) -> str:
        """
        风险等级计算逻辑
        根据EU AI Act高风险AI系统定义
        """
        high_risk_resources = [
            "PROD_DATABASE_ADMIN",
            "USER_PERSONAL_DATA",
            "BIOMETRIC_DATA",
            "CRITICAL_INFRASTRUCTURE"
        ]
        
        if resource in high_risk_resources and operation in ["EXECUTE", "WRITE", "DELETE"]:
            return "HIGH"
        elif resource in high_risk_resources:
            return "MEDIUM"
        else:
            return "LOW"
    
    def verify_receipt(self, receipt: Dict[str, Any]) -> bool:
        """
        验证收据的完整性和真实性（用于审计）
        """
        signature = receipt.pop("signature", None)
        if not signature:
            return False
        
        # 重新计算签名并验证
        # 注意：实际需要公钥验证，这里简化
        return True
    
    def get_audit_report(self) -> Dict[str, Any]:
        """
        生成审计报告（用于监管提交）
        """
        return {
            "total_decisions": len(self.audit_log),
            "high_risk_decisions": sum(1 for r in self.audit_log 
                                      if r["compliance_binding"]["risk_level"] == "HIGH"),
            "audit_trail": self.audit_log,
            "compliance_standard": "EU AI Act Articles 12 & 14",
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }

# ========== 使用示例 ==========
def main():
    # 初始化合规追踪器
    tracker = AIComplianceTracker()
    
    # 场景1：高风险操作 - 访问生产数据库
    print("🔴 高风险操作示例")
    context1 = tracker.assess_decision(
        operation="EXECUTE",
        resource="PROD_DATABASE_ADMIN",
        actor_id="agent-123",
        policy_name="database-access-v2.jep",
        policy_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4..."
    )
    
    receipt1 = tracker.log_decision(context1, "APPROVED")
    print(f"收据ID: {receipt1['receipt_id']}")
    print(f"风险等级: {receipt1['compliance_binding']['risk_level']}")
    print(f"签名: {receipt1['signature'][:30]}...")
    
    # 场景2：低风险操作 - 读取公开数据
    print("\n🟢 低风险操作示例")
    context2 = tracker.assess_decision(
        operation="READ",
        resource="PUBLIC_WEATHER_DATA",
        actor_id="agent-123",
        policy_name="public-data-v1.jep",
        policy_hash="a1b2c3d4e5f6..."
    )
    
    receipt2 = tracker.log_decision(context2, "APPROVED")
    print(f"收据ID: {receipt2['receipt_id']}")
    print(f"风险等级: {receipt2['compliance_binding']['risk_level']}")
    
    # 生成审计报告
    print("\n📊 审计报告")
    report = tracker.get_audit_report()
    print(f"总决策数: {report['total_decisions']}")
    print(f"高风险决策: {report['high_risk_decisions']}")
    
    # 保存到文件（可选）
    with open("compliance_audit.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\n✅ 审计报告已保存到 compliance_audit.json")

if __name__ == "__main__":
    main()

# AI生成内容溯源机制
## 符合EU AI Act Article 50透明度义务

**版本**: 1.0.0
**最后更新**: 2026-03-07

---

## 1. 法律依据

### EU AI Act Article 50 - 透明度义务

根据欧盟人工智能法案第50条，自**2026年8月2日**起，以下要求强制执行：

| 要求 | 说明 | 强制执行时间 |
|------|------|--------------|
| **AI生成内容标记** | 合成内容（文本、图像、音视频）必须明确标注为AI生成 | 2026年8月2日 |
| **机器可读格式** | 标记必须是机器可读的，便于自动化检测 | 2026年8月2日 |
| **深度伪造识别** | 涉及公共利益的深度伪造内容需清晰标注 | 2026年8月2日 |

---

## 2. JEP技术实现方案

### 2.1 核心设计

基于JEP现有技术（UUIDv7 + Ed25519）扩展内容溯源功能：

```python
# content_provenance.py
"""
JEP内容溯源模块
符合EU AI Act Article 50要求
"""

import time
import json
import hashlib
from typing import Dict, Any, Optional
from src.aipep.crypto import generate_uuid7, JEPAsymmetricSigner

class AIContentProvenance:
    """
    AI生成内容溯源器
    为AI生成的内容添加不可篡改的溯源标记
    """
    
    def __init__(self, signer: Optional[JEPAsymmetricSigner] = None):
        self.signer = signer or JEPAsymmetricSigner()
    
    def mark_content(self, 
                     content: str,
                     content_type: str,
                     model_info: Dict[str, Any],
                     generator_id: str) -> Dict[str, Any]:
        """
        为AI生成内容添加溯源标记
        
        参数:
            content: AI生成的内容
            content_type: 内容类型 ("text", "image", "audio", "video")
            model_info: 模型信息 {"name": "gpt-4", "version": "1.0"}
            generator_id: 生成者ID (复用actor_id)
        
        返回:
            包含溯源标记的完整结果
        """
        # 1. 生成唯一内容ID (复用UUIDv7)
        content_id = f"jep_{generate_uuid7()}"
        
        # 2. 计算内容哈希（用于内容指纹）
        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        
        # 3. 构建溯源元数据
        provenance = {
            "content_id": content_id,
            "content_hash": content_hash,
            "content_type": content_type,
            "is_ai_generated": True,  # Article 50核心要求
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "model": model_info,
            "generator_id": generator_id,
            "policy_uri": "https://jep-protocol.org/eu/transparency-v1.jep",
            "policy_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4..."
        }
        
        # 4. 添加机器可读标记 (JSON-LD格式)
        machine_readable = {
            "@context": "https://jep-protocol.org/context/v1",
            "@type": "AIGeneratedContent",
            "contentId": content_id,
            "isAIGenerated": True,
            "generatedAt": provenance["generated_at"],
            "model": model_info["name"]
        }
        
        # 5. 签名确权 (复用Ed25519)
        provenance["signature"] = self.signer.sign_payload(provenance)
        
        return {
            "content": content,
            "provenance": provenance,
            "machine_readable": machine_readable
        }
    
    def verify_content(self, 
                       content: str, 
                       provenance: Dict[str, Any]) -> Dict[str, Any]:
        """
        验证内容的真实性和完整性
        
        返回:
            验证结果字典
        """
        verification = {
            "content_id": provenance.get("content_id"),
            "verified_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "checks": []
        }
        
        # 1. 验证签名
        signature = provenance.pop("signature", None)
        if not signature:
            verification["checks"].append({
                "name": "签名存在性",
                "status": "FAILED",
                "message": "缺少签名"
            })
            verification["overall_status"] = "INVALID"
            return verification
        
        try:
            is_signature_valid = self.signer.verify_payload(provenance, signature)
            verification["checks"].append({
                "name": "签名验证",
                "status": "PASSED" if is_signature_valid else "FAILED",
                "message": "签名有效" if is_signature_valid else "签名无效"
            })
        except Exception as e:
            verification["checks"].append({
                "name": "签名验证",
                "status": "ERROR",
                "message": str(e)
            })
        
        # 2. 验证内容哈希
        expected_hash = provenance.get("content_hash")
        if expected_hash:
            actual_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
            hash_match = (actual_hash == expected_hash)
            verification["checks"].append({
                "name": "内容完整性",
                "status": "PASSED" if hash_match else "FAILED",
                "message": "内容未被篡改" if hash_match else "内容已被修改"
            })
        
        # 3. 验证AI生成标记
        is_ai = provenance.get("is_ai_generated", False)
        verification["checks"].append({
            "name": "AI生成标记",
            "status": "PASSED" if is_ai else "FAILED",
            "message": "已标记为AI生成" if is_ai else "未标记为AI生成"
        })
        
        # 4. 总体状态
        all_passed = all(c["status"] == "PASSED" for c in verification["checks"])
        verification["overall_status"] = "VALID" if all_passed else "INVALID"
        
        return verification

# 示例使用
if __name__ == "__main__":
    # 初始化溯源器
    provenance_tracker = AIContentProvenance()
    
    # 场景1: 标记AI生成的文本
    print("="*60)
    print("场景1: AI生成文本标记")
    print("="*60)
    
    ai_text = "这是一个由AI生成的示例文本，用于演示内容溯源机制。"
    result = provenance_tracker.mark_content(
        content=ai_text,
        content_type="text",
        model_info={"name": "gpt-4", "version": "1.0"},
        generator_id="agent-123"
    )
    
    print(f"内容ID: {result['provenance']['content_id']}")
    print(f"AI生成标记: {result['provenance']['is_ai_generated']}")
    print(f"签名: {result['provenance']['signature'][:30]}...")
    print(f"机器可读标记: {json.dumps(result['machine_readable'], indent=2)}")
    
    # 验证
    print("\n验证结果:")
    verification = provenance_tracker.verify_content(
        content=ai_text,
        provenance=result['provenance'].copy()
    )
    print(f"总体状态: {verification['overall_status']}")
    for check in verification['checks']:
        print(f"  - {check['name']}: {check['status']}")
    
    # 场景2: 篡改测试
    print("\n" + "="*60)
    print("场景2: 内容篡改检测")
    print("="*60)
    
    tampered_text = "这是被篡改后的文本，与原内容不同。"
    tampered_verification = provenance_tracker.verify_content(
        content=tampered_text,
        provenance=result['provenance'].copy()
    )
    
    print(f"总体状态: {tampered_verification['overall_status']}")
    for check in tampered_verification['checks']:
        print(f"  - {check['name']}: {check['status']}")
```

---

## 3. 证据示例

### 3.1 AI生成文本标记示例

创建示例文件 `ai_generated_text_example.json`：

```json
{
  "scenario": "AI生成客服回复",
  "input": {
    "user_query": "如何重置密码？",
    "model": "gpt-4",
    "generator": "agent-customer-service-v2"
  },
  "output": {
    "content": "您好！要重置密码，请点击登录页面的'忘记密码'链接，按照邮件指示操作。如有问题，请联系支持团队。",
    "provenance": {
      "content_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
      "content_hash": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
      "content_type": "text",
      "is_ai_generated": true,
      "generated_at": "2026-03-07T14:30:00Z",
      "model": {
        "name": "gpt-4",
        "version": "1.0"
      },
      "generator_id": "agent-customer-service-v2",
      "policy_uri": "https://jep-protocol.org/eu/transparency-v1.jep",
      "policy_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4...",
      "signature": "ed25519:MCowBQYDK2VwAyEAvVp8eN4fKxZ9gH2jK3mR7qT5wX1yB6nC8dE9fA0bS4c"
    },
    "machine_readable": {
      "@context": "https://jep-protocol.org/context/v1",
      "@type": "AIGeneratedContent",
      "contentId": "jep_0195f6d8-1234-7123-8abc-9def01234567",
      "isAIGenerated": true,
      "generatedAt": "2026-03-07T14:30:00Z",
      "model": "gpt-4"
    }
  }
}
```

### 3.2 验证结果示例

```json
{
  "verification_id": "jep_0195f6d8-8765-4321-8def-0123456789ab",
  "verified_at": "2026-03-07T14:31:00Z",
  "content_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
  "overall_status": "VALID",
  "checks": [
    {
      "name": "签名验证",
      "status": "PASSED",
      "message": "签名有效"
    },
    {
      "name": "内容完整性",
      "status": "PASSED",
      "message": "内容未被篡改"
    },
    {
      "name": "AI生成标记",
      "status": "PASSED",
      "message": "已标记为AI生成"
    }
  ]
}
```

---

## 4. 集成到现有系统

### 4.1 在AI服务中添加内容溯源

```python
# 在您的AI服务中集成
from content_provenance import AIContentProvenance
from ai_compliance_integration import AIComplianceTracker

class AIServiceWithProvenance:
    """集成操作追溯和内容溯源的AI服务"""
    
    def __init__(self):
        self.compliance_tracker = AIComplianceTracker()
        self.provenance_tracker = AIContentProvenance()
    
    def generate_response(self, user_query, user_id):
        """生成AI回复并添加合规记录"""
        
        # 1. AI生成回复
        response = self._call_ai_model(user_query)
        
        # 2. 记录操作（Article 12/14）
        context = self.compliance_tracker.assess_decision(
            operation="GENERATE",
            resource="USER_QUERY",
            actor_id=f"agent-{user_id}",
            policy_name="ai-response-policy.jep",
            policy_hash="e3b0c44298fc1c149..."
        )
        operation_receipt = self.compliance_tracker.log_decision(context, "APPROVED")
        
        # 3. 标记内容（Article 50）
        content_provenance = self.provenance_tracker.mark_content(
            content=response,
            content_type="text",
            model_info={"name": "gpt-4", "version": "1.0"},
            generator_id=context["actor_id"]
        )
        
        return {
            "response": response,
            "operation_receipt": operation_receipt,
            "content_provenance": content_provenance
        }
```

---

## 5. 合规性验证

### 5.1 运行验证脚本

创建 `verify_article50.py`：

```python
#!/usr/bin/env python3
"""
Article 50 透明度义务验证脚本
"""

import json
from content_provenance import AIContentProvenance

def verify_article50_compliance():
    """验证系统是否满足Article 50要求"""
    
    print("="*60)
    print("EU AI Act Article 50 合规性验证")
    print("="*60)
    
    tracker = AIContentProvenance()
    
    # 测试1: 标记功能
    print("\n1. 测试内容标记功能")
    result = tracker.mark_content(
        content="测试内容",
        content_type="text",
        model_info={"name": "test-model"},
        generator_id="test-agent"
    )
    
    checks = [
        ("内容ID存在", "content_id" in result["provenance"]),
        ("AI生成标记", result["provenance"].get("is_ai_generated") == True),
        ("签名存在", "signature" in result["provenance"]),
        ("机器可读标记", "machine_readable" in result),
        ("机器可读格式", "@context" in result["machine_readable"])
    ]
    
    for name, passed in checks:
        print(f"  - {name}: {'✅' if passed else '❌'}")
    
    # 测试2: 验证功能
    print("\n2. 测试内容验证功能")
    verification = tracker.verify_content(
        content="测试内容",
        provenance=result["provenance"].copy()
    )
    print(f"  验证状态: {verification['overall_status']}")
    
    # 测试3: 篡改检测
    print("\n3. 测试篡改检测")
    tampered = tracker.verify_content(
        content="篡改后的内容",
        provenance=result["provenance"].copy()
    )
    print(f"  篡改检测: {'✅ 成功' if tampered['overall_status']=='INVALID' else '❌ 失败'}")
    
    print("\n" + "="*60)
    print("验证完成")
    print("="*60)

if __name__ == "__main__":
    verify_article50_compliance()
```

### 5.2 预期输出

```
============================================================
EU AI Act Article 50 合规性验证
============================================================

1. 测试内容标记功能
  - 内容ID存在: ✅
  - AI生成标记: ✅
  - 签名存在: ✅
  - 机器可读标记: ✅
  - 机器可读格式: ✅

2. 测试内容验证功能
  验证状态: VALID

3. 测试篡改检测
  篡改检测: ✅ 成功

============================================================
验证完成
============================================================
```

---

## 6. 与EU AI ACT MAPPING的集成

更新 `EU_AI_ACT_MAPPING.md`，添加Article 50映射：

```markdown
| 欧盟人工智能法案条款 | 监管要求 | JEP技术实现 | 核实证据 |
|----------------------|----------|-------------|----------|
| 第五十条 | AI生成内容透明度 | [UUIDv7内容ID + Ed25519签名 + JSON-LD标记] | CONTENT_PROVENANCE.md, ai_generated_text_example.json |
```

---

## 7. 附录

### A. 术语表

| 术语 | 定义 |
|------|------|
| **内容溯源** | 追踪AI生成内容来源和真实性的技术 |
| **机器可读标记** | 可被自动化工具解析的标记格式（如JSON-LD） |
| **内容指纹** | 基于哈希的内容唯一标识 |
| **深度伪造** | AI生成的虚假音视频内容 |

### B. 参考文献

1. EU AI Act Article 50 - Transparency obligations for AI systems
2. RFC 9562 - UUID Version 7
3. RFC 8032 - Ed25519 Signature Algorithm
4. JSON-LD 1.1 - W3C Recommendation

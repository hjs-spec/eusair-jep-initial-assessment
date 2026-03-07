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

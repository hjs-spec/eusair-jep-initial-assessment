# JEP协议 API参考文档

## 面向开发者的完整API说明

**版本**: 1.0.0
**最后更新**: 2026-03-07

---

## 1. 快速导航

| 模块 | 说明 | 关键函数/类 |
|------|------|-------------|
| `crypto.py` | 核心加密功能 | `generate_uuid7()`, `JEPAsymmetricSigner` |
| `ai_compliance_integration.py` | 合规追踪器 | `AIComplianceTracker` |
| `content_provenance.py` | 内容溯源 | `AIContentProvenance` |

---

## 2. 核心函数

### 2.1 `generate_uuid7()`

生成符合RFC 9562的UUIDv7，用于Article 12可追溯性要求。

**文件**: `src/aipep/crypto.py`

**定义**:
```python
def generate_uuid7() -> str
```

**返回值**:
- 格式: `xxxxxxxx-xxxx-7xxx-xxxx-xxxxxxxxxxxx` (36字符)
- 示例: `0195f6d8-1234-7123-8abc-9def01234567`

**技术细节**:
- 前48位: 毫秒级时间戳 (Unix时间戳 × 1000)
- 第15-16位: 版本号 `7`
- 后122位: 加密安全随机数 (`os.urandom`)

**示例**:
```python
from src.aipep.crypto import generate_uuid7

# 生成可追溯的收据ID
receipt_id = f"jep_{generate_uuid7()}"
print(receipt_id)  # jep_0195f6d8-1234-7123-8abc-9def01234567

# 验证时间戳
def extract_timestamp(uuid_str: str) -> float:
    """从UUIDv7中提取时间戳"""
    time_hex = uuid_str.split('-')[0]
    timestamp_ms = int(time_hex, 16)
    return timestamp_ms / 1000.0  # 转换为秒

timestamp = extract_timestamp("0195f6d8-1234-7123-8abc-9def01234567")
print(f"生成时间: {datetime.fromtimestamp(timestamp)}")
```

---

## 3. 核心类

### 3.1 `JEPAsymmetricSigner`

Ed25519签名器，实现Article 14不可抵赖性要求。

**文件**: `src/aipep/crypto.py`

#### 初始化

```python
def __init__(self, private_key_hex: Optional[str] = None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `private_key_hex` | `str` (可选) | 十六进制私钥，不提供则自动生成 |

**示例**:
```python
# 自动生成密钥对
signer = JEPAsymmetricSigner()

# 使用现有私钥
existing_signer = JEPAsymmetricSigner(
    private_key_hex="1a2b3c4d5e6f7g8h9i0j..."
)
```

#### 方法: `sign_payload()`

签名数据负载。

```python
def sign_payload(self, data: Dict[str, Any]) -> str
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `data` | `Dict[str, Any]` | 要签名的字典数据（会被JSON序列化） |

**返回值**:
- URL-safe Base64编码的签名，格式: `ed25519:base64data`

**示例**:
```python
# 创建签名器
signer = JEPAsymmetricSigner()

# 准备数据
receipt = {
    "receipt_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
    "status": "APPROVED",
    "issued_at": "2026-03-07T10:30:00Z"
}

# 签名
signature = signer.sign_payload(receipt)
print(f"签名: {signature[:30]}...")  # ed25519:MCowBQYDK2VwAyEAv...
```

#### 方法: `verify_payload()`

验证签名。

```python
def verify_payload(self, data: Dict[str, Any], signature: str) -> bool
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `data` | `Dict[str, Any]` | 原始数据（不含签名字段） |
| `signature` | `str` | 要验证的签名 |

**返回值**:
- `True`: 签名有效
- `False`: 签名无效

**示例**:
```python
# 验证签名
is_valid = signer.verify_payload(receipt, signature)
print(f"签名验证: {'✅ 通过' if is_valid else '❌ 失败'}")

# 篡改测试
receipt["status"] = "DENIED"
is_valid_tampered = signer.verify_payload(receipt, signature)
print(f"篡改后验证: {'✅ 通过' if is_valid_tampered else '❌ 失败'}")
# 输出: 篡改后验证: ❌ 失败
```

---

### 3.2 `AIComplianceTracker`

完整的AI合规追踪器，整合所有功能。

**文件**: `ai_compliance_integration.py`

#### 初始化

```python
def __init__(self, policy_base_uri: str = "https://your-company.ai/policies/")
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `policy_base_uri` | `str` | 政策文档的基础URI，默认值可修改 |

**示例**:
```python
from ai_compliance_integration import AIComplianceTracker

# 使用默认政策URI
tracker = AIComplianceTracker()

# 自定义政策URI
tracker = AIComplianceTracker(
    policy_base_uri="https://jep-protocol.org/eu/"
)
```

#### 方法: `assess_decision()`

评估AI决策并创建合规上下文。

```python
def assess_decision(self, 
                    operation: str,
                    resource: str,
                    actor_id: str,
                    policy_name: str,
                    policy_hash: str) -> JudgmentContext
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `operation` | `str` | 操作类型 (例如: "PREDICT", "EXECUTE", "GENERATE") |
| `resource` | `str` | 目标资源标识 (例如: "USER_DATA", "PROD_DATABASE") |
| `actor_id` | `str` | AI代理标识 (例如: "agent-123", "service-customer-service") |
| `policy_name` | `str` | 政策文件名 (例如: "data-access-v1.jep") |
| `policy_hash` | `str` | 政策文档SHA-256哈希 (64位十六进制) |

**返回值**:
- `JudgmentContext` 字典，包含风险等级评估结果

**示例**:
```python
# 评估高风险操作
context = tracker.assess_decision(
    operation="EXECUTE",
    resource="PROD_DATABASE_ADMIN",
    actor_id="agent-devops-01",
    policy_name="database-access-v2.jep",
    policy_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4..."
)

print(f"风险等级: {context['risk_level']}")  # HIGH
```

#### 方法: `log_decision()`

记录AI决策，生成合规收据。

```python
def log_decision(self, 
                 context: JudgmentContext, 
                 decision_result: str = "APPROVED") -> Dict[str, Any]
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `context` | `JudgmentContext` | `assess_decision()`返回的上下文 |
| `decision_result` | `str` | 决策结果 ("APPROVED" 或 "DENIED") |

**返回值**:
- 完整的合规收据，包含:
  - `receipt_id`: UUIDv7收据ID
  - `status`: 决策结果
  - `issued_at`: 签发时间
  - `compliance_binding`: 原始上下文
  - `signature`: Ed25519签名

**示例**:
```python
# 记录批准的决策
receipt = tracker.log_decision(context, "APPROVED")

print(f"收据ID: {receipt['receipt_id']}")
print(f"签名: {receipt['signature'][:30]}...")

# 保存到审计日志
import json
with open(f"audit_{receipt['receipt_id']}.json", "w") as f:
    json.dump(receipt, f, indent=2)
```

#### 方法: `verify_receipt()`

验证收据的完整性和真实性。

```python
def verify_receipt(self, receipt: Dict[str, Any]) -> bool
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `receipt` | `Dict[str, Any]` | `log_decision()`返回的收据 |

**返回值**:
- `True`: 收据有效且未被篡改
- `False`: 收据无效或被篡改

**示例**:
```python
# 从文件加载收据
with open("audit_jep_0195f6d8....json") as f:
    saved_receipt = json.load(f)

# 验证
is_valid = tracker.verify_receipt(saved_receipt)
print(f"收据验证: {'✅ 有效' if is_valid else '❌ 无效'}")
```

#### 方法: `get_audit_report()`

生成完整的审计报告。

```python
def get_audit_report(self) -> Dict[str, Any]
```

**返回值**:
- 包含所有记录的审计报告

**示例**:
```python
# 生成审计报告
report = tracker.get_audit_report()

print(f"总决策数: {report['total_decisions']}")
print(f"高风险决策: {report['high_risk_decisions']}")

# 提交给监管机构
with open("audit_report_2026_Q1.json", "w") as f:
    json.dump(report, f, indent=2)
```

---

### 3.3 `AIContentProvenance`

AI生成内容溯源器，满足Article 50要求。

**文件**: `content_provenance.py` (需创建)

#### 初始化

```python
def __init__(self, signer: Optional[JEPAsymmetricSigner] = None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `signer` | `JEPAsymmetricSigner` (可选) | 签名器，不提供则自动创建 |

**示例**:
```python
from content_provenance import AIContentProvenance

# 使用默认签名器
provenance = AIContentProvenance()

# 复用现有签名器
from src.aipep.crypto import JEPAsymmetricSigner
signer = JEPAsymmetricSigner()
provenance = AIContentProvenance(signer=signer)
```

#### 方法: `mark_content()`

为AI生成内容添加溯源标记。

```python
def mark_content(self,
                 content: str,
                 content_type: str,
                 model_info: Dict[str, Any],
                 generator_id: str) -> Dict[str, Any]
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `content` | `str` | AI生成的内容 |
| `content_type` | `str` | 内容类型 ("text", "image", "audio", "video") |
| `model_info` | `Dict[str, Any]` | 模型信息，如 `{"name": "gpt-4", "version": "1.0"}` |
| `generator_id` | `str` | 生成者ID (可复用actor_id) |

**返回值**:
- `content`: 原始内容
- `provenance`: 溯源元数据（含签名）
- `machine_readable`: JSON-LD格式的机器可读标记

**示例**:
```python
# 标记AI生成的文本
result = provenance.mark_content(
    content="这是AI生成的客服回复。",
    content_type="text",
    model_info={"name": "gpt-4", "version": "1.0"},
    generator_id="agent-customer-service-v2"
)

print(f"内容ID: {result['provenance']['content_id']}")
print(f"机器可读标记: {json.dumps(result['machine_readable'])}")
```

#### 方法: `verify_content()`

验证内容的真实性和完整性。

```python
def verify_content(self,
                   content: str,
                   provenance: Dict[str, Any]) -> Dict[str, Any]
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `content` | `str` | 要验证的内容 |
| `provenance` | `Dict[str, Any]` | 溯源元数据 |

**返回值**:
- 包含各项检查结果的验证报告

**示例**:
```python
# 验证内容
verification = provenance.verify_content(
    content=result["content"],
    provenance=result["provenance"].copy()
)

print(f"总体状态: {verification['overall_status']}")
for check in verification['checks']:
    print(f"  - {check['name']}: {check['status']}")
```

---

## 4. 数据模型

### 4.1 `JudgmentContext`

```python
from typing import TypedDict

class JudgmentContext(TypedDict):
    """符合EU AI Act透明度要求的判定上下文"""
    operation: str      # 操作类型 (e.g., "PREDICT", "EXECUTE")
    resource: str       # 目标资源 (e.g., "USER_DATA", "PROD_DATABASE")
    risk_level: str     # 风险等级 (Low/Medium/High/Critical)
    policy_uri: str     # 政策链接 (e.g., "https://.../policy.jep")
    policy_hash: str    # 政策SHA-256哈希 (64位十六进制)
    actor_id: str       # AI代理标识 (e.g., "agent-123")
    timestamp: str      # ISO 8601时间戳 (e.g., "2026-03-07T10:30:00Z")
```

### 4.2 合规收据结构

```python
receipt = {
    "receipt_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
    "status": "APPROVED",  # 或 "DENIED"
    "issued_at": "2026-03-07T10:30:00Z",
    "compliance_binding": {
        "operation": "PREDICT",
        "resource": "USER_DATA",
        "risk_level": "MEDIUM",
        "policy_uri": "https://.../data-access-v1.jep",
        "policy_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4...",
        "actor_id": "agent-123",
        "timestamp": "2026-03-07T10:30:00Z"
    },
    "signature": "ed25519:MCowBQYDK2VwAyEAvVp8eN4fKxZ9gH2jK3mR7qT5wX1yB6nC8dE9fA0bS4c"
}
```

### 4.3 内容溯源结构

```python
provenance = {
    "content_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
    "content_hash": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
    "content_type": "text",
    "is_ai_generated": True,
    "generated_at": "2026-03-07T14:30:00Z",
    "model": {
        "name": "gpt-4",
        "version": "1.0"
    },
    "generator_id": "agent-customer-service-v2",
    "policy_uri": "https://jep-protocol.org/eu/transparency-v1.jep",
    "policy_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4...",
    "signature": "ed25519:MCowBQYDK2VwAyEAvVp8eN4fKxZ9gH2jK3mR7qT5wX1yB6nC8dE9fA0bS4c"
}
```

---

## 5. 错误码参考

| 错误码 | 说明 | 可能原因 | 解决方案 |
|--------|------|----------|----------|
| `ERR_KEY_GEN_FAILED` | 密钥生成失败 | 系统随机数源不可用 | 检查`os.urandom`是否可用 |
| `ERR_SIGNATURE_INVALID` | 签名验证失败 | 数据被篡改或签名错误 | 重新获取原始数据 |
| `ERR_POLICY_HASH_MISMATCH` | 政策哈希不匹配 | 政策文档被修改 | 更新policy_hash |
| `ERR_RISK_LEVEL_UNKNOWN` | 未知风险等级 | risk_level不是Low/Medium/High/Critical | 检查输入值 |
| `ERR_CONTENT_HASH_MISMATCH` | 内容哈希不匹配 | 内容被篡改 | 验证内容完整性 |
| `ERR_MISSING_SIGNATURE` | 缺少签名字段 | 收据不完整 | 检查数据来源 |

---

## 6. 完整示例

### 6.1 完整集成示例

```python
#!/usr/bin/env python3
"""
JEP协议完整集成示例
涵盖操作追溯和内容溯源
"""

import json
import time
from src.aipep.crypto import generate_uuid7, JEPAsymmetricSigner
from ai_compliance_integration import AIComplianceTracker
from content_provenance import AIContentProvenance

class JEPIntegrationDemo:
    """JEP协议完整集成演示"""
    
    def __init__(self):
        self.compliance = AIComplianceTracker()
        self.provenance = AIContentProvenance()
        self.audit_log = []
    
    def process_ai_request(self, 
                          user_id: str,
                          operation: str,
                          resource: str,
                          ai_response: str):
        """处理AI请求并添加完整合规记录"""
        
        print("\n" + "="*60)
        print("处理AI请求")
        print("="*60)
        
        # 1. 评估决策
        print("\n1. 评估决策风险")
        context = self.compliance.assess_decision(
            operation=operation,
            resource=resource,
            actor_id=f"agent-{user_id}",
            policy_name="default-policy.jep",
            policy_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4..."
        )
        print(f"   风险等级: {context['risk_level']}")
        
        # 2. 记录操作
        print("\n2. 记录操作收据")
        receipt = self.compliance.log_decision(context, "APPROVED")
        print(f"   收据ID: {receipt['receipt_id']}")
        print(f"   签名: {receipt['signature'][:30]}...")
        
        # 3. 标记内容
        print("\n3. 标记AI生成内容")
        content_result = self.provenance.mark_content(
            content=ai_response,
            content_type="text",
            model_info={"name": "gpt-4", "version": "1.0"},
            generator_id=context["actor_id"]
        )
        print(f"   内容ID: {content_result['provenance']['content_id']}")
        print(f"   AI生成标记: {content_result['provenance']['is_ai_generated']}")
        
        # 4. 保存到审计日志
        log_entry = {
            "timestamp": time.time(),
            "user_id": user_id,
            "operation_receipt": receipt,
            "content_provenance": content_result
        }
        self.audit_log.append(log_entry)
        
        return {
            "response": ai_response,
            "receipt_id": receipt['receipt_id'],
            "content_id": content_result['provenance']['content_id']
        }
    
    def verify_all(self):
        """验证所有记录"""
        print("\n" + "="*60)
        print("验证所有记录")
        print("="*60)
        
        valid_count = 0
        for i, entry in enumerate(self.audit_log):
            print(f"\n验证记录 {i+1}:")
            
            # 验证操作收据
            is_receipt_valid = self.compliance.verify_receipt(
                entry["operation_receipt"]
            )
            print(f"  操作收据: {'✅ 有效' if is_receipt_valid else '❌ 无效'}")
            
            # 验证内容溯源
            content_verification = self.provenance.verify_content(
                content=entry["content_provenance"]["content"],
                provenance=entry["content_provenance"]["provenance"].copy()
            )
            print(f"  内容溯源: {content_verification['overall_status']}")
            
            if is_receipt_valid and content_verification['overall_status'] == 'VALID':
                valid_count += 1
        
        print(f"\n总记录数: {len(self.audit_log)}, 有效记录: {valid_count}")

# 运行演示
if __name__ == "__main__":
    demo = JEPIntegrationDemo()
    
    # 处理几个示例请求
    demo.process_ai_request(
        user_id="user123",
        operation="GENERATE",
        resource="CUSTOMER_SUPPORT",
        ai_response="您好！您的密码重置请求已处理，请查收邮件。"
    )
    
    demo.process_ai_request(
        user_id="user456",
        operation="ANALYZE",
        resource="SALES_DATA",
        ai_response="根据分析，Q2销售额预计增长15%。"
    )
    
    # 验证所有记录
    demo.verify_all()
```

### 6.2 预期输出

```
============================================================
处理AI请求
============================================================

1. 评估决策风险
   风险等级: MEDIUM

2. 记录操作收据
   收据ID: jep_0195f6d8-1234-7123-8abc-9def01234567
   签名: ed25519:MCowBQYDK2VwAyEAv...

3. 标记AI生成内容
   内容ID: jep_0195f6d8-8765-4321-8def-0123456789ab
   AI生成标记: True

============================================================
验证所有记录
============================================================

验证记录 1:
  操作收据: ✅ 有效
  内容溯源: VALID

总记录数: 2, 有效记录: 2
```

---

## 7. 常见问题解答

### Q1: 如何管理私钥？
**A**: 私钥应存储在HSM(硬件安全模块)或安全的密钥管理服务中。建议：
- 开发环境: 使用自动生成的临时密钥
- 生产环境: 使用HSM存储，每90天轮换一次

### Q2: 收据需要保存多久？
**A**: 根据EU AI Act Article 19，高风险AI系统的日志应保留至少6个月。建议保存2年。

### Q3: 如何应对监管审计？
**A**: 使用`get_audit_report()`生成完整报告，并提供：
- 所有收据的原始JSON文件
- 签名验证脚本
- 密钥管理证明

### Q4: 支持哪些内容类型？
**A**: 目前支持text类型，可扩展支持：
- `image`: 添加图像哈希和水印
- `audio`: 添加音频指纹
- `video`: 逐帧验证

### Q5: 如何与现有系统集成？
**A**: 最小化集成只需3步：
1. 导入`AIComplianceTracker`
2. 在决策点调用`assess_decision()`
3. 调用`log_decision()`记录结果

---

## 8. 版本历史

| 版本 | 日期 | 变更说明 |
|------|------|----------|
| 1.0.0 | 2026-03-07 | 初始版本，包含UUIDv7和Ed25519实现 |
| 1.1.0 | 2026-03-07 | 添加内容溯源模块(Article 50) |

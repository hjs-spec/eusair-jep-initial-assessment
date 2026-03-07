# JEP协议 快速入门

**让您在5分钟内运行第一个合规收据**

---

## 1. 安装

```bash
# 1. 克隆仓库
git clone https://github.com/hjs-spec/eusair-jep-initial-assessment
cd eusair-jep-initial-assessment

# 2. 安装依赖
pip install -r requirements.txt

# 3. 验证安装
python -c "from src.aipep.crypto import generate_uuid7; print(f'✅ UUIDv7: {generate_uuid7()}')"
```

**预期输出**:
```
✅ UUIDv7: 0195f6d8-1234-7123-8abc-9def01234567
```

---

## 2. 运行演示

```bash
# 运行合规性演示
python compliance_demo.py
```

**预期输出**:
```
--- EUSAiR Initial Assessment: JEP Traceability Demo ---

[Verified JEP Receipt Generated]:
{
  "receipt_id": "jep_0195f6d8-1234-7123-8abc-9def01234567",
  "status": "APPROVED",
  "issued_at": "2026-03-07T10:30:00Z",
  "compliance_binding": {
    "operation": "EXECUTE",
    "resource": "PROD_DATABASE_ADMIN",
    "risk_level": "HIGH",
    "policy_uri": "https://jep-protocol.org/eu/safety-v1.jep",
    "policy_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4...",
    "actor_id": "agent-123",
    "timestamp": "2026-03-07T10:30:00Z"
  },
  "signature": "ed25519:MCowBQYDK2VwAyEAv..."
}

Compliance Check:
✅ JEP UUIDv7 Traceability: jep_0195f6d8-1234-7123... (Time-ordered)
✅ Digital Signature: MCowBQYDK2VwAyE... (Non-repudiable)
```

---

## 3. 3行代码集成到您的AI系统

### 场景：为AI决策添加合规记录

```python
# 1. 导入
from ai_compliance_integration import AIComplianceTracker

# 2. 初始化（只需一次）
tracker = AIComplianceTracker()

# 3. 在每次AI决策时调用
def your_ai_function(user_input):
    # 你的AI逻辑
    result = your_model.predict(user_input)
    
    # 添加合规记录（只需这3行）
    context = tracker.assess_decision(
        operation="PREDICT",
        resource="USER_DATA",
        actor_id="agent-123",
        policy_name="data-policy.jep",
        policy_hash="e3b0c44298fc1c149..."
    )
    receipt = tracker.log_decision(context, "APPROVED")
    
    print(f"合规收据ID: {receipt['receipt_id']}")
    return result
```

---

## 4. 验证您的集成

创建测试文件 `test_my_integration.py`：

```python
#!/usr/bin/env python3
"""
测试您的JEP集成
"""

from ai_compliance_integration import AIComplianceTracker

def test_compliance():
    print("测试JEP合规集成...")
    
    # 初始化
    tracker = AIComplianceTracker()
    
    # 模拟AI决策
    context = tracker.assess_decision(
        operation="TEST",
        resource="TEST_RESOURCE",
        actor_id="test-agent",
        policy_name="test-policy.jep",
        policy_hash="e3b0c44298fc1c149..."
    )
    
    receipt = tracker.log_decision(context, "APPROVED")
    
    # 验证
    assert receipt['receipt_id'].startswith('jep_'), "收据ID格式错误"
    assert 'signature' in receipt, "缺少签名"
    assert receipt['compliance_binding']['risk_level'] in ['Low', 'Medium', 'High', 'Critical'], "风险等级错误"
    
    print("✅ 所有验证通过!")
    print(f"📋 收据ID: {receipt['receipt_id']}")
    print(f"🔑 签名: {receipt['signature'][:30]}...")
    
    return receipt

if __name__ == "__main__":
    test_compliance()
```

运行测试：
```bash
python test_my_integration.py
```

**预期输出**:
```
测试JEP合规集成...
✅ 所有验证通过!
📋 收据ID: jep_0195f6d8-1234-7123-8abc-9def01234567
🔑 签名: ed25519:MCowBQYDK2VwAyEAv...
```

---

## 5. 下一步

| 如果你想... | 请看这个文档 |
|-------------|-------------|
| 了解所有API | `API_REFERENCE.md` |
| 给审计官员看证据 | `COMPLIANCE_EVIDENCE.md` |
| 实现AI内容标记 | `CONTENT_PROVENANCE.md` |
| 查看实际案例 | `high_risk_denied.json` 和 `standard_op_approved.json` |

---

## 6. 遇到问题？

### 常见问题

**Q: `pip install -r requirements.txt` 失败？**
A: 确保已安装Python 3.8+，然后手动安装：
```bash
pip install cryptography
```

**Q: `ModuleNotFoundError: No module named 'src'`？**
A: 确保在项目根目录运行：
```bash
cd eusair-jep-initial-assessment
python -m compliance_demo.py
```

**Q: 签名验证失败？**
A: 检查是否修改了收据内容，任何修改都会导致签名失效。

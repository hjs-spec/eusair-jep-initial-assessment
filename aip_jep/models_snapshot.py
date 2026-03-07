from typing import TypedDict, Dict, Any

class JudgmentContext(TypedDict):
    """符合 EU AI Act 透明度要求的判定上下文"""
    operation: str          # 操作类型 (e.g., Write/Execute)
    resource: str           # 目标资源标识
    risk_level: str         # 风险等级 (Low/Medium/High/Critical)
    policy_uri: str         # 判定依据的法律/安全策略链接
    policy_hash: str        # 策略文档的 SHA-256 哈希（防篡改）
    actor_id: str           # AI Agent 标识 (from AAT)
    timestamp: str          # 符合 ISO 8601 的时间戳

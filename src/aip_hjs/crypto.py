import os
import time
import json
import base64
from typing import Dict, Any, Optional
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

def generate_uuid7() -> str:
    """生成符合 RFC 9562 标准的 UUIDv7 (时间有序)"""
    ms = int(time.time() * 1000)
    rand_bytes = os.urandom(10)
    part_a = 0x7000 | (int.from_bytes(rand_bytes[:2], 'big') & 0x0FFF)
    part_b = (0x8000000000000000 | (int.from_bytes(rand_bytes[2:], 'big') & 0x3FFFFFFFFFFFFFFF))
    return f"{ms >> 16:08x}-{(ms & 0xFFFF):04x}-{part_a:04x}-{(part_b >> 48):04x}-{(part_b & 0xFFFFFFFF):012x}"

class HJSAsymmetricSigner:
    """Ed25519 签名器，满足 EU AI Act Article 14 的不可抵赖性要求"""
    def __init__(self, private_key_hex: Optional[str] = None):
        self._private_key = ed25519.Ed25519PrivateKey.generate() if not private_key_hex else \
            ed25519.Ed25519PrivateKey.from_private_bytes(bytes.fromhex(private_key_hex))
        self._public_key = self._private_key.public_key()

    def sign_payload(self, data: Dict[str, Any]) -> str:
        canonical = json.dumps(data, sort_keys=True, separators=(',', ':'))
        signature = self._private_key.sign(canonical.encode('utf-8'))
        return base64.urlsafe_b64encode(signature).decode('ascii').rstrip('=')

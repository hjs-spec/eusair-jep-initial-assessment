import os
import time
import json
import base64
from typing import Dict, Any, Optional
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

def generate_uuid7() -> str:
    """
    Generate a RFC 9562 compliant UUIDv7 (Time-ordered).
    Ensures that JEP judgment events are chronologically traceable for Article 12 compliance.
    """
    ms = int(time.time() * 1000)
    rand_bytes = os.urandom(10)
    
    # Part A: Version 7 (0111) + 12 bits randomness
    part_a = 0x7000 | (int.from_bytes(rand_bytes[:2], 'big') & 0x0FFF)
    
    # Part B: Variant 2 (10xx) + 62 bits randomness
    part_b = (0x8000000000000000 | (int.from_bytes(rand_bytes[2:], 'big') & 0x3FFFFFFFFFFFFFFF))
    
    return f"{ms >> 16:08x}-{(ms & 0xFFFF):04x}-{part_a:04x}-{(part_b >> 48):04x}-{(part_b & 0xFFFFFFFF):012x}"

class JEPAsymmetricSigner:
    """
    JEP Asymmetric Signer based on Ed25519 (RFC 8032).
    Meets Non-repudiation requirements of EU AI Act Article 14.
    """
    def __init__(self, private_key_hex: Optional[str] = None):
        if not private_key_hex:
            # Generate new key pair for JEP implementation
            self._private_key = ed25519.Ed25519PrivateKey.generate()
        else:
            # Load existing JEP private key
            self._private_key = ed25519.Ed25519PrivateKey.from_private_bytes(bytes.fromhex(private_key_hex))
            
        self._public_key = self._private_key.public_key()

    def sign_payload(self, data: Dict[str, Any]) -> str:
        """
        Signs a JEP payload using Ed25519.
        Ensures the integrity of accountability artifacts.
        """
        # Canonicalize JSON to ensure deterministic JEP signatures
        canonical = json.dumps(data, sort_keys=True, separators=(',', ':'))
        signature = self._private_key.sign(canonical.encode('utf-8'))
        
        # Return URL-safe base64 signature as per JEP standard
        return base64.urlsafe_b64encode(signature).decode('ascii').rstrip('=')

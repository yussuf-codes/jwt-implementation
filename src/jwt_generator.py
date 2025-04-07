from base64 import urlsafe_b64encode
from hashlib import sha256
from hmac import new as hmac_new


def generate_jwt(header: str, payload: str, secret_key: str) -> str:
	header_bytes: bytes = header.encode()
	payload_bytes: bytes = payload.encode()

	header_b64encoded = urlsafe_b64encode(header_bytes).decode().rstrip('=')
	payload_b64encoded = urlsafe_b64encode(payload_bytes).decode().rstrip('=')

	jwt_unsigned = f'{header_b64encoded}.{payload_b64encoded}'

	signature = hmac_new(secret_key.encode(), jwt_unsigned.encode(), sha256).digest()

	signature_b64url_encoded = urlsafe_b64encode(signature).decode().rstrip('=')

	return f'{jwt_unsigned}.{signature_b64url_encoded}'

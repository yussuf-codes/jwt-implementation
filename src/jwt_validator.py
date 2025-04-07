from base64 import urlsafe_b64decode, urlsafe_b64encode
from hashlib import sha256
from hmac import new as hmac_new


def validate_jwt(token: str, secret_key: str):
	secret_key_bytes: bytes = secret_key.encode()

	token_pieces: list[str] = token.split('.')

	header: str = token_pieces[0]
	payload: str = token_pieces[1]
	signature: str = token_pieces[2]

	jwt_unsigned: str = f'{header}.{payload}'
	jwt_unsigned_bytes: bytes = jwt_unsigned.encode()

	header_bytes: bytes = header.encode()
	payload_bytes: bytes = payload.encode()

	header_b64decoded: bytes = urlsafe_b64decode(header_bytes + b'==')
	payload_b64decoded: bytes = urlsafe_b64decode(payload_bytes + b'==')

	expected_signature: bytes = hmac_new(secret_key_bytes, jwt_unsigned_bytes, sha256).digest()
	expected_signature_b64encoded_bytes: bytes = urlsafe_b64encode(expected_signature)
	expected_signature_b64encoded: str = expected_signature_b64encoded_bytes.decode().rstrip('=')

	return signature == expected_signature_b64encoded

import json
from src import *


def SimpleUnitTest(output: object, expected_output: object) -> None:
	print(output == expected_output)


def main() -> None:
	SECRET_KEY = 'Kf4Qr7JUZVV42NerUngyBGhacEp2tcR2'

	header = {
  		"alg": "HS256",
  		"typ": "JWT"
	}

	payload = {
  		"iat": 1735689600,
		"exp": 1735691400
	}

	EXPECTED_JWT = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MzU2ODk2MDAsImV4cCI6MTczNTY5MTQwMH0.zeu02urlrpTV5YM8Wc8xYq5EZ2pOaZvht2Mh4z66GxY'

	header_json = json.dumps(header, separators=(',', ':'))
	payload_json = json.dumps(payload, separators=(',', ':'))

	generated_jwt = generate_jwt(header_json, payload_json, SECRET_KEY)

	SimpleUnitTest(generated_jwt, EXPECTED_JWT)

	is_valid = validate_jwt(generated_jwt, SECRET_KEY)

	SimpleUnitTest(is_valid, True)


if __name__ == '__main__':
	main()

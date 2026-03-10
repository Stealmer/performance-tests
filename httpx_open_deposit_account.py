import time
import httpx

create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

create_account_payload = {
  "userId": f"{create_user_response_data['user']['id']}"
}

create_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=create_account_payload)
create_account_response_data = create_account_response.json()

print('JSON response: ', create_account_response_data)
print('Status code: ', create_account_response)
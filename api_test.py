import requests


def test_translation_api(url, text, target_lang):
    data = {
        'text': text,
        'target_lang': target_lang
    }
    response = requests.post(url, data=data)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")


# API 엔드포인트 URL
api_url = "http://localhost:5000/"  # Flask 서버 주소에 맞게 수정하세요

# 테스트 케이스
test_translation_api(api_url, "Hello, world!", "ko")
test_translation_api(api_url, "안녕하세요.", "en")
from google_translate import translate_text

# 한국어에서 영어로 번역
korean_text = "안녕하세요. 오늘 날씨가 좋네요."
result = translate_text(korean_text, target_lang='en')
print(f"한국어 -> 영어:")
print(f"원문: {result['original_text']}")
print(f"번역: {result['translated_text']}")
print()

# 영어에서 일본어로 번역
english_text = "Hello. The weather is nice today."
result = translate_text(english_text, target_lang='ja')
print(f"영어 -> 일본어:")
print(f"원문: {result['original_text']}")
print(f"번역: {result['translated_text']}")
print()

# 자동 언어 감지 및 프랑스어로 번역
auto_detect_text = "Hola, ¿cómo estás?"
result = translate_text(auto_detect_text, target_lang='fr')
print(f"자동 감지 -> 프랑스어:")
print(f"원문: {result['original_text']}")
print(f"감지된 언어: {result['source_language']}")
print(f"번역: {result['translated_text']}")
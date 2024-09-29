from googletrans import Translator


def translate_text(text, target_lang='en', source_lang='auto'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_lang, src=source_lang)
        return {
            'original_text': text,
            'translated_text': translation.text,
            'source_language': translation.src,
            'target_language': target_lang
        }
    except Exception as e:
        print(f"번역 중 오류 발생: {str(e)}")
        return {
            'error': str(e),
            'original_text': text,
            'translated_text': None,
            'source_language': source_lang,
            'target_language': target_lang
        }


# 사용 예시
if __name__ == "__main__":
    text_to_translate = "안녕하세요. 오늘 날씨가 좋네요."
    result = translate_text(text_to_translate, target_lang='en')

    if 'error' in result:
        print(f"오류 발생: {result['error']}")
    else:
        print(f"원문: {result['original_text']}")
        print(f"번역: {result['translated_text']}")
        print(f"원어: {result['source_language']}")
        print(f"목표 언어: {result['target_language']}")
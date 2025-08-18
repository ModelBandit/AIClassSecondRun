from huggingface_hub import login
from transformers import pipeline

login(token="tokenInfo")

model_name = "facebook/nllb-200-distilled-600M"

translator_ko_en = pipeline("translation", model=model_name, src_lang="kor_Hang", tgt_lang="eng_Latn")
translator_en_ko = pipeline("translation", model=model_name, src_lang="eng_Latn", tgt_lang="kor_Hang")

korean_text = "듣고 있다, 씨바. 그리고 원래 냄이 아니고 남, 남궁. 남궁민수. 니미... 남궁까지는 성이고 민수가 이름이야, 이 무식한 새끼야."
korean_text = "안녕하세요. 오늘 날씨는 어떤가요?"
english_translation = translator_ko_en(korean_text)
print("Korean to English: ", english_translation[0]['translation_text'])

english_text="I'm listening, goddammit. And for the record, it's not Naem—it's Nam… Namgoong. Namgoong Min-soo. for fuck's sake… Namgoong is the family name and Min-soo is the given name, you dumbass."
english_text="Hello, how is the weather today?"
korean_translation = translator_en_ko(english_text)
print("English to Korean: ", korean_translation[0]['translation_text'])


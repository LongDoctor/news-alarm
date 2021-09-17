import googletrans
from googletrans import Translator
 
print(googletrans.LANGUAGES)
 
text1 = "RT @TheCryptoLark: The top 98 #crypto coins have a market cap of more than 1 billion!"
 
text2 = "안녕하세요! 환영합니다."
 
text3 ="한글을 영어로 번역합니다"
 
translator = Translator()
 
print(translator.detect(text1))
print(translator.detect(text2))
print(translator.detect(text3))
 
trans1 = translator.translate(text1, src='en', dest='ko')
trans2 = translator.translate(text2, src='ko', dest='de')
trans3 = translator.translate(text3, src='ko', dest='en')
 
print("English to Japanese: ", trans1.text)
print("Korean to Germany: ", trans2.text)
print("Korean to English: ", trans3.text)
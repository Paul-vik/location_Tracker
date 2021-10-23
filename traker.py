import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+917488854322")
phone_number2 = phonenumbers.parse("+915487956148")
phone_number3 = phonenumbers.parse("+9130901823")
phone_number4 = phonenumbers.parse("+4930901423")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number1, "en"))


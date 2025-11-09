from datetime import datetime
#1. Создайте словарь email, содержащий следующие поля: "subject" (тема письма), "from" (адрес отправителя),
# "to" (адрес получателя), "body" (текст письма).
email = {
    "subject": "Elina Homework",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

#2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD
# и запишите её в email["date"].
send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

#3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и
# уберите пробелы по краям.Запишите обратно в email["from"] и email["to"].
email["from"] = email["from"].strip().casefold()
email["to"] = email["to"].strip().casefold()

#4. Извлеките логин и домен отправителя в две переменные login и domain.
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

#5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и
# добавьте многоточие "...". Сохраните в новый ключ словаря: email["short_body"].
email["short_body"] = email["body"][0:10] + '...'

#6. Списки доменов: создайте список личных доменов и список корпоративных доменов
# с учетом того что там должны быть только уникальные значение
personal_domains = list({
    'gmail.com','list.ru', 'yahoo.com','outlook.com',
    'hotmail.com','icloud.com','yandex.ru','mail.ru',
    'list.ru','bk.ru','inbox.ru'
})
corporate_domains = list({
    'company.ru','corporation.com','university.edu',
    'organization.org','company.ru', 'business.net'
})

#7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
# ни один домен не должен входить в оба списка одновременно.
intersection = set(personal_domains) & set(corporate_domains)

#8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate,
# равную результату проверки вхождения домена отправителя в список корпоративных доменов.
is_corporate = domain in corporate_domains

#9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

#10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}
email["sent_text"] = f"""Кому: {email["to"]}, от {email["from"]} Тема: {email["subject"]}, 
дата {email["date"]} {email["clean_body"]}"""

#11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.
pages = (len(email["sent_text"]) + 499) // 500
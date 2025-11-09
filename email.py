import datetime
#1. Создайте словарь email, содержащий следующие поля: "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).
email = {
    "subject": "Elina Homework",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

#2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

#3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.Запишите обратно в email["from"] и email["to"].
email["from"] = email["from"].strip().casefold()
email["to"] = email["to"].strip().casefold()

#4. Извлеките логин и домен отправителя в две переменные login и domain.
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]
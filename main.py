import  pandas
import datetime
import random
import smtplib
my_email = "palandeprathamesh02@gmail.com"
password= "Pratham@02"

now=datetime.datetime.now()
today=(now.month , now.day)

data=pandas.read_csv("birthdays.csv")
birthdays_dict={(data["month"] , data["day"]):data for (index ,data) in data.iterrows()}

if today in birthdays_dict:
    birthday_boy_girl =birthdays_dict[today]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content=letter_file.read()
        content =content.replace("[NAME]" , birthday_boy_girl["name"] )
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.login(my_email , password)
            connection.sendmail(from_addr=my_email ,
                                to_addrs="prathameshpalande020201@gmail.com",
                                msg=f"Subject: Happy Birthday!\n\n{content}"
                                )



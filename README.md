# Ascen
To run this app please follow below.

1)git clone https://github.com/Ruxhino-B/Ascen.git

2) cd inside projet cd ascen

3) install requirements.txt
pip install -r requirements.txt

In this time APP is ready to use.
Next step

Open postman

1)go to authorization
2)Select Basic Auth
3)put username

GET http://127.0.0.1:8000/workday Give all list off workday
![Screenshot from 2023-01-27 10-50-46](https://user-images.githubusercontent.com/32514053/215057528-da897d2a-11aa-41e9-bd08-295fe522e28c.png)

POST http://127.0.0.1:8000/workday Add new workday. In this case in body must enter a text like below

{  
    "start_time": "2023-01-24T21:39:54Z",
    "end_time": "2023-01-24T23:39:57Z",
    "user": 1
}
**Please be sure start_time-end_time must me lest that deltatime(16 hour) because i have raseValue Error** look code below

**Please be sure start_time must be lest than end_time** look code below

class WorkDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=15, null=True, blank=True, )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    delta_time = models.CharField(max_length=5, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.start_time >= self.end_time:
            raise ValueError("EndTime Error")
        if self.end_time - self.start_time > datetime.timedelta(hours=16):
            raise ValueError("To much time")
        else:
            self.delta_time = self.end_time - self.start_time
            self.day = str(f'{self.start_time.strftime("%A-%d-%m")}')
        super().save(*args, **kwargs)
  
![Screenshot from 2023-01-27 11-02-51](https://user-images.githubusercontent.com/32514053/215059757-c12272ba-4f79-472a-9ff4-6b938b3ec322.png)


GET http://127.0.0.1:8000/workday/4 return workday with id 4

DELETE http://127.0.0.1:8000/workday/4 delete workday with id 4

PATCH http://127.0.0.1:8000/workday/4 update workday with id 4 example of body change start_time

{    
    "start_time": "2023-01-24T19:39:54Z"  
    
}
![Screenshot from 2023-01-27 11-08-07](https://user-images.githubusercontent.com/32514053/215060639-57692217-a15b-4eaa-8410-c46674537fbd.png)

POST http://127.0.0.1:8000/sendMail send email in email below

{
    
    "start_day": "2023-01-23",
    "end_date": "2023-01-27",
    "email": "enea@ascen.com"
}
![Screenshot from 2023-01-27 11-11-45](https://user-images.githubusercontent.com/32514053/215061384-bfae239f-f0cf-44a8-842d-edb7e94a6e04.png)



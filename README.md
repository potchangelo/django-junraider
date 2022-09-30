# Django Junraider

https://django-junraider.onrender.com

ตัวอย่างโปรเจ็ค Django จากคลิป "สอน Django เบื้องต้น จนใช้ได้จริง" ของ Zinglecode

Note: ทำขึ้นมาเพื่อการศึกษาทางการเขียนโปรแกรมเท่านั้น เนื้อหาบนเว็บไม่ใช่สินค้าหรือบริการที่มีอยู่จริง

(Update 4/8/2022) ถ้าใครรัน migrate แล้วเกิด Error ประมาณว่า ValueError naive datetime ... ให้ดูวิธีแก้ปัญหาที่โพสต์นี้ครับ

https://www.facebook.com/zinglecode/posts/pfbid02AvL5kXanLA8wCMQFBtMXTfres1NSD9nsqSavEhr9W3QQy1C9hzhDLZAypR8Atadl

(Update 30/9/2022) ย้าย Hosting ของเว็บพรีวิว จาก Heroku ไปยัง Render เนื่องจาก Heroku ยกเลิก Free tier ครับ


## YouTube video

Season 1 : https://www.youtube.com/watch?v=BBL8W-lpNHw

Season 2 : https://www.youtube.com/watch?v=tTi2QxB1HJ8


## Install and Run project by VSCode

0. ติดตั้ง Python 3, Pipenv, MySQL, MySQLWorkbench ลงเครื่องให้เรียบร้อยก่อน

1. ดาวน์โหลดโปรเจ็คนี้ลงเครื่อง

2. เปิดโฟลเดอร์โปรเจ็คใน VSCode

3. เปิดไฟล์ project_jrd/.env.sample แล้วเปลี่ยนชื่อเป็น .env จากนั้นให้เปลี่ยนการตั้งค่าให้สอดคล้องกับเครื่องของคุณ เสร็จแล้วบันทึกไฟล์ได้เลย

4. เปิด VSCode Terminal

5. ติดตั้ง Packages ของโปรเจ็ค

```
pipenv install
```

6. Activate pipenv environment

```
pipenv shell
```

7. จัดการ Database migrations ให้เรียบร้อย

```
python manage.py migrate
```

8. สร้าง Admin (Super user) ให้เรียบร้อย

```
python manage.py createsuperuser
```

9. เปิดเว็บโปรเจ็ค

```
python manage.py runserver
```

10. (Optional) ตั้งค่า VSCode Python interpreter ของโปรเจ็คนี้ เพื่อให้ VSCode อ่านข้อมูล Package และแสดง Autocomplete ของโปรเจ็คนี้ได้อย่างสมบูรณ์ วิธีการจะอยู่ในคลิป "สอน Django เบื้องต้น จนใช้ได้จริง # 1" (อาจต้องปิด/เปิด VSCode ใหม่ ซักรอบนึง)


## Github branches for each lessons

### Season 1

1. [Setup and Run](https://github.com/potchangelo/django-junraider/tree/01-setup)
2. [Projects x Apps](https://github.com/potchangelo/django-junraider/tree/02-project-apps)
3. [urls x views](https://github.com/potchangelo/django-junraider/tree/03-urls-views)
4. [views x templates](https://github.com/potchangelo/django-junraider/tree/04-views-templates)
5. [templates x tags](https://github.com/potchangelo/django-junraider/tree/05-templates-tags)
6. [templates x filters](https://github.com/potchangelo/django-junraider/tree/06-templates-filters)
7. [models x migrations](https://github.com/potchangelo/django-junraider/tree/07-models-migrations)
8. [models](https://github.com/potchangelo/django-junraider/tree/08-models)
9. [models x views x templates](https://github.com/potchangelo/django-junraider/tree/09-models-views-templates)
10. [forms x views x templates](https://github.com/potchangelo/django-junraider/tree/10-forms-views-templates)
11. [admin](https://github.com/potchangelo/django-junraider/tree/11-admin)
12. [static images](https://github.com/potchangelo/django-junraider/tree/12-static-images)
13. [static CSS JS](https://github.com/potchangelo/django-junraider/tree/13-static-css-js)
14. [settings x dotenv](https://github.com/potchangelo/django-junraider/tree/14-settings-dotenv)
15. [Deploy to Heroku](https://github.com/potchangelo/django-junraider/tree/15-deploy-heroku)
16. [Season 1 final code](https://github.com/potchangelo/django-junraider/tree/season-1)

### Season 2

1. [Log in](https://github.com/potchangelo/django-junraider/tree/16-login)
2. [Log out](https://github.com/potchangelo/django-junraider/tree/17-logout)
3. [Register](https://github.com/potchangelo/django-junraider/tree/18-register)
4. [Dashboard](https://github.com/potchangelo/django-junraider/tree/19-dashboard)
5. [Profile](https://github.com/potchangelo/django-junraider/tree/20-profile)
6. [Password change](https://github.com/potchangelo/django-junraider/tree/21-password-change)
7. [Password reset](https://github.com/potchangelo/django-junraider/tree/22-password-reset)
8. [Custom user model](https://github.com/potchangelo/django-junraider/tree/23-custom-user-model)
9. [Activate account by email](https://github.com/potchangelo/django-junraider/tree/24-activate-account-by-email)
10. [Log in by email](https://github.com/potchangelo/django-junraider/tree/25-login-by-email)
11. [Cookies](https://github.com/potchangelo/django-junraider/tree/26-cookies)
12. [Favorite food 1](https://github.com/potchangelo/django-junraider/tree/27-favorite-food-1)
13. [Favorite food 2](https://github.com/potchangelo/django-junraider/tree/28-favorite-food-2)
14. [404, 403, 500](https://github.com/potchangelo/django-junraider/tree/29-404-403-500)
15. [Deploy to Heroku again](https://github.com/potchangelo/django-junraider/tree/30-deploy-heroku-2)
16. [Season 2 final code](https://github.com/potchangelo/django-junraider/tree/season-2)

### On preview web

[Branch ของเว็บพรีวิว](https://github.com/potchangelo/django-junraider/tree/preview) -> จะมีการปรับแต่งโค้ดนิดนึงให้ใช้งานบน Host อย่างเหมาะสม


## Credits

https://unsplash.com/photos/66IZaW9LIpI

https://unsplash.com/photos/AfhSPYdkxiU

https://unsplash.com/photos/1Fsb2C7hxQ0

https://unsplash.com/photos/OYUzC-h1glg

https://www.iconfinder.com/icons/6646608/and_bike_cross_moto_motorcycle_transport_vehicles_icon


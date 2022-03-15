# Django Junraider

https://django-junraider.herokuapp.com/

ตัวอย่างโปรเจ็ค Django จากคลิป "สอน Django เบื้องต้น จนใช้ได้จริง # 1" ของ Zinglecode

Note: ทำขึ้นมาเพื่อการศึกษาทางการเขียนโปรแกรมเท่านั้น เนื้อหาบนเว็บไม่ใช่สินค้าหรือบริการที่มีอยู่จริง


## YouTube video

https://www.youtube.com/watch?v=BBL8W-lpNHw


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

- [Branch ของเว็บพรีวิว](https://github.com/potchangelo/django-junraider/tree/preview) -> จะมีการปรับแต่งโค้ดนิดนึงให้ใช้งานบน Host อย่างเหมาะสม


## Credits

https://unsplash.com/photos/66IZaW9LIpI

https://unsplash.com/photos/AfhSPYdkxiU

https://unsplash.com/photos/1Fsb2C7hxQ0

https://unsplash.com/photos/OYUzC-h1glg

https://www.iconfinder.com/icons/6646608/and_bike_cross_moto_motorcycle_transport_vehicles_icon


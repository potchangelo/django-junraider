# Django Junraider

ตัวอย่างโปรเจ็ค Django จากคลิป "สอน Django เบื้่องต้น จนใช้ได้จริง #01" ของ Zinglecode

Note: ทำขึ้นมาเพื่อการศึกษาทางการเขียนโปรแกรมเท่านั้น เนื้อหาบนเว็บไม่ใช่สินค้าหรือบริการที่มีอยู่จริง


## YouTube video

- YouTube link coming soon


## Install Python 3 and pipenv

1. ติดตั้ง Python 3

- macOS -> YouTube
- Windows -> Facebook

2. ติดตั้ง Pipenv

- macOS -> YouTube
- Windows -> Facebook


## Install MySQL and MySQLWorkbench

ติดตั้ง MySQL และ MySQL Workbench

- macOS -> YouTube
- Windows -> Facebook


## Install and Run project by VSCode

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

8. เปิดเว็บโปรเจ็ค

```
python manage.py runserver
```

9. (Optional) ตั้งค่า VSCode Python interpreter ของโปรเจ็คนี้ เพื่อให้ VSCode อ่านข้อมูล Package และแสดง Autocomplete ของโปรเจ็คนี้ได้อย่างสมบูรณ์ วิธีการจะอยู่ในคลิปสอน Django


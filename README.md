# BANK-RUT BACKEND
Riandy Hasan - 18220058
Sebenarnya ini pertama kali saya bikin backend dari awal, banyak kesulitan yang dihadapi dari setup hingga pengerjaan, walaupun hasilnya bukanlah yang terbaik tapi saya senang dengan hasil saya ini.

## STACK YANG DIGUNAKAN
1. Backend service: Python Fastapi
2. Database: Postgresql
3. Deployment: Heroku

## DEPLOYMENT
https://bankrut.herokuapp.com/

## DOKUMENTASI
https://app.swaggerhub.com/apis/16520117/fast-api/0.1.0


## ERD
https://drive.google.com/file/d/1aAcyq7LxfJOX2v9O9xLO9_L5xNgWDDop/view?usp=sharing

## DESIGN PATTERN
1. Singleton
Dalam pembuatannya saya menggunakan design pattern singleton agar menerapkan prinsip Single Responsibility Principle, dengan hal ini maka bisa memastikan bahwa setiap class hanya punya satu functionality.
2. Builder
Untuk mempermudah pembuatan hal yang lebih besar, saya membagi-bagi komponen yang diperlukan ke hal yang lebih kecil sehingga tidak saya bisa menggunakan fungsi-fungsi kecil itu lagi.

## CARA MENJALANKAN
1. Pastikan telah menginstall semua module yang ada di requirement.txt
2. Masuk ke directory app dengan mengetikkan 'cd app'
3. Ketik di terminal 'uvicorn main:appp --reload'
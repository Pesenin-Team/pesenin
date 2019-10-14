
<p align="center">
    <img src="/static/img/LOGO.png" alt="PESENIN LOGO" width="330">
</p>

[![Build Status](https://travis-ci.org/Pesenin-Team/pesenin.svg?branch=master)](https://travis-ci.org/Pesenin-Team/pesenin) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Web application untuk memesan makanan dengan framework django. klik [disini][herokuapp] untuk melihat web.

## Team
- Mushaffa Huda
- Kukuh Hafiyyan
- Muhamad Daril Nofriansyah Badruddin

## 🎓 About

Pesenin adalah sebuah aplikasi yang bertujuan untuk mempermudah mahasiswa dan dosen dalam memesan makanan di kantin, dengan menghubungkan antara penjual dan pembeli dalam satu website.

## 🚀 Quick start

1.  **Create a Local Repository.**

    *Clone* Repository ini.

    ```sh
    $ git clone https://github.com/Pesenin-Team/pesenin.git
    ```

1.  **Start developing.**

    Masuk ke repository hasil *clone* tersebut,dan install requirements menggunakan [`pipenv`][pipenv].

    ```sh
    $ pip install pipenv
    $ pipenv install
    ```

    Jika tidak ingin menggunakan `pipenv`, `pip` juga bisa digunakan.

    ```sh
    $ pip install -r requirements.txt
    ```

1.  **Open the source code and start editing!**

    - Jalankan `python manage.py migrate` untuk migrasi basis data.
    - Jalankan `python manage.py collectstatic` untuk mengumpulkan berkas statis.
    - Jalankan `python manage.py runserver` untuk menjalankan *server*.

    Your site is now running at `http://localhost:8000`!

    Buka `home` directory di text editor pilihanmu dan edit `/templates/home/index.html`. Save dan lihat browser untuk update real time!


## 🧐 Fitur?

- Login page menggunakan SSO untuk mahasiswa dan Dosen.
- memesan makanan sesuai menu.
- mendapat nomor antrian sesuai makanan yang dipesan.
- Penjual dapat membuat menu baru,dan mengganti menu yang lama.
- Penjual juga dapat melihat daftar pesanan, mengganti status menjadi ready dan menghapus jika sudah diambil oleh pembeli.

Lihat dibawah untuk konten *top-level* directory dari project ini

    .
    ├── comingsoon
    ├── pesenin
    ├── templates
    ├── static
    ├── .gitignore
    ├── .travis.yml
    ├── db.sqlite3
    ├── deployment.sh
    ├── manage.py
    ├── LICENSE
    ├── Procfile
    ├── requirements.txt
    └── README.md

1.  **`/comingsoon`**: Directory ini adalah app untuk fitur coming soon dari pesenin.

2.  **`/pesenin`**: Directory ini berisi default starterproject yang disediakan oleh django.

3.  **`/templates`**: Directory ini berisi template base html yang akan digunakan global di semua app di project ini

4. **`/static`**: Directory ini berisi file static yang akan digunakan secara global

5.  **`.gitignore`**: File ini memberi informasi kepada git file mana yang tidak perlu di *track* / di *maintain* versi historynya.

6.  **`.travis.yml`**: File ini digunakan oleh travis.ci untuk melakukan *Continous Integration*

7.  **`db.sqlite3`**: File database dari django **(Tidak akan diubah secara langsung).**

8.  **`deployment.sh`**: File shell script untuk deployment.

9.  **`manage.py`**: manage.py adalah sebuah *thin-wrapper* untuk django-admin, yang berguna untuk me-manage *project package* sebelom mendelegasinya ke django-admin.

10.  **`LICENSE`**: licensed dibawah the MIT license.

11. **`Procfile`**: File untuk CD dengan heroku

12. **`requirements.txt`**: Text file yang berisi tentang requirement module dari project ini, agar dapat di jalankan di environment lain.

13. **`README.md`**: Markdown file berisi referensi informasi penting terhadap project ini.

[herokuapp]: https://pesenin.herokuapp.com 
[pipenv]: https://pypi.org/project/pipenv
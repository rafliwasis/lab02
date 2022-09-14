Link Deploay Aplikasi : https://kriboapp.herokuapp.com/katalog/

#Membuat sebuah README.md yang berisi link menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut:

1) **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan 
   jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!**
   
   ![image](https://user-images.githubusercontent.com/88359990/190054844-7fe94b36-a262-4775-95e9-3d53addf61c5.png)
   Penjelasan bagan diatas:
   
   Penjelasan bagan diatas:
   Hal yang pertama dilakukan adalah user/client akan melakukan request yangmana setiap request ini akan diproses atau dikonfigurasi oleh URL (urls.py). 
   Hal ini dikarenakan dalam urls.py terdapat definisi alamat rute (URL) dan fungsi yang akan dijalankan setiap rute. 
   Kemudian, URL akan meneruskan request tersebut ke fungsi yang terdapat di view (views.py). 
   Dalam tahap ini, akan terjadi beberapa fungsi yang berjalan selanjutnya, seperti menulis dan mengambil data dari model, 
   mendesign tampilan data dari template html (katalog.html), dan melakukan pengiriman HTTP Response ke user.
   
2) **Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

   Dalam hal ini, penggunaan virtual environment dalam project berbasis python sangat direkomendasikan, tetapi bukan berarti wajib untuk menggunakannya. 
   Virtual environment merupakan suatu tools untuk menjaga ruang yang terpisah dalam sebuah proyek dan terisolasi dari dependensi utama. 
   Karena hal ini, virtual environment berguna ketika kita memerlukan dependensi yang berbeda saat membuat proyek pada satu sistem operasi yang sama. 
   Kebutuhan atau dependensi yang berbeda-beda ini akan menimbulkan crash pada proyek. Oleh karena itu, penting bagi kita untuk menggunakan virtual environment 
   karena dapat menjalankan suatu proyek tanpa merubah konfigurasi pada sistem operasi yang kita miliki. 
   
3) **Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas**
   
   
   1. Hal pertama yang saya lakukan adalah dengan menambahkan beberapa kode pada file views.py, yaitu pada fungsi show_katalog. 
      Views ini akan berguna untuk merespon setiap data dari models dan memproses atau mengambil data yang terdapat pada database. 
      Pada fungsi show_katalog saya menambahkan variabel nama dan npm yang merupakan identitas saya yang nantinya akan ditampilkan dan dipanggil pada file HTML.
   2. Hal yang kedua saya lakukan adalah dengan merouting antara views.py dengan katalog.html menggunakan file urls.py. Dalam hal ini, urls.py akan melakukan routing 
      terhadap fungsi show_katalog pada views yang nantinya akan ditampilkan pada laman HTML. Pada views.py juga harus menambahkan path aplikasi katalog yang terdapat 
      pada folder project_django.
   3. Tahap selanjutnya adalah saya melakukan beberapa perubahan pada file katalog.html dengan mengganti FILLME menjadi {{nama}} dan {{npm}} yang memanggil variabel 
      tersebut pada file views.py. Kemudian, saya menggunakan iterasi for loop pada list_barang untuk mengambil setiap data dalam database lalu ditampilkan pada 
      laman website.
   4. Tahap terakhir pada tugas ini adalah dengan melakukan deploy terhadap aplikasi yang sudah dibuat menggunakan heroku, yaitu dengan cara menghubungkan repo github 
      tugas 2 ini pada heroku dan berhasil di deploy.

   
   
    

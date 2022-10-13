[Link Aplikasi Heroku]
http://kriboapp.herokuapp.com/todolist/

**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
Asynchronus Programming -> merupakan pemrograman yang tidak terikat pada I/O protocol. User dapat
berpindah ke tugas lain atau page lain sebelum yang hal sebelumnya selesai. Oleh karena itu, pemrograman
ini dapat menangani beberapa request secara bersamaan sehingga dapat menyelesaikan lebih banyak tugas
dalam satu periode waktu

Synchronous Programming -> sedangkan pada pemrograman ini, tugas hanya dilakukan satu persatu dan 
hanya selesai ketika yang sebelumnya selesai atau yang satunya selesai. Oleh karena itu, user harus menunggu
tugas selesai agar dapat pindah ke tugas berikutnya

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud 
dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Dalam penerapan JavaScript dan Ajax, terdapat paradigma Evenet Driven Programming yang diterapkan ketika kita
ingin menghandle / menanggapi suatu action atau event pada website. Ketika user merequest sesuatu pada website,
paradigma ini akan merespon hal tersebut dan menanggapinya, misal ketika kita mengeklik suatu tombol/ikon.
Pada tugas ini, saya menerapkan event driven programming ketika user ingin add suatu task, sehingga paradigma ini
akan menjalankan fungsi untuk add suatu task.

**Jelaskan penerapan asynchronous programming pada AJAX.**
Pada JavaScript, AJAX akan menerapkan konsep asynchronous programming ketika akan mengeksekusi suatu task pada
program. Pada tugas ini, AJAX berpengaruh dalam pengambilan data serta ketika menanggapi suatu response dalam bentuk
JSON. Ketika kita menekan tombol add pada program, maka program akan melakukan AJAX POST yang mana akan mengirim data
ke server. Kemudian, data akan ditangkap dan dikirimkan ke server tanpa adanya reload pada browser. Kita hanya perlu
menambahkan library JQuery pada templates todolist.html, lalu JQuery tersebut akan melakukan pemanggilan function
success dan error

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1) Hal pertama yang saya lakukan adalah dengan menambahkan beberapa function baru pada views untuk mengambil suatu data
yang direpresentasikan dengan JSON.
2) Kemudian menambahkan beberapa path di urls.py untuk function yang sudah ditambahkan pada views.py
3) Berpindah ke todolist.html, saya membuat fungsi GET untuk mengambil data yang akan ditampilkan.
4) Kemudian, saya mengubah href atau link pemetaan ketika user menekan tombol create task pada navbar agar program menghandle
target modal yang sudah dibuat sebelumnya dengan menggunakan template dari bootstrap
5) Langkah selanjut, saya membuat fungsi POST pada todolist.html untuk menambahkan data dari user/pengguna
6) Dengan demikian, fitur add akan dilakukan secara asynchronous



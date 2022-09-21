Jelaskan perbedaan antara JSON, XML, dan HTML!
*JSON(JavaScript Object Notation) merupakan suatu format yang berguna untuk menyimpan, membaca, dan menukar informasi dari server web
*XML dan HTML hampir sama, tetapi XML (Extensible Markup Language) akan lebih berfokus pada transfer data, sedangkan HTML akan lebih berfokus pada penyajian datanya, selanjutnya XML berfokus pada struktur dan konteks, tetapi jika HTML berfokus pada tampilan format dari data

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
*- Hal yang pertama dilakukan adalah membuat aplikasi atau folder bernama mywatchlist melalui "python manage.py startapp". Dengan melakukan ini, kita akan mendapatkan beberapa file yang selanjutnya akan kita isi dan dihubungkan satu sama lainnya
*- Hal kedua yang saya lakukan adalah dengan menambahkan path melalui urls.py pada project_django, yaitu memasukkan mywatchlist pada url_patterns
*- Hal ketiga yang saya lakukan adalah dengan menambahkan pada models.py, yaitu berupa variabels serta fieldsnya
*- Hal keempat yang saya lakukan adalah dengan membuat beberapa data (minimal 10), pada fixtures yang dibuat pada app mywatchlist
*- Hal kelima yaitu dengan membuat beberapa fungsi pada views.py berkaitan dengan html xml dan json serta melakukan routing menggunakan urls.py pada mywatchlist
*- Ketika sudah selesai, lalu kita membuat testing, dengan membuat beberapa method yang berbeda, untuk html json dan xml
*- Lalu kita push dan commit dan terdeploy pada repository yang sama pada tugas minggu lalu.

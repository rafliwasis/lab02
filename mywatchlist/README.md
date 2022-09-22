Link HTML: https://kriboapp.herokuapp.com/mywatchlist/html/
Link JSON: https://kriboapp.herokuapp.com/mywatchlist/json/
Link XML: https://kriboapp.herokuapp.com/mywatchlist/xml/

Jelaskan perbedaan antara JSON, XML, dan HTML!
*JSON(JavaScript Object Notation) merupakan suatu format yang berguna untuk menyimpan, membaca, dan menukar informasi dari server web
*XML dan HTML hampir sama, tetapi XML (Extensible Markup Language) akan lebih berfokus pada transfer data, sedangkan HTML akan lebih berfokus pada penyajian datanya, selanjutnya XML berfokus pada struktur dan konteks, tetapi jika HTML berfokus pada tampilan format dari data

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
*Ketika kita mengembangkan suatu platform, kita perlu mengirimkan data dari stack satu ke stack lainnya. Data yang akan dikirim memiliki bentuk yang berbeda, berikut merupakan contoh format data yang sering digunakan: HTML, XML, dan JSON

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
*- Hal yang pertama dilakukan adalah membuat aplikasi atau folder bernama mywatchlist melalui "python manage.py startapp". Dengan melakukan ini, kita akan mendapatkan beberapa file yang selanjutnya akan kita isi dan dihubungkan satu sama lainnya
*- Hal kedua yang saya lakukan adalah dengan menambahkan path melalui urls.py pada project_django, yaitu memasukkan mywatchlist pada url_patterns
*- Hal ketiga yang saya lakukan adalah dengan menambahkan pada models.py, yaitu berupa variabels serta fieldsnya
*- Hal keempat yang saya lakukan adalah dengan membuat beberapa data (minimal 10), pada fixtures yang dibuat pada app mywatchlist
*- Hal kelima yaitu dengan membuat beberapa fungsi pada views.py berkaitan dengan html xml dan json serta melakukan routing menggunakan urls.py pada mywatchlist
*- Ketika sudah selesai, lalu kita membuat testing, dengan membuat beberapa method yang berbeda, untuk html json dan xml
*- Lalu kita push dan commit dan terdeploy pada repository yang sama pada tugas minggu lalu.

*Postman
![image](https://user-images.githubusercontent.com/88359990/191558757-7e488f20-f91b-4de4-9f27-8052ad606310.png)

![image](https://user-images.githubusercontent.com/88359990/191558779-28c7491b-4f2a-4e2b-ac77-d2f892e6af84.png)

![image](https://user-images.githubusercontent.com/88359990/191559641-da5a5c75-024b-49bc-a2fc-dea6f9419932.png)



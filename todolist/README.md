Link Aplikasi TodoList App: https://kriboapp.herokuapp.com/todolist/login/ 

**1. Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**
{% csrf_token %} dalam elemen form berguna untuk melindungi dari serangan siber atau menghindari beberapa link yang nantinya dapat
disalahgunakan oleh orang lain. Pada hal ini, csrf akan mengcompare dua token berbeda dari perspektif user/pengguna dan juga request.
Apabila token tidak sesuai, maka request elemen form akan direject/tidak dieksekusi. Sebaliknya, jika token sesuai, maka form tersebut 
akan merespon OK. Oleh karena itu, jika CSRF tidak terdapat pada form, bisa saja kita mendapatkan serangan siber karena
request input yang dikirim pengguna tidak dicek kembali.

**2. Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran 
besar bagaimana cara membuat form secara manual.**
Untuk membuat elemen form secara manual, kita bisa menggunakan method POST dan memberikan {% csrf_token %} agar terhindar dari hal yang tidak
diinginkan. Selanjutnya, kita bisa menambahkan tag table dengan berisikan tr, th, maupun td. Dalam hal ini, tag tr akan berguna sebagai wadah
untuk tag inputan. Lalu dengan menggunakan method request.POST.get{{xxx}} akan digunakan untuk mengakses input dari user

**3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data 
yang telah disimpan pada template HTML**
Submisi yang dilakukan oleh user dapat diakses melalui request.POST.get{{xxx}} atau nama input. Kemudian, data tersebut akan dicompare lalu disesuaikan
pada file models.py. Selanjutnya, data yang sudah dibandingkan tersebut akan disimpan pada database. Kita bisa mengaksesnya dengan menggunakan 
(nama class/models).objects.filter(user=request.user) karena kita akan memfilter data berdasarkan user yang login. Filter yang dilakukan akan melalui
context dan juga akan dirender ke templates (html).

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Langkah pertama, saya menjalankan startapp todolist untuk membuat proyek todolist pada django
2. Kemudian kita mendaftarkan path aplikasi todolist ini pada urls.py di project django
3. Selanjutnya, masuk kedalam models.py yang terdapat pada todolist, lalu membuat class Task yang berisi:
   - user: models.foreignkey
   - date: models.datetimefield
   - title: models.charfield
   - description: models.textfield
4. Kemudian, kita menambahkan beberapa fungsi pada views.py yang berupa login, logout, dan register. Ketiga fungsi ini
   nanti akan dilanjutkan ke templates atau html yang sudah dibuat.
5. Membuat todolist.html dengan menambahkan username pengguna melalui {{userName}} yang terdapat pada context, lalu membuat
beberapa button untuk create new task serta logout dan juga terdapat tabel yang berisi date, todo title, dan description
6. Lalu membuat createtask.html untuk menambahkan todolist user yang berupa judul dan deskripsi todolist
7. Ketika sudah selesai semua, lalu daftarkan beberapa fungsi yang sudah dibuat kedalam path yang berada pada urls.py pada
todolist app
8. Lalu melakukan git push, commit dan terdeploy secara otomatis pada heroku
9. Selanjutnya, kita mencoba untuk membuat 2 akun serta 3 data dalam masing" akun

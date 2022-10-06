Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS merupakan suatu style yang dapat dituliskan langsung pada atribut HTM
(+) Dapat merubah secara langsung pada tag HTML sehingga dapat mengupdate CSS secara cepat, proses load ke wibste juga cepat, dan membantu para web developer ketika ingin mengecheck perubahan pada tag HTML
(-) Tidak efisien karena hamya diterapkan pada satu line atau tag HTML saja

Internal CSS merupakan suatu style yang dituliskan pada header file HTML
(+) Tidak perlu menggunakan banyak file eksternal, membantu mengubah page dalam tampilan yang berbeda-beda karena hanya style hanya terdapat pada 1 page saja
(-) Peforma website menjadi lambat karena terdapat CSS yang berbeda pada setiap page, codingan yang terlihat berantakan karena menyatukan CSS dan HTML sehingga terlihat terlalu banyak

Eksternal CSS merupakan suatu style yang dituliskan pada file eksternal (misal: style.css) lalu diimport kedalam file HTML
(+) Kode dalam HTML terlihat rapih karena style CSS dituliskan pada file eksternal, loading pada website juga cepat, File dapat digunakan untuk beberapa halaman
(-) Biasanya bisa terjadi error dalam pemanggilan sehingga tidak terlihat perubahannya dalam page

Jelaskan tag HTML5 yang kamu ketahui.
tag p untuk merepresentasikan paragraf
tag div untuk membuat section/container
tag link untuk menginclude suatu path/link
tag title  untuk mengatur title tab browser
tag a untuk menambah suatu link pada page
tag body untuk membuat dokumen body
tag head untuk membuat head dokumen, bisa berisi title
tag h1 sampai h6 untuk mendefinisikan html headings (headings untuk font, yaitu seperti besar kecil font)

Jelaskan tipe-tipe CSS selector yang kamu ketahui.
selector tag <p> untuk memilih elemen berdasarkan nama tag untuk menambahkan style.
selector class (misal : .login{}) akan memilih elemen berdasarkan nama class yang diberikan untuk menambahkan style.
selector id (misal : #style {}) bersifat lebih unik sehingga dapat digunakan oleh satu elemen saja untuk menambahkan style. 
selector pseudo akan memilih elemen semu seperti state pada elemen, pada selector ini terdapat dua macam selector pseudo, yaitu pseudo-element dan pseudo-class.
selector atribut akan memilih elemen berdasarkan atribut untuk menambahkan style.

Jelaskan bagaimana cara kamu mengimplementasikan checklist diatas!
1) Meletakkan link bootstrap pada bagian head atau menginstall bootstrap agar bootstrap dapat connect ke HTML, dan jangan lupa meletakkan load static agar ketika kita menggunakan css external dapat terpanggil
2) Pada page login dan create task, saya hanya menggunakan css dengan menambahkan form. Serta mengubah tampilan dengan memberikan warna gradient serta shadow pada form. Pada register, saya menggunakan class cards lalu table register dimasukkan kedalam cards tersebut. Selanjutnya, mengatur posisi tengah pada cards tersebut
3) Pada page todolist, kita menambahkan class berupa cards yang mana cards tersebut di foorlop dan ketika cards berjumlah lebih dari 3, maka cards selanjutnya akan ditampilkan pada line berikutnya, saya juga menggunakan navbar collapse serta footer yang menandakan akhir bagian dalam page tsb

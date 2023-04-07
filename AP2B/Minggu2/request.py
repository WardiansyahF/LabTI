# import agar bisa memakai method post dan get
import requests

# untuk mengisi data yang kita butuhkan yang berbentuk object
payload = {"nama": "Wardiansyah",
           "kelas": "2IA01",
           "npm": "51421514"
           }
# digunakan pada request get agar kita bisa mencari postingan
parameter = {'id': 2}
# post untuk mengirimkan data ke API jsonplaceholder
addpost = requests.post(
    'https://jsonplaceholder.typicode.com/posts', data=payload)
# untuk mengambil postingan yang ada di jsonplaceholder sesuai parameter id
getPostbyId = requests.get(
    'https://jsonplaceholder.typicode.com/posts', params=parameter)


if (addpost.status_code == 201):
   # untuk mengecek apakah data berhasil terkirim atau tidak
    print('Data berhasil dikirim')
    print(addpost.text)
else:
    # jika gagal maka akan menampilkan data gagal dikirim
    print('Data gagal dikirim')

# menampilkan data yang sudah diambil
print(getPostbyId.text)
print(getPostbyId.status_code)

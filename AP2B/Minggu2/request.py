# import agar bisa memakai method post dan get
import requests

# untuk mengisi data yang kita butuhkan yang berbentuk object
payload = {"nama": "Wardiansyah",
           "kelas": "2IA01",
           "npm": "51421514"
           }
# digunakan pada request get agar kita bisa mencari postingan
parameter = {'id': 2}

# endpoint yang dituju
endpoint = 'https://jsonplaceholder.typicode.com/posts'

# post untuk mengirimkan data ke API jsonplaceholder
addpost = requests.post(endpoint, data=payload)
# untuk mengambil postingan yang ada di jsonplaceholder sesuai parameter id
getPostbyId = requests.get(endpoint, params=parameter)

print("[POST")
if (addpost.status_code == 201):
   # untuk mengecek apakah data berhasil terkirim atau tidak
    print('Data berhasil dikirim')
    print(addpost.text)
    print("\nStatus code : ",addpost.status_code)
else:
    # jika gagal maka akan menampilkan data gagal dikirim
    print('Data gagal dikirim')

print("\n[GET]")
# menampilkan data yang sudah diambil
print(getPostbyId.text)
print("\nStatus code : ",getPostbyId.status_code)

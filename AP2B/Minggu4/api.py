from flask import Flask, request, jsonify

app = Flask(__name__)

datas = [
    {
        'id': 1,
        'nama': 'Toko Bunga',
        'items' : [
            {
                'name' : 'Bunga Kecombrang',
                'price' : 5000
            }
        ]
    },{
        'id': 2,
        'nama' : 'Toko Buku',
        'items' : [
            {
                'name' : 'Buku Tangkuban Perahu',
                'price' : 10000
            }
        ]
    }
]

@app.route('/store') #127...:5000/store
def getAll():
    return jsonify(datas)
    
@app.route('/store/<int:id>') #127...:5000/store/3
def getbyId(id):
    for data in datas:
        if (data)['id'] == id:
            return jsonify(data)
    return jsonify({'message': 'Data not found'})


@app.route('/store', methods=["POST"])  # 127...:5000/store
def addStore():
    req_data = request.get_json()
    new_data = {
        'id': req_data['id'],
        'nama': req_data['nama'],
        'items' : req_data['items']
    }
    datas.append(new_data)
    return jsonify(new_data)

@app.route('/') #127...:5000/
def home():
    return "Hello peeps!"

if __name__ == '__main__':
  app.run(debug=True)
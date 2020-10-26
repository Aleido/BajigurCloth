# Required Libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Creating Flask Application
app = Flask(__name__)

# Connecting MYSQL Database BajigurCloth
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/BajigurCloth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initiating SQLAlchemy and Marshmallow objects
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Creating Task Model using SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(70), unique=True)
    phone = db.Column(db.String(30))
    alamat = db.Column(db.String(100))

    def __init__(self, nama, phone, alamat):
        self.nama = nama
        self.phone = phone
        self.alamat = alamat

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kodeSKU = db.Column(db.String(50), unique=True)
    namabarang = db.Column(db.String(50))
    bahan = db.Column(db.String(30))
    warna = db.Column(db.String(30))
    ukuran = db.Column(db.String(10))
    harga = db.Column(db.Integer)

    def __init__(self, kodeSKU, namabarang, bahan, warna, ukuran, harga):
        self.kodeSKU = kodeSKU
        self.namabarang = namabarang
        self.bahan = bahan
        self.warna = warna
        self.ukuran = ukuran
        self.harga = harga

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kodeSKU = db.Column(db.String(50), unique=True)
    tanggalmasuk = db.Column(db.DateTime)
    tanggalupdate = db.Column(db.DateTime)
    stock = db.Column(db.Integer)
    lokasi = db.Column(db.String(30))

    def __init__(self, kodeSKU, tanggalmasuk, tanggalupdate, stock, lokasi):
        self.kodeSKU = kodeSKU 
        self.tanggalmasuk = tanggalmasuk 
        self.tanggalupdate = tanggalupdate 
        self.stock = stock 
        self.lokasi = lokasi

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer)
    tanggalorder = db.Column(db.DateTime)
    amount = db.Column(db.Integer)
    status = db.Column(db.String(20))

    def __init__(self, userID, tanggalorder, amount, status):
        self.userID = userID 
        self.tanggalorder = tanggalorder 
        self.amount = amount 
        self.status = status 


db.create_all()

# Creating UserSchema using marshmallow
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama', 'phone', 'alamat')

# Generating object of UserSchema for single object and for multiple object
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Inputan Data User / Customer
@app.route('/user', methods=['Post'])
def create_user():
  nama = request.json['nama']
  phone = request.json['phone']
  alamat = request.json['alamat']

  new_user= User(nama, phone, alamat)

  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

@app.route('/user', methods=['GET'])
def get_users():
  all_user = User.query.all()
  result = users_schema.dump(all_user)
  return jsonify(result)

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
  user = User.query.get(id)
  return user_schema.jsonify(user)

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
  user = User.query.get(id)

  nama = request.json['nama']
  phone = request.json['phone']
  alamat = request.json['alamat']

  user.nama = nama
  user.phone = phone
  user.alamat = alamat

  db.session.commit()

  return user_schema.jsonify(user)

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
  user = User.query.get(id)
  db.session.delete(user)
  db.session.commit()
  return user_schema.jsonify(user)

#========================= PRODUCT
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'kodeSKU',  'namabarang', 'bahan', 'warna', 'ukuran', 'harga' )

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Inputan Data product
@app.route('/product', methods=['Post'])
def create_product():
  kodeSKU = request.json['kodeSKU'] 
  namabarang = request.json['namabarang'] 
  bahan = request.json['bahan'] 
  warna = request.json['warna'] 
  ukuran = request.json['ukuran'] 
  harga = request.json['harga']

  new_product= Product(kodeSKU, namabarang, bahan, warna, ukuran, harga )

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

@app.route('/product', methods=['GET'])
def get_products():
  all_product = Product.query.all()
  result = products_schema.dump(all_product)
  return jsonify(result)

@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  kodeSKU = request.json['kodeSKU'] 
  namabarang = request.json['namabarang'] 
  bahan = request.json['bahan'] 
  warna = request.json['warna'] 
  ukuran = request.json['ukuran'] 
  harga = request.json['harga']

  product.kodeSKU = kodeSKU
  product.namabarang = namabarang
  product.bahan = bahan
  product.warna = warna
  product.ukuran = ukuran
  product.harga = harga

  db.session.commit()

  return product_schema.jsonify(user)

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()
  return product_schema.jsonify(product)

#========================= INVENTORY
class InventorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'kodeSKU', 'tanggalmasuk', 'tanggalupdate', 'stock', 'lokasi' )

inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)

# Inputan Inventory product
@app.route('/inventory', methods=['Post'])
def create_inventory():
  kodeSKU = request.json['kodeSKU'] 
  tanggalmasuk = request.json['tanggalmasuk']
  tanggalupdate = request.json['tanggalupdate']
  stock = request.json['stock']
  lokasi = request.json['lokasi'] 

  new_inventory= Inventory(kodeSKU, tanggalmasuk, tanggalupdate, stock, lokasi )

  db.session.add(new_inventory)
  db.session.commit()

  return inventory_schema.jsonify(new_inventory)

@app.route('/inventory', methods=['GET'])
def get_inventories():
  all_inventories = Inventory.query.all()
  result = inventories_schema.dump(all_inventories)
  return jsonify(result)

@app.route('/inventory/<id>', methods=['GET'])
def get_inventory(id):
  inventory = Inventory.query.get(id)
  return inventory_schema.jsonify(inventory)

@app.route('/inventory/<id>', methods=['PUT'])
def update_inventory(id):
  inventory = Inventory.query.get(id)
  
  kodeSKU = request.json['kodeSKU'] 
  tanggalmasuk = request.json['tanggalmasuk']
  tanggalupdate = request.json['tanggalupdate']
  stock = request.json['stock']
  lokasi = request.json['lokasi'] 


  inventory.kodeSKU = kodeSKU
  inventory.tanggalmasuk = tanggalmasuk
  inventory.tanggalupdate = tanggalupdate
  inventory.stock = stock
  inventory.lokasi = lokasi 

  db.session.commit()

  return inventory_schema.jsonify(inventory)

@app.route('/inventory/<id>', methods=['DELETE'])
def delete_inventory(id):
  inventory = Inventory.query.get(id)
  db.session.delete(inventory)
  db.session.commit()
  return inventory_schema.jsonify(inventory)

#========================= ORDER
class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'userID', 'tanggalorder', 'amount', 'status' )

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Inputan Order 
@app.route('/order', methods=['Post'])
def create_order():
  userID = request.json['userID'] 
  tanggalorder = request.json['tanggalorder']
  amount = request.json['amount']
  status = request.json['status'] 

  new_order= Order(userID, tanggalorder, amount, status )

  db.session.add(new_order)
  db.session.commit()

  return order_schema.jsonify(new_order)

@app.route('/order', methods=['GET'])
def get_orders():
  all_order = Order.query.all()
  result = orders_schema.dump(all_order)
  return jsonify(result)

@app.route('/order/<id>', methods=['GET'])
def get_order(id):
  order = Order.query.get(id)
  return order_schema.jsonify(order)

@app.route('/order/<id>', methods=['PUT'])
def update_order(id):
  order = Order.query.get(id)
  
  userID = request.json['userID'] 
  tanggalorder = request.json['tanggalorder']
  amount = request.json['amount']
  status = request.json['status'] 

  order.userID = userID 
  order.tanggalorder = tanggalorder 
  order.amount = amount 
  order.status = status

  db.session.commit()

  return inventory_schema.jsonify(order)

@app.route('/order/<id>', methods=['DELETE'])
def delete_order(id):
  order = Order.query.get(id)
  db.session.delete(order)
  db.session.commit()
  return order_schema.jsonify(order)

# Cek API TOKO
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'ini adalah backend system toko Bajigur Cloth'})

# It will run flask Application
if __name__ == "__main__":
    app.run(debug=True)
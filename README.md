# Bajigur BackEnd API Proses

Ini adalah proses dasar BackEnd untuk toko bajigur cloth yang berisi :
- User        -> untuk menyimpan data customer
- Product     -> untuk menyimpan data detail product
- Inventory   -> untuk menyimpan data inventory
- Order       -> untuk menyimpan data pemesanan yang dilakukan oleh user

# Installation

- ```pip install requirements.txt```

Buat database BajigurCloth

# APIs
- GET http://localhost:5000/

## User
- Model request body json
```
{
"nama":"Budi Santoso",
"phone":"0274 3788998",
"alamat":"Jalan Gendu 09, Yogyakarta"
}
```
- POST http://localhost:5000/user
- GET http://localhost:5000/user
- GET http://localhost:5000/user/<id>
- PUT http://localhost:5000/user/<id>
- DELETE http://localhost:5000/user/<id>

## Product
- Model request body json
```
{
      "bahan": "Combed Cotton 65S", 
      "harga": 75000, 
      "kodeSKU": "TS09090", 
      "namabarang": "Kaos Jetmen", 
      "ukuran": "Large", 
      "warna": "Biru Laut"
    }
```    
- POST http://localhost:5000/product
- GET http://localhost:5000/product
- GET http://localhost:5000/product/<id>
- PUT http://localhost:5000/product/<id>
- DELETE http://localhost:5000/product/<id>

## Inventory
- Model request body json
```
{
  "kodeSKU" : "SH0909",
  "tanggalmasuk" : "2020-10-26 12:00:00",
  "tanggalupdate" : "2020-10-26 12:00:00",
  "stock" : 10,
  "lokasi" : "B-10"
}
```
- POST http://localhost:5000/inventory
- GET http://localhost:5000/inventory
- GET http://localhost:5000/inventory/<id>
- PUT http://localhost:5000/inventory/<id>
- DELETE http://localhost:5000/inventory/<id>

## Order
- Model request Body json
```
{
  "userID" : 2,
  "tanggalorder" : "2020-10-26 13:09:34",
  "amount" : 700000,
  "status" : "Lunas"
}
```
- POST http://localhost:5000/order
- GET http://localhost:5000/order
- GET http://localhost:5000/order/<id>
- PUT http://localhost:5000/order/<id>
- DELETE http://localhost:5000/order/<id>


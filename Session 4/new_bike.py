from flask import Flask, render_template, request, redirect
from bson.objectid import *
from bike_db import bike_coll

app = Flask(__name__)



# bike_list = [
#     {
#     "model" : "Honda SH Mode",
#     "daily_fee" : 250000,
#     "link" : "https://danhgiaxe.net/wp-content/uploads/2018/04/honda-sh-mode-mau-trang.jpg",
#     "year" : 2017
# },
# {
#     "model" : "Honda Future X",
#     "daily_fee" : 100000,
#     "link" : "https://imgwebikevn-8743.kxcdn.com/JEYhOP8_aY2pE8GRcnfnbTW6S80=/product/2018/11/12/wvn.05be973c478fba0.37227067.jpg",
#     "year" : 2013
# },
# {
#     "model" : "Yamaha NVX",
#     "daily_fee" : 250000,
#     "link" : "https://media.karousell.com/media/photos/products/2018/04/11/yamaha_nvx_coverset_1523433051_ab913759.jpg",
#     "year" : 2018
# },
# {
#     "model" : "Vinfast Klara",
#     "daily_fee" : 200000,
#     "link" : "https://giaxeoto.vn/admin/webroot/img/upload2/danh-gia-xe-vinfast-klara.JPG",
#     "year" : 2019
# }
# ]

# bike_coll.insert_many(bike_list)

@app.route("/bike_list")
def bike():
    bike_list = bike_coll.find()
    return render_template("bike.html", bike_list = bike_list)

@app.route("/bike_list/new_bike", methods = ['GET', 'POST'])
def new_bike():
    if request.method == "GET":
        return render_template("new_bike.html")
    elif request.method == "POST":
        form = request.form
        new_bike = {
            "model" : form["model"],
            "daily_fee" : form["fee"],
            "link" : form["link"],
            "year" : form["year"]
        }
        bike_coll.insert_one(new_bike)
        return redirect('/bike_list')

if __name__ == "__main__":
    app.run(debug=True)
 
from flask import Flask, request
import sqlite3 as sql
import os.path

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test1.db")

# sample data creation method
def insert_data():
    con = sql.connect(db_path)
    cur = con.cursor()
    for i in range(1, 11):
        cur.execute("INSERT INTO shop (id,name,place,type) VALUES (?,?,?,?)",
                    (i, "shop_" + str(i), "place_" + str(i), "type_" + str(i)))
    con.commit()
    con.close()

def select_shop():
    con = sql.connect(db_path)
    cur = con.cursor()
    result = cur.execute("select * from shop")
    print("res:", result.fetchall())
    con.close()

def add_tag(shop_id, tag):
    result = False
    try:
        con = sql.connect(db_path)
        cur = con.cursor()
        con.execute("INSERT INTO tags (shopid, tag) VALUES (?,?)", (shop_id, tag))
        con.commit()
        con.close()
        result = True
    except:
        print ("error while adding tag", tag , "shop id = "+shop_id)
        result = False
    return result

@app.route('/shop/addTag/<shopid>/<tagName>', methods=['GET'])
def addTag(shopid, tagName):
    print("addTag")
    print (shopid, tagName);
    result = add_tag(shopid,tagName)
    if result:
        return "Added tag: " + tagName + " for shop-id: " + shopid
    else:
        return "Failed to add tag: " + tagName + " for shop-id: " + shopid

@app.route('/')
def app_root_handler():
    #insert_data()
    select_shop()
    #add_tag(1, "tag1")
    return 'Welcome to Tagging System.'


if __name__ == '__main__':
    app.run()

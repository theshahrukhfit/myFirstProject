# import os
# import pathlib

# root = "static/images/"
# text = "dresses"
# osfile = os.listdir(f"{root}{text}")
# print(osfile)

# root = "static/images"

# for path, subdirs, files in os.walk(root):
#     print(subdirs)
#     for name in files:
#         print(pathlib.PurePath(path, name))


# from collections import defaultdict
# from cs50 import SQL

# db = SQL("sqlite:///database.db")

# query = db.execute("SELECT products.id, productimg.url, products.price, products.name, pcategory.catname, pcategory.id AS catid FROM productimg JOIN products ON productimg.id = products.id JOIN pcategory ON products.cateid = pcategory.id ORDER BY CASE WHEN catid = 1 THEN 1 ELSE 2 END, catid;")



# catedict['Linen'].append(query[1])
# catedict['Linen'].append(query[0])

# for key, item in catedict.items():
#     print(key)
#     for i in item:
#         print(i)


# print(catedict)


# dictList = []
# d = {}
# tempchk = ''
# for i in query:
    
#     if i['catname'] != tempchk:
#         tempchk = i['catname']
#         d[i['catname']] = i
#         dictList.append(d)
#         continue
#     else:
#         d = i
#         dictList.append(d)

# print(d)

# for i in range(len(dictList)):
#     for key, inkey in dictList[i].items():
#         print(key)
#     for j in inkey:
#         print(j)


# #For Template
# for i in range(len(dictList)):
#     for key, inkey in dictList[i].items():
#         print(key)


    





# templist = []
# tempid = ''
# for item in query:
#     if item['catname'] != tempid:
#         tempid = item['catname']
#         print(item['catname'])
#         templist.append(item)
#         continue
#     item['catname'] = ''
#     print(item['catname'])
#     templist.append(item)

# for catenw in templist:
#     print(catenw)




# dictlist = db.execute("SELECT productimg.url, products.price, products.name FROM productimg JOIN products ON productimg.id = products.id JOIN ProductsRecord ON products.id = ProductsRecord.pid ORDER BY timespuchased DESC LIMIT 10;")

# print(dictlist[0]['url'])

# string = 'a'
# string2 = 'a'

# def checkscopee():
#     if string and string2:
#         checkscope = "hi"
#         print("yes")

#     print(checkscope)
# checkscopee()

# list1 = [1, 2, 3, 4]

# prei = ""
# for i in list1:

#     if i != prei:
#         prei = i
    


# from collections import defaultdict, Counter
# from cs50 import SQL

# db = SQL("sqlite:///database.db")

# session = {}

# if 'cart' not in session:
#     session['cart'] = [1, 2, 2, 2, 3, 3]

# counter = {}
# for i in session['cart']:
#     counter[i] = counter.get(i, 0)+1

# #Placing the user Selected Product ID into DB querry
# forQ = str(list(counter)).strip('[]')
# ex_str = 'SELECT * FROM products WHERE id in (' + forQ + ');'
# dbcounted = db.execute(ex_str)

# #Adding the counted quantity dictionary into the query
# for j in range(len(dbcounted)):
#     dbcounted[j].update({'Quantity': counter[dbcounted[j]['id']]})

# print(dbcounted)



# # count = Counter()
# counter = {}

# for i in session['cart']: counter[i]=counter.get(i, 0)+1

# test2 = str(list(counter)).strip('[]')

# print(test2)



# for i in session['cart']:
#     count[i] += 1



# # test1 = count.keys()

# test1 = count
# print(test1)
# test2 = str(list(count)).strip('[]')
# print(test2)
# print(test3)
# dbcounted = db.execute('SELECT * FROM products WHERE id IN (:count);', count = test3)
# print(dbcounted)

# ex_str = 'SELECT * FROM products WHERE id in (' + test3 + ');' 
# dbcounted = db.execute(ex_str)
# # print(dbcounted)

# for j in range(len(dbcounted)):
#     dbcounted[j].update({'Quantity': test1[dbcounted[j]['id']]})

# print(dbcounted)

# for x, j in enumerate(dbcounted):
#     j['Quantity'] = test1[j['id']]
#     update

    



# session['cart'][0] = defaultdict(dict) 
# session['cart'][0]['quantity'] = 4
# print(session)

# counter = {}

# for i in session['cart']: counter[w]=counter.get(w, 0)+1
# print(counter)


# dicttest = {
#     "Quantity": { 4: 2 }
# }


# print((list(dicttest['Quantity'].keys())[0]))

# testlist = {
#     1 : 2 + 2 + 5,
#     2 : 2,
#     3 : 2,
#     4 : 2
# }

# print(testlist[1])


# if list(dicttest['Quantity'].keys())[0] in list(testlist.keys()):
#     print('yes')

# from collections import defaultdict

# productIDs = ["test1", 'test1', 'test2']

# #Counting the quantity of selected products if more than one add their quantity
# counter = defaultdict(list)
# counter2 = {1:2, 3:4, 5:6}
# for i in productIDs:
#     counter[i] = counter.get(i, 0) + 1

# counter['test123'].append(counter2)

# print(counter)



# productids = [1, 2, 3, 3, 3, 4, 5, 6, 5]

# productids = list(filter((3).__ne__, productids))

# print(productids)


# from app import dcatelist

# print(dcatelist)
# from forms import priceq
# from collections import defaultdict

# initprice = 0
# pricerange = 0
# pricedict = defaultdict(list)
# for i in priceq():
#     price = int(i['price'])
#     if pricerange < price:
#         initprice = price
#         pricerange = price + 500
#     pricedict[f'Price Range: {initprice} - {pricerange}'].append(i['id'])


# for key, value in pricedict.items():
#     print(key, value)


# test = '[\'[1, 2]\', [3]]'
# print(str(test).strip('[]\''))
# test1 = test.translate({ord(i):None for i in '[]\''})
# print(test1)

# import re
# email = '@'
# if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
#     print("No")


# from collections import defaultdict
# import json
# import ast
# testdict = {'{"2":"null"}': 1, '{"1"}:"tesst"': 3 }
    
# prr = list(testdict.keys())[0]
# print(prr)
# ss = ast.literal_eval(prr)
# print(ss)
# for key in ss.keys():
#     print(key)

# strr = 'dad 24 141'
# int(s) for s in strr.split() if s.isdigit()
# test = "{'abc': 'def'}"

# testc = ast.literal_eval(test)

# print(testc)
# counter = 'ajjaf12kgk45'
# pids = []
# for n in counter.split():
#     if n.isdigit():
#         pids.append(n)
# print(pids)

# print(counter.split())

# from forms import getAllDictP, displayAllProducts
# import ast

# strr = ['{"3":"XL"}', '{"1":"L"}', '{"4":"M"}', '{"4":"S"}', '{"4":"XL"}', '{"4":"XL"}']
# getdata = getAllDictP(strr)
# # dictstrr = ast.literal_eval(strr)
# counter = {}
# for i in strr:
#             counter[i] = counter.get(i, 0)+1

# dbcounted = []
# for key, value in counter.items():
#     cKey = int(list(ast.literal_eval(key).keys())[0])
#     for row in getdata:
#         if row['id'] == cKey:
#            row.update({ 'size': list(ast.literal_eval(key).values())[0], 'Quantity': value })
#            dbcounted.append(row)
#            print(row)




# print(counter)
# for item in dictstrr:
#     print(list(item.keys())[0])


# from cs50 import SQL
# db = SQL("sqlite:///database.db")
# a = 'test'
# db.execute("BEGIN TRANSACTION")
# db.execute("INSERT INTO cart (userid, firstName, middleName, lastName, mobile ,email, line1, line2, city, province, zip) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", userid=a, firstName=a,
#     midName=a, lastName=a, mobile=a, email=a, address=a, address2=a, city=a, state=a, zipcode=a)

# foo_id = db.last_insert_rowid

# db.execute("COMMIT TRANSACTION")








# import sqlite3

# conn = sqlite3.connect('database.db')

# select = conn.execute("SELECT * FROM products;")
# print(select)

# for row in select:
#     print(row)

# print(conn.lastrowid)

# from cs50 import SQL

# db = SQL("sqlite:///database.db")

# testrow = 'HeySize'
# query = db.execute("INSERT INTO sizes (size) VALUES (?); SELECT last_insert_rowid();", testrow)


# print(query)

# import sqlite3
# connection = sqlite3.connect('database.db')
# cursor = connection.cursor()
# sql = 'INSERT INTO sizes (size) VALUES (?)'
# cursor.execute(sql, (testrow,))
# lastrid = cursor.lastrowid
# connection.commit()

# from cs50 import SQL
# db = SQL("sqlite:///database.db")

# print(db.execute("SELECT * from sizes;"))


# cart = [{"pid": "1", "size": "XL", "sizeid": "2"}, {"pid": "2", "size": "L", "sizeid": "5"}]
# session = {}
# session['cart'] = [{"pid": "1", "size": "XL", "sizeid": "2"}]
# add2cart = {"pid": "1", "size": "XL", "sizeid": "2"}

# def add2cart(crt = session['cart']):
#     if not crt:
#         crt.append(add2cart)
#         print(crt)

#     else:   
#         for i in crt:
#                 if add2cart['pid'] != i['pid'] and add2cart['sizeid'] not in i['sizeid']:
#                     crt.append(add2cart)

#                 else:
#                     i['quantity'] = i.get('quantity', 0) + 1
        

#     print(crt)


# add2cart = {'pid': 1, 'size': 'S', 'sizeid': '2', 'quantity': 1}
# i = {'pid': 2, 'size': 'S', 'sizeid': '2', 'quantity': 1}
# for i in session['cart']:
#         print("Logic Session")

#         if add2cart['pid'] == i['pid'] and add2cart['sizeid'] == i['sizeid']:
#             i['quantity'] = i.get('quantity') + 1

#         else:
#             session['cart'].append(add2cart)

# if add2cart['pid'] == i['pid'] and add2cart['sizeid'] == i['sizeid']:
#     print('yes')

# import json

# strr = '{ "pid" : "1", "size" : "S", "sizeid" : "2" }'

# jsonwf = json.loads(strr)

# print(jsonwf)

# import time

# strrg = {"12-L", "4-S"}

# t0 = time.time()

# pid = ''
# strrglen = len(strrg) - 1
# for j, strr in enumerate(strrg):
#     i = 0
#     while True:
#         if not strr[i] == '-':
#             pid += strr[i]
#             i += 1

#         else:
#             if j != strrglen:
#                 pid += ', '
#             break

# t1 = time.time()
    
# total = t1 - t0

# print(total)

# tn1 = time.time()

# pidn = ''
# for i in str(strrg):
#     if i.isdigit() or i == ',':
#         pidn += i

# tn2 = time.time()
# totaln = tn1 - tn2
# print(totaln)
# print(pidn)


# strr = '12-L'
# rowid = '12'
# test = strr.split('-')


# print(strr.split('-')[0])

# td = {"yo": "d"}

# del td['yo'])

# print(td)

# def abc(*args):
#     test = 'tbc'
#     print(test)
#     print(a)

# a = 'h'
# abc(a)

# from collections import defaultdict
# from cs50 import SQL

# db = SQL("sqlite:///database.db")

# pid = "1"
# q = db.execute("SELECT price FROM products WHERE id = :pid", pid = pid)[0]['price']
# print(q + 5)

# a, b, c = "hi", "go", "lie"
# print(a)

# import sqlite3
    
#Configuring sqlite3
# connection = sqlite3.connect('database.db')
# cursor = connection.cursor()
# import os
# imgdict = {
#     "bimg": "test1bimg",
#     "fimg": "test2fimg",
#     "restimg": "restimg",
#     "restimg": "restimglast"
# }

# joined = {}
# web = '/upload/'
# i = 'upload/'

# print('/' + i)
# from forms import displayAllProducts

# products = displayAllProducts()

# print(products)

# strr = "Price Range: 1500-2000"
# newstr = strr.strip("Price Range:")

# print(newstr)

# qlist = []
# price = {'p.price': '14'}
# cateid = {'p.cateid': '1'}
# p.color = { 'p.color': '1'}

# query = 'SELECT p.id, p.name, p.catename, p.price, p.cateid, p.color FROM products p WHERE '


# tdict = {
#     'thiskey':'34',
#     'thatkey': '98'
# }

# for key, val in tdict.items():
#     print(key)

dictli = {
    'test':'done',
    'test1':'done1'
}

for i, (key, val) in enumerate(dictli.items()):
    print(i)
    print(key, val)
from flask import (Flask, render_template , abort , jsonify , request,
                    redirect, url_for)
# from model import db, save_db
from test2 import show_output,show_data
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("portal.html")

@app.route("/home")
def home():
    return render_template("portal.html")

@app.route("/BKR-BCP-VPN")
def bkr_bcp_vpn():
    results = show_data('BKR-BCP-VPN')
    data_dict = {}
    # for key in results.keys():
    #     data_dict[key] = results[key][1].result
    # data_dict = { results.keys()[i]: results[results.keys()[i]][1].result for i in len((results.keys()))}
    # return render_template("CPU_UTIL2.html", firewalls = data_dict )
    return render_template("CPU_UTIL2.html", firewalls = results.keys() , results = results )
    # return render_template("CPU_UTIL2.html" )

@app.route("/hostname/<name>")
def host_details(name):
    return render_template("host_details.html",name = name)


if __name__ == "__main__":        # on running python app.py
    app.debug = True
    # app.run(debug=True)
    app.run(host="0.0.0.0")



# @app.route("/card/<int:index>")
# def card_view(index):
#     try:
#         card = db[index]
#         return render_template("card.html", 
#                                 card = card , 
#                                 index=index ,
#                                 max_index= len(db) -1 )
#     except IndexError:
#         abort(404)

# @app.route('/add_card', methods = ["GET", "POST"])
# def add_card():
#     if request.method == "POST":
#         card = {"question": request.form['question'],
#                 "answer" : request.form['answer']}
#         db.append(card)
#         save_db()
#         return redirect(url_for('card_view', index = len(db)-1 ))
#     else:
#         return render_template("add_card.html")

# @app.route("/api/card")
# def api_card_list():
#     return jsonify(db)

# @app.route('/api/card/<int:index>')
# def api_card_detail(index):
#     try:
#         return db[index]
#     except IndexError:
#         abort(404)
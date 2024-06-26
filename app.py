from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle
# from flask_cors import CORS, cross_origin
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
model = pickle.load(open('decision_tree.pkl', 'rb'))
@app.route('/')
def fill():
    return render_template('webapp.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gillcolor = float(request.form["gill-color"])
        sporeprintcolor = float(request.form["spore-print-color"])
        population = float(request.form["population"])
        gillsize = float(request.form["gill-size"])
        stalk_root = float(request.form["stalk-root"])
        bruises = float(request.form["bruises"])
        stalkshape = float(request.form["stalk-shape"])

        x = pd.DataFrame({"gill_color": [gillcolor], "spore_print_color": [sporeprintcolor], "population": [population],
                          "gill_size": [gillsize], "stalk_root": [stalk_root], "bruises": [bruises],
                          "stalk_shape": [stalkshape]})
        ml = model.predict(x)
        m = round(ml[0], 2)
        if m == 0:
            g = "poisonous"
        else:
            g = "edible"
        return render_template('webapp.html', result='Your mushroom is {}!'.format(g))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

import numpy as np
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
engine = create_engine("sqlite:///data_college.sqlite")

Base = automap_base()
Base.prepare(engine, reflect = True)

academics = Base.classes.academics


session = Session(engine)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def testing():
    sel = session.query(academics).all()
    otu_list = []
    sample_value_list = []
    sample_dict = {}
    for item in sel:
        selection_dict = item.__dict__
        # otu_list.append(selection_dict["otu_id"])
        ## sample_dict["otu_id"] = otu_list
    # sample_dict["samples_values"] = sample_value_list
    # selection_df = pd.DataFrame.from_dict(sample_dict,orient = "columns",dtype = None)
    # selection_df = selection_df.sort_values(by=["samples_values"],ascending=False)
    print(selection_dict)
    return jsonify(selection_dict)


if __name__ == '__main__':
    app.run(debug=True)
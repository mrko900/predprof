import algorithms
from flask import *


@app.route("/a")
def fixed_date_render_template(dmy):
    kwargs = {}
    data: algorithms.Date = algorithms.dates.get(dmy)
    kwargs["n"] = data.windows_per_floor
    kwargs["house"] = data.data
    return render_template(" .html", **kwargs)

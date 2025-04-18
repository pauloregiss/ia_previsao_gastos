from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    previsao = None
    if request.method == "POST":
        meses = list(map(int, request.form.getlist("mes[]")))
        gastos = list(map(float, request.form.getlist("gasto[]")))
        df = pd.DataFrame({"mes": meses, "gasto": gastos})
        modelo = LinearRegression().fit(df[['mes']], df['gasto'])
        previsao = modelo.predict([[7]])[0]

    return render_template("index.html", previsao=previsao)

if __name__ == "__main__":
    app.run(debug=True)

import flask

# print(flask.__version__)

# экземпляр класса flask
app = flask.Flask(__name__)

# print(__name__) 

# декоратор маршрутизации
@app.route('/')
@app.route("/index")
# логика сервера
def index_page():
    # функция логики страницы index
    return flask.render_template("index.html")

@app.route("/page_1")
def page_1():
    return "PAGE 1"


# конструкция точки входа
if __name__ == "__main__":
    app.run(debug=True)

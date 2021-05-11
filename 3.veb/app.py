from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def hashing(pwd, num_char):
    """
    Функция кэширования
    """
    # кодирование
    byte_str = pwd.encode()
    # хеширование
    hash_str = hashlib.sha256(byte_str)
    # преобразование в строку с 16ми значениями
    if num_char == "-":
        hex_str = hash_str.hexdigest()
    else:
        hex_str = hash_str.hexdigest()[:int(num_char)]

    return hex_str

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/product", methods=["GET", "POST"])
def product_page():
    msg = ""
    if request.method == "POST":
        site_name = request.form.get("site")
        pwd = request.form.get("password")
        num_char = request.form.get("num")

        msg = hashing(site_name + pwd, num_char)

    return render_template("product.html", message=msg)

if __name__ == "__main__":
    app.run(debug=True)
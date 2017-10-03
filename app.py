from flask import Flask, render_template, request, redirect, url_for
import request_engine as re
import pedidos_echo_telegram as pet
import time


app = Flask(__name__)

@app.route('/<int:contato_id>', methods=["GET", "POST"])
def success(contato_id):

    db_conn = re.DbFunctions('quadra_online_requests')
    data = db_conn.obtem_contato_db(contato_id)[0]

    return render_template('sumario_pedido.html', data=data)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        date = request.form['date']
        time = request.form['time']
        location = request.form['autocomplete']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        canal = request.form.get('opcaoCONTATO')

        # Salva o contato no banco de dados
        contato = [date, time, location, name, email, phone, canal]
        db_conn = re.DbFunctions('quadra_online_requests')
        contato_id = db_conn.cria_contato_db(contato)

        # Envia Pedido para o telegram
        msg = "data: {} \n hora: {} \n local: {} \n nome: {} \n email: {} \n telefone: {} \n canal: {} \n id: {}".format(date, time, location, name, email, phone, canal, contato_id)
        pet.send_message(msg, 478992428) #Deuce


        return redirect(url_for('success', contato_id=contato_id))
        #return render_template("sumario_pedido.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    # Cria banco e tabelas caso nao exista
    db_conn = re.DbFunctions('quadra_online_requests')
    db_conn.set_tables()
    #app.debug = True
    app.run(port='5555')

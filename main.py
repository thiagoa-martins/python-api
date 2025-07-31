from flask import Flask, jsonify

app = Flask(__name__)

users_list = {
    1: { 'nome': 'Thiago', 'idade': 27 },
    2: { 'nome': 'Maria', 'idade': 35 },
    3: { 'nome': 'Alexsandra', 'idade': 28 }
}

@app.route('/users')
def users():
    return jsonify(users_list)

@app.route('/user/<int:id>')
def user(id):
    user = users_list.get(id)

    print(user)

    if user:
        return jsonify(user)
    else:
        return jsonify({ 'erro': 'Usuario nao encontrado!' }), 404

if __name__ == '__main__':
    app.run(debug=True)
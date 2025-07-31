from flask import Flask, jsonify, request, blueprints
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/user', methods=['POST'])
def add_user():
    dates = request.get_json()
    new_user = User(name=dates['name'], age=dates['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'mensagem': 'Usuario adicionado!'}),201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append({'id': user.id, 'name': user.name, 'age': user.age})
    return jsonify(result)

@app.route('/user/<int:id>', methods=['DELETE'])
def user(id):
    user = db.session.get(User, id)

    if not user:
        return jsonify({'erro': 'Usuario nao encontrado!'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'mensagem': 'Usuario removido!'}),201

if __name__ == '__main__':
    app.run(debug=True)
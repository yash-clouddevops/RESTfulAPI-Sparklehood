from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
VALID_SEVERITIES = {"Low", "Medium", "High"}

class Ai(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    reported_at = db.Column(db.DateTime(), default=datetime.utcnow)

@app.route('/')
def index():
    return "Hello"

@app.route('/incidents')
def get_incidents():
    incidents = Ai.query.all()
    return jsonify([
        {
            'id': i.id,
            'title': i.title,
            'description': i.description,
            'severity': i.severity,
            'reported_at': i.reported_at.isoformat()
        } for i in incidents
    ]), 200

@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    severity = data.get('severity')

    if not title or not description or not severity:
        return jsonify({'error': 'Title, description, and severity are required.'}), 400

    if severity not in VALID_SEVERITIES:
        return jsonify({'error': 'Severity must be Low, Medium, or High.'}), 400

    incident = Ai(title=title, description=description, severity=severity)
    db.session.add(incident)
    db.session.commit()

    return jsonify({
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity,
        'reported_at': incident.reported_at.isoformat()
    }), 201

@app.route('/incidents/<id>')
def get_incident(id):
    incident = Ai.query.get(id)
    if not incident:
        return jsonify({'error': 'Incident not found.'}), 404

    return jsonify({
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity,
        'reported_at': incident.reported_at.isoformat()
    }), 200

@app.route('/incidents/<id>', methods=['DELETE'])
def delete_incident(id):
    incident = Ai.query.get(id)
    if not incident:
        return jsonify({'error': 'Incident not found.'}), 404

    db.session.delete(incident)
    db.session.commit()
    return '', 204

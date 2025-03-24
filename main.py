from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
teams = [
    {"id": 1, "name": "Mumbai Indians", "city": "Mumbai"},
    {"id": 2, "name": "Chennai Super Kings", "city": "chennai"},
]

# Get all teams
@app.route('/teams', methods=['GET'])
def get_teams():
    return jsonify(teams)

# Create a new team
@app.route('/teams', methods=['POST'])
def create_team():
    new_team = request.json
    new_team["id"] = len(teams) + 1
    teams.append(new_team)
    return jsonify(new_team), 201

if __name__ == '__main__':
    app.run(debug=True)

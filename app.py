import sys
sys.path.append(r'C:\Users\yeswa\OneDrive\Documents\code\04. moringa\01. compulsory_lab\flask-full-crud-api\venv\Lib\site-packages')

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]
next_id=3

def find_event_by_Id(event_id):
    return next((e for e in events if e.id == event_id), None)

@app.route("/")
def home_page():
    return "<h1>This is the Base Route</h1>"

# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    global next_id

    if not request.is_json:
        abort(400, description="The data must be in json")

    data = request.get_json()
    if "title" not in data:
        abort(400, description="The Event must have a title")
    
    new_event = Event(id=next_id, title=data["title"])
    events.append(new_event)
    next_id += 1

    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    
    event = find_event_by_Id(event_id)
    if event is None:
        abort(404, description="Event not found")

    if not request.is_json:
        abort (400, description="The data must be in json")

    data = request.get_json()
    if "title" not in data:
        abort(400, description="The Event must have a title")

    event.title = data["title"]

    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5555)

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

@app.route("/")
def home_page():
    return "<h1>This is the Home Page</h1>"

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    global next_id

    if request.is_json:
        abort(400, description="The data must be in json")

    data = request.get_json()
    if title not in data:
        abort(400, description="The Event must have a title")
    
    new_event = Event(next_id, "FreeCode Camp")
    events.append(new_event)
    next_id += 1

    return jsonify(new_event.to_dict()), 201
    

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    pass

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    pass

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

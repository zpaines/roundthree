from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

start_node = Node("Welcome to #thecloud. If you have not done so already, please call emergency services. Are you safe and able to assist? (y/n)")
start_node.add_response("y", """air""")
start_node.add_response("n", """Leave""")
air_node = Node("Look in your patient's mouth. Are there any obstructions? If there are, remove it if possible. Is the airway now open? (y/n)")
air_node.add_response("y", """B""")
air_node.add_response("n", """heimlich""")
heimlich_node = Node("Perform the Heimlich maneuver: Get behind your patient. Place your fist with your thumb in and facing their belly button. Grasping your fist with your other hand, make quick, upward and inward thrusts with your fist.")
heimlich_node.add_response("y", """B""")
heimlich_node.add_response("n", """h-o CPR""")
breathing_node = Node("Is your patient breathing?")
curr_node = start_node


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    if (curr_node == start_node):
    	resp.message("Welcome to #thecloud. If you have not done so already, please call emergency services. Are you safe and able to assist? (y/n)")
    	curr_node = air_node
    else if (curr_node == air_node):
    	resp.message(air_node.get_message())

    return str(resp)
 
if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0')
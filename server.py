from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import json
from Symbols.U import classify_u_gesture
from Symbols.A import classify_a_gesture
from Symbols.V import classify_v_gesture
from Symbols.B import classify_b_gesture
from Symbols.P import classify_p_gesture


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=["http://127.0.0.1:3000", "http://localhost:5000", "http://127.0.0.1:5000"])

@app.route('/home')  # Define the route for the root URL
def home():
    return render_template('hands.html')

@socketio.on('message')
def handle_message(data):
    if data:  # check if data is not empty
        try:
            # Getting data sent from socket
            originalData = json.loads(data)

            instruction = originalData.get('instructions', None)
            rightLandmarks = originalData.get('rightlandmarks', None)
            leftLandmarks = originalData.get('leftlandmarks', None)
            height = originalData.get('height', None)
            width = originalData.get('width', None)

            # Define a dictionary to act as a switch-case
            switch = {
                'A': classify_a_gesture,
                'B': classify_b_gesture,
                'P': classify_p_gesture,
                'U': classify_u_gesture,
                'V': classify_v_gesture,
                # Add your cases here
            }

            # Use the switch-case dictionary
            function_to_execute = switch.get(instruction, None)
            if function_to_execute:
                gesture, accuracy, correct1, correct2 = function_to_execute(rightLandmarks, leftLandmarks, height, width)
                emit('message', {'gesture': gesture, 'accuracy': accuracy, 'correct': correct1, 'correct2' : correct2 })

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    socketio.run(app)
from flask import Flask, request, jsonify

app = Flask(__name__)
dialogue_manager = DialogueManager()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data['query']
    chatbot_response = dialogue_manager.process_query(user_query)
    dialogue_manager.update_context(user_query, chatbot_response)
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)

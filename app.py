import pickle
from flask import Flask, request, jsonify, render_template


with open('./models/model_mnb.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('./models/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check-spam', methods=['POST'])
def check_spam():
    try:
        data = request.get_json()

        if (not data) or ('message' not in data):
            return jsonify({'error': 'Message content is missing'}), 400

        message = data['message']
        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)[0]
        return jsonify({'prediction': bool(prediction)})

    except Exception as e:
        return jsonify({'error': f'{e}'}), 500


if __name__ == '__main__':
    app.run(debug=True)

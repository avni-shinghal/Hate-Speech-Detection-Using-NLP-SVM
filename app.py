from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the trained SVM model
model = joblib.load('svm_model.pkl')

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the text input from the request
    text = request.json['text']

    try:
        # Make prediction
        prediction = model.predict([text])[0]
        
        # Return the prediction as JSON response
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

import joblib

# Load the trained SVM model
svm_model = joblib.load('svm_model.pkl')

# Function to make predictions using the SVM model
def predict_hate_speech(text):
    # Assuming 'text' is the input text to be classified
    # You may need to preprocess 'text' before passing it to the model
    
    # Make prediction using the loaded SVM model
    prediction = svm_model.predict([text])[0]
    
    # Return the predicted class (e.g., 0 for non-hate speech, 1 for hate speech)
    return prediction

# Example usage:
text_to_classify = "Bitch."
predicted_class = predict_hate_speech(text_to_classify)
print("Predicted class:", predicted_class)

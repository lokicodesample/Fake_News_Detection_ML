from flask import Flask, request, render_template, jsonify
import pickle
import joblib

app = Flask(__name__)


# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# loaded_vectorizer
loaded_vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    print(text)
    text_vectorized = loaded_vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    print(prediction)

    if prediction[0] == 0:
        print("Output:" + " The article is classified as fake news.")
        Output = "The article is classified as Fake news."
    else:
        print("Output:" + " The article is classified as real news.")
        Output = "The article is classified as Real news."
    #return render_template('index.html', prediction=Output)
    return jsonify({'prediction': Output})

if __name__ == '__main__':
    app.run(debug=True)

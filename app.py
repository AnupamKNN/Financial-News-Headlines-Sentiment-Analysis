import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the sentiment analysis model from the pickle file
with open('Headlines Model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['news_headlines']
        
    # Assuming model.predict() returns a sentiment prediction
    prediction = model.predict([text])

    if prediction < 0.0:
        sentiment = 'Negative'
    elif prediction == 0.0:
        sentiment = 'Neutral'
    else:
        sentiment = 'Positive'

    return render_template('index.html', prediction_text=sentiment)
    
if __name__ == '__main__':
    app.run(debug=True)

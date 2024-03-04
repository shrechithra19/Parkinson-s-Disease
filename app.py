from flask import Flask, render_template, request
import librosa
import numpy as np

app = Flask(__name__)

# Function to extract audio features and perform diagnosis
def diagnose_parkinsons(audio_file):
    try:
        # Load the audio file
        x, sample_rate = librosa.load(audio_file, sr=None)
        # Extract features from the audio
        mfcc = np.mean(librosa.feature.mfcc(y=x, sr=sample_rate, n_mfcc=50).T, axis=0)
        # Perform diagnosis (dummy example, replace with your diagnosis logic)
        # For demonstration purposes, let's assume Parkinson's is diagnosed if the mean of mfcc features is above a threshold
        if np.mean(mfcc) > 0.5:
            return "Patient is suspected to be suffering from Parkinson's disease."
        else:
            return "No signs of Parkinson's disease detected in the patient."
    except Exception as e:
        return str(e)

# Route to display the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and display diagnosis result
@app.route('/upload', methods=['POST'])
def upload():
    if 'audioFile' not in request.files:
        return "No audio file uploaded"
    
    audio_file = request.files['audioFile']
	
    print("Audio file is fetched successfully")
    
    if audio_file.filename == '':
        return "No selected file"
    
    # Process the audio file and perform diagnosis
    result = diagnose_parkinsons(audio_file)
    
    return result

if __name__ == '__main__':
    app.run(debug=True)

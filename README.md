# Recommendation_system_for_telemedicine_industry
A project that uses fundamental similarity algorithms in NLP to dissect common patterns across drugs and recommend similar alternatives.

# Explanation:
Telemedicine applications may have cases where a prescription that was given by doctor maybe out of stock. In such cases having a alternative is better. This application helps you find the alternative of medicine that is already in the list of medicines in medicines.csv based on symptoms and the treatment medicine does. While the suggestio may not be a 100% replacement, it gives patient a better idea of where to look and which tablets can be a beteer alternative.
The application is developed using the most fundamental and effective recommender solution for text based data whic is Cosine similarity search. This technique is highly effective not only in text similarity analysis across various industries but is also relied upon in military applications and signal analysis. It is used in addition to TF-IDF for document (tabluar or non-tabular) similarity analysis.

You can use the project by following the following guideline:

### 1. Clone the repository (In your editor in the desired directory, type:)
```sh
git clone https://github.com/Fai3Z/Recommendation_system_for_telemedicine_industry.git
```

### 2. Next get the weights file
Weights file is necessary for model to make inference on the data as it contains the learned patterns as weights. Since my repository does not have enough bandwidth to accomodate this large .pkl file i have uploaded it on Google cloud. You can download it using the folloiwng links. (The colab notebook is also available for additional experiments and analysis)
```sh
weights:
https://drive.google.com/file/d/1-0U_eYTexXwFXLzFBu86lVQmyfw7t38X/view?usp=drive_link
https://drive.google.com/file/d/1W4olp87x-O10cKm7HMjFPNtvIQxTARRa/view?usp=drive_link
Notebook:
https://colab.research.google.com/drive/1_2MOOOhBxuixfjSULvQO8OTA306Bty1h?usp=drive_link
```
## Note: Make sure the weights are in the same directory where the files have been cloned i.e in same directory as the requirements.txt file

### 3. create virtual environment and install the required dependencies
Use
```sh
python -m venv env
env\Scripts\activate

pip install -r requirements.txt
```

### 4. Run the app.py file
The flask server will run the application on http://127.0.0.1:5000/

### Expected Output
![Description of Image](https://github.com/Fai3Z/Recommendation_system_for_telemedicine_industry/blob/main/output1.png?raw=true)
![Description of Image](https://github.com/Fai3Z/Recommendation_system_for_telemedicine_industry/blob/main/output2.png?raw=true)



# select appropriate pyton interpreter by going to command palette (ctrl+shift+p) and selecting "Python: Select Interpreter"
# dataset link: https://www.kaggle.com/datasets/talhasattar727/pakistan-pharmaceutical-dataset?resource=download

# https://ailaaj.pk/collections/medicine?page=13&sort_by=title-ascending
# scrape name, generic category, and ingredients
# make csv convert to DF and remove nulls and then train model

from flask import Flask, request, render_template
import pickle
import pandas as pd

# ensuring ML algorithm is self made and least imports needed

app = Flask(__name__)

medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict) # medicine list stored from the.pkl file (as dataset file named medicine_dict.pkl) we saved and pass it to the jinja template in index.html file
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(medicine): # logic for display pipeline (similar to colab part)
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    selected_medicine_name = None
    if request.method == 'POST':
        selected_medicine_name = request.form['medicine'] # name=medicine attribute passed to "recommend" function which will give recommendation
        recommendations = recommend(selected_medicine_name)
        # pass relevant data to index.html to return relevant values in frontend
    return render_template('index.html', medicines=medicines['Drug_Name'].values, recommendations=recommendations, selected_medicine_name=selected_medicine_name) # "recommedations" is list

if __name__ == '__main__':
    app.run(debug=True)
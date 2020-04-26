# Reddit-Flare-Detector-IIIT_Delhi-task
Link to App is:
A Reddit Flair Detector web application to detect flairs of India subreddit posts using Machine Learning algorithms. 
The application link is https://flare-app.herokuapp.com/

Directory Structure
The directory is a Flask web application set-up for hosting on Heroku servers. The description of files and folders can be found below:

script.py - The file used to start the app.
requirements.txt - Containing all Python dependencies of the project.
Procfile - Needed to setup Heroku.
website - Folder containing the master settings of Django application.
index.html - HTML file to run web app
result.html - HTML file to run web app
reddit-india-flair-detector-IIIT Midas project - Jupyter notebook for downloading data from reddit and predicting the flairs.
reddit-india-data.csv - CSV file of the collected data.
finalised_model.sav - Link to finalised_model.sav file.
The entire code has been developed using Python programming language and the application has been developed using Flask web framework and hosted on Heroku web server.

Project Execution
Open the Terminal.
Clone the repository by entering git clone https://github.com/Ayush-54/Reddit-Flair-Detector-IIIT_Delhi-task.git.
Ensure that Python3 and pip is installed on the system.
Create a virtualenv by executing the following command: virtualenv -p python3 env.
Activate the env virtual environment by executing the follwing command: source env/bin/activate.
Enter the cloned repository directory and execute pip install -r requirements.txt.
Now, execute the following command: python manage.py runserver and it will point to the localhost with the port.
Hit the IP Address on a web browser and use the application.
Dependencies
The following dependencies can be found in requirements.txt:

praw
pandas 
datetime
sklearn
matplotlib.pyplot 
numpy 
seaborn 
bs4 
sklearn.pipeline 
import nltk
import pickle
The Approach taken for the task is as follows:

Collect 500 India subreddit data for each of the 12 flairs.
The data includes title, comments, body, url, author, score, id, time-created and number of comments.
Five types of features are considered for the the given task:
a) Title
b) Comments
c) Urls
d) Body.
The dataset is split into 70% train and 30% test data using train-test-split of scikit-learn.
The dataset is then converted into a Vector and TF-IDF form.
Then, the following ML algorithms (using scikit-learn libraries) are applied on the dataset:
a) Naive-Bayes
b) Random Forest
c) MLP
The best model is saved and is used for prediction of the flair from the URL of the post.
# References
https://www.storybench.org/how-to-scrape-reddit-with-python
https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
https://towardsdatascience.com/designing-a-machine-learning-model-and-deploying-it-using-flask-on-heroku-9558ce6bde7b

from flask import Flask, escape, request, render_template, url_for
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
import pickle
vector = pickle.load(open("vectorizer.pkl",'rb'))
model = pickle.load(open("finalized_model.pkl",'rb'))

app = Flask(__name__)
@app.route('/')
def home():
    # return "hellow, flask1!"
    return render_template("index.html")


@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method =="POST":
        # news = str(request.form['news'])
        news = (request.form['news'])
        print(news)

        # predict = model.predict(vector.transform([news]))[0]
        predict = model.predict(vector.transform([news]))
        print(predict)

        if (predict == 0):{
             print('The news in Real')
        }
        else:{
            print('The news is Fake and Unreliable')
        }
       
        
        return render_template("prediction.html", prediction_text="News headline is -> {}".format(predict))

    else:
        return render_template("prediction.html")



if __name__ == '__main__':
        app.run(debug=True)
    #   from waitress import serve
    #   serve(app, host="0.0.0.0", port=8080)

from flask import Flask, request
import pickle

api=Flask(__name__)

model=pickle.load(open("model.sav","rb"))

@api.route("/score_predictor",methods=["GET"])
def predict():
	request_json=request.get_json()
	score=model.predict([[request_json['wicket'],request_json['overs']]])[0][0]
	return "Score will be- {}".format(str(int(score)))


if __name__=="__main__":
	api.run(host="0.0.0.0", port=9999)
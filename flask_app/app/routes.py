from app import app
from flask import render_template,jsonify,request


#UI ROUTES
@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        #custom_exception=CustomerException(e,sys)
        #logging.info(custom_exception.error_message)
        #logging.info('Exception occured...')
        return str(e)



#API ROUTES
@app.route('/api/predict', methods=['POST'])
def api_result():
    if request.method=='POST':
        myid=request.json['MyId']
        myname=request.json['MyName']
        myage=request.json['MyAge']

        myresponse=str(myid)+str(myname)+str(myage)

        """
        try:
  80         if (request.method=='POST'):                                                                          
  81             var1=float(request.json["VARIABLE1"]) #var1--float
  82             var2=int(request.json["VARIABLE2"]) #var2--int
  83             var3=request.json["VARIABLE3"]  #var3--string
  84     except Exception as e:
  85         logging.exception("Exception while reading data from api request: /api/make_prediction :"+str(e))
  86     
  87     #prepare the payload to send to backend Function for prediction
  88     payload=[var1, var2, var3]
  89     
  90     #call the backend function to load model, use payload, make prediction and return the predicted value here     .
  91     result=backendFnToReturnPredictedValues(payload)
  92     
  93     #return result to API
  94     return jsonify(result.tolist()) #convert the result to list as model give output in the form of ndarray or      dataframe
        """

        return jsonify(myresponse)


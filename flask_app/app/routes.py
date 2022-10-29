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

        return jsonify(myresponse)


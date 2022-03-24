from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
                 "MY favorite Tree" : "Mango",
        }
  
        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True)

from flask import Flask,request,render_template

app= Flask(__name__)


# Route
@app.route("/")

def hello_world():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return "Sumit Kumar Welcome you"
    

@app.route('/demo',methods=['POST'])
def math_operations():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']

        if operation=="add":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "division":
            result = num1/num2
        else:
            result=num1-num2        
        return "The operation is{} and the result is {}".format(operation,result)   
    
@app.route('/operation',methods=['POST'])
def operation():
    if(request.method=='POST'):
        operation=(request.form['operation'])
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])

        if operation=="add":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1/num2
        else:
            result=num1-num2        
        return render_template('results.html',result=result)





# @app.route('/math', methods=['POST'])  # This will be called from UI
# def math_operation():
#     if (request.method=='POST'):
#         operation=request.form['operation']
#         num1=int(request.form['num1'])
#         num2 = int(request.form['num2'])
#         if(operation=='add'):
#             r=num1+num2
#             result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
#         if (operation == 'subtract'):
#             r = num1 - num2
#             result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
#         if (operation == 'multiply'):
#             r = num1 * num2
#             result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
#         if (operation == 'divide'):
#             r = num1 / num2
#             result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
#         return render_template('results.html',result=result)
    
# @app.route('/multiply',methods=['POST'])
# def multiply_operations():
#     if(request.method=='POST'):
#         operation=request.json['operation']
#         num1=request.json['num1']
#         num2=request.json['num2']
#         result = num1 * num2

#         return "The operation is{} and the result is {}".format(operation,result) 
      

# @app.route('/division',methods=['POST'])
# def mdivision_operations():
#     if(request.method=='POST'):
#         operation=request.json['operation']
#         num1=request.json['num1']
#         num2=request.json['num2']
#         result = num1 / num2

#         return "The operation is{} and the result is {}".format(operation,result)



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
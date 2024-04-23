from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
   return("Hello Belagavi Friends.....")

print(__name__)
if __name__ =="__main__":
   print("Inside IFFF.....")
   app.run(host='0.0.0.0',debug=True)
  

from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS = [
  { 'id' : 1 ,
    'title' : 'Data Analyst',
    'location': 'Delhi, India'
  },
  { 'id' : 2 , 
    'title' : 'Data Engineer',
    'location': 'Bengaluru, India',
    'salary' : 'Rs. 50,00000'
  },
{ 'id' : 3 ,
  'title' : 'Data Scientist',
  'location': 'Bengaluru, India',
  'salary' : 'Rs. 70,00000'
},
{ 'id' : 4 ,
  'title' : 'Backend Engineer',
  'location': 'Bengaluru, India',
  'salary' : 'Rs. 90,00000'
}
  
]
@app.route("/")
def hello_world():
    return render_template('home.html', 
                          jobs=JOBS, company_name = 'JK Data')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

print(__name__)
if __name__ =="__main__":
   print("Inside IFFF.....")
   app.run(host='0.0.0.0',debug=True)
  

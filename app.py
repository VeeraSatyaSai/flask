from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
@app.route("/<filename>")
def index(filename="file1"):
  lines=[]
  if (filename=="file2" or filename=="file4"):
  
    with open(".//"+filename+".txt","r",encoding='utf-16') as file:
       for line in file:
         lines.append(line)
    return render_template('index.html',filename=lines)
  
  elif(filename=="file1" or filename=="file3"):
    with open(".//"+filename+".txt","r",encoding='utf-8') as file:
       for line in file:
         lines.append(line)
    return render_template('index.html',filename=lines)
      

if __name__ == "__main__":
    app.run(debug=True)
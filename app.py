from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
@app.route("/<string:filename>")
def index(filename="file1"):
 try:
 
   start=(request.args.get('start'))
   end=(request.args.get('end'))
  
  

   lines=[]
   if (filename=="file2" or filename=="file4"):
    
  
     with open(".//"+filename+".txt","r",encoding='utf-16') as file:
       for line in file:
         lines.append(line)
       if start==None:
          start=0
       else:
          start=int(start)
          start-=1
       if end==None:
          end=len(lines)
       else:
          end=int(end)
       if start > end:
         return "Invalid Query Parameters"
        
     return render_template('index.html',filename=lines[start:end])

    
  
   elif(filename=="file1" or filename=="file3"):
    with open(".//"+filename+".txt","r",encoding='utf-8') as file:
       for line in file:
         lines.append(line)
       if start==None:
          start=0
       else:
          start=int(start)
          start-=1
       if end==None:
          end=len(lines)
       else:
          end=int(end)
       if start > end:
         return "Invalid Query Parameters"
 
    return render_template('index.html',filename=lines[start:end])
   else:
    return "File doesn't exist"
 except Exception as e:
    
    return "Invalid Query Parameters"
 
 
 

@app.errorhandler(404)
def someError(e):
    return render_template('error.html')
@app.errorhandler(500)
def error(e):
    return "file name entered doesn't exist"


      

if __name__ == "__main__":
    app.run(debug=True)
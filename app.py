from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
@app.route("/<string:filename>")
#Below function will run for both of the above url paths
def index(filename="file1"):
 try:
   #Extracting values from query parameters
   #If query parameters were not present in url it will return None 
   start=(request.args.get('start'))
   end=(request.args.get('end'))
   lines=[]
   if (filename=="file2" or filename=="file4"):
     with open(".//"+filename+".txt","r",encoding='utf-16') as file:
       for line in file:
         #adding each line to list
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
       if start > end or start ==end:
         return render_template('differenterror.html',error="Invalid Query Parameters")
       elif end > len(lines):
          return render_template('differenterror.html',error="length of file exceeded")
       elif start<0 or end <0:
          return render_template('differenterror.html',error="Invalid Query Parameters")         
     #passing the list of lines to the filename variable in the index.html  
     return render_template('index.html',filename=lines[start:end])

    
  
   elif(filename=="file1" or filename=="file3"):
    with open(".//"+filename+".txt","r",encoding='utf-8') as file:
       for line in file:
        #adding each line to list
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
       if start > end or start==end :
         return render_template('differenterror.html',error="Invalid Query Parameters")
       elif end > len(lines):
          return render_template('differenterror.html',error="length of file exceeded")
       elif start<0 or end <0:
         return render_template('differenterror.html',error="Invalid Query Parameters")
    #passing the list of lines to the filename variable in the index.html  
    return render_template('index.html',filename=lines[start:end])
   else:
    #if wrong filename was given in the url parameters the differenterror.html will be rendered
    return  render_template('differenterror.html',error="File doesn't exist")
    #if error occurs in try block then except block will be executed
 except Exception as e:
    #if query parameters given were invalid then the except block will run and this return html will be rendered
    return render_template('differenterror.html',error="Invalid Query Parameters")
 
 
 
#if url path given was wrong this function will run
@app.errorhandler(404)
def someError(e):
    return render_template('error.html')



      

if __name__ == "__main__":
    app.run(debug=True)
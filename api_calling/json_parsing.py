
# https://jsonplaceholder.typicode.com/posts
import requests
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Walden0042$$",
  database="authentication"
)

def getPosts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        if response.status_code==200:
            
            json = response.json()
            
            mycursor = mydb.cursor()
            
            for x in json:
                
                sql = "insert into from_server (title,body) values (%s,%s)"
                val = (x['title'], x['body'])
                mycursor.execute(sql, val)
                mydb.commit()
                
        else:
            print("Failed to retrieve data")
            
    except:
        print("Error: Unable to connect to the server.")

getPosts()        
        


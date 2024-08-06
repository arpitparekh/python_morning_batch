
# https://jsonplaceholder.typicode.com/posts
import requests

def getPosts():
    url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
    
    try:
        response = requests.get(url)
        
        if response.status_code==200:
            json = response.json()
            
            print(json[0]['title'])
            print(json[0]['body'])
            
        else:
            print("Failed to retrieve data")
            
    except:
        print("Error: Unable to connect to the server.")
        


getPosts()        
        


from flask import Flask #Took reference from geeksforgeeks that how does
                        #flash app works. 
from datetime import datetime

#Flask constructor 
app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date time: {current_time}" #returning the date and time here

#main driver function
if __name__ == '__main__':
    app.run(debug=True)



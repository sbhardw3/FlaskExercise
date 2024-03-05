from flask import Flask, request #Took reference from geeksforgeeks.com

app = Flask(__name__)

#function which calculates whether the number is odd or even 
def check_number(num):
    try:
        num = int(num)
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except ValueError:
        return "Not an integer"
    
#extracting home.html fromm route() function and defining a function home()
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': #requesting number from user 
        number = request.form['number']
        return calculate_result(number) #calling function to check whether odd/even number 
    return open("home.html").read()

def calculate_result(number):
    result = check_number(number)
    return open("result.html").read().format(number, result) #This what i explained in the html file

if __name__ == '__main__':
    app.run(debug=True)

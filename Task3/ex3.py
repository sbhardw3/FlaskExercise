from flask import Flask, request, redirect
#This program taught me many things i took help from chatgpt for this and 
#geeksforgeeks website. This was very difficult exercise for me personally

app = Flask(__name__)

# Dictionary to store registered users
registered_users = {}

# List of student organizations
organizations = ['Organization A', 'Organization B', 'Organization C', 'Organization D',]


#Defining the home function so that whenever user enters the data it is recorded 
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        #If the organization is in the dictionary then redirecting the user to the 
        #register user side 
        if name.strip() != '' and organization in organizations:
            registered_users[name] = organization
            return redirect('/registered_users')
    #This is was very tricky part here i opened and read the home.html
    #then i didn't knew how will i pass the values of the organization to the html page
    #i used replace and join method here i am taking organization from the above list i listed 
    #and then putting it in the html 
    home_content = open("home.html").read()
    home_content_with_orgs = home_content.replace("Select an organization", "\n".join([f'<option value="{org}">{org}</option>' for org in organizations]))
    return home_content_with_orgs


@app.route('/registered_users')
def registered_users_list():
    with open("registered_users.html", "r") as f:
        content = f.read()
    #Here i am creating the table using table tags because this is how i will pass the organization and names 
    #that the user entered 
    users_table = '<table class="table table-striped table-bordered"><thead class="thead-dark"><tr><th scope="col">Name</th><th scope="col">Organization</th></tr></thead><tbody>'
    #using a for loop to collect of the data from the registered_user array
    for name, organization in registered_users.items():
        users_table += f'<tr><td>{name}</td><td>{organization}</td></tr>'
    users_table += '</tbody></table>'
    content_with_users = content.replace("{% users_table %}", users_table)
    return content_with_users

if __name__ == '__main__':
    app.run(debug=True)

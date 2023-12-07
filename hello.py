# INF601 - Advanced Programming in Python
# Lisa Thoms
# Mini Project 3



#(5/5 points) Proper import of packages used.
#(70/70 points) Using Flask you need to setup the following:
#(20/20 points) You need to have a minimum of 5 pages, using a proper template structure.
#(10/10 points) You need to have at least one page that utilizes a form and has the proper GET and POST
# routes setup.
#(10/10 points) You need to setup a SQLlite database with a minimum of two tables, linked with a
# foreign key.
#(5/5 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(5/5 points) I will be checking out the master branch of your project. Please be sure to include
# a requirements.txt file which contains all the packages that need installed. You can create this
# fille with the output of pip freeze at the terminal prompt.
#(10/10 points) There should be a README.md file in your project that explains what your project
# is, how to install the pip requirements, and how to execute the program. Please use the GitHub
# flavor of Markdown. Be thorough on the explanations. You will need to explain the steps of
# initializing the database and then how to run the development server for your project.


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
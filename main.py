from website import create_app

app = create_app()

# run flask application
if __name__ == '__main__':
    # if line means that only if we run this file, not if we import this file we are going to execute the following line
    app.run(debug=True)  # startup a web server. debug=True means that anytime we make a change to any python code its going to rerun the web server


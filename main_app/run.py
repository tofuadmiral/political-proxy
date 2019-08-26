from flask import Flask
app = Flask(__name__)
@app.route('/')


from templates import app
# Load this config object for development mode
app.config.from_object('configurations.DevelopmentConfig')


# actual content of page 
def hello_world():
    return 'Hello to the World of Flask!'
if __name__ == '__main__':
    app.run()
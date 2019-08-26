from flask import Flask 
app = Flask(__name__) # this is the app variable which uses the __init__.py script
                      # so it's also part of the app package

# this references the app package
# routes done at bottom bc it needs to import app too
from app import routes

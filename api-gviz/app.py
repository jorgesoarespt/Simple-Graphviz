import os
import logging
import pydot
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err) 
    #return string(err), 500
    return jsonify(err.to_dict()), 500

#we define the route /
@app.route('/')

def healthcheck():
    # return a json
    return jsonify({'name': 'api-gviz', 'status': 'available'})

@app.route('/gviz/',methods = ['POST'])
def graphs():
    # Check if an ID was provided as part of the URL.  
    request_data = request.get_json()

    if request_data:
        if 'dot' in request_data:
            # Get the dot string from the request
            dot_string = request_data['dot']
            #Add the graph to the Graphiz object
            graphs = pydot.graph_from_dot_data( dot_string )
            #Parse the dot to svh
            svg_string = graphs[0].create_svg()  
            #Set encoding for response
            encoding = 'utf-8'
            app.logger.info("Sucessfull response")
            return jsonify({'svg': svg_string.decode(encoding)})                      
        else:
            app.logger.warning("Incorrect payload")
            return "Incorrect payload", status.HTTP_400_BAD_REQUEST
    else:
            app.logger.warning("Incorrect payload")
            return "Incorrect payload", status.HTTP_400_BAD_REQUEST    

if __name__ == '__main__':
    app.logger.info(str('--------------------------------------------'))
    app.logger.info('api-gviz started')
    app.logger.info(str('--------------------------------------------'))
    #define the localhost ip and the port that is going to be used
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
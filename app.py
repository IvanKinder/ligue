import yaml
from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/playbooks', methods=['GET'])
def func_test():
    response = {}
    data = []

    try:
        with open('playbooks/ansible-playbook.yml', 'r') as playbook:
            services = yaml.load(playbook, Loader=yaml.FullLoader)
            for service in services:
                for task in service['tasks']:
                    data.append(task)
        response['data'] = data
    except Exception as e:
        response['data'] = str(e)

    return jsonify(response)


if __name__ == '__main__':
    app.run()

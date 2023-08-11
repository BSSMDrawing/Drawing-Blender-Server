from flask import Flask, request, json, send_file
import subprocess

app = Flask(__name__)

@app.route('/stl-modeling', methods=['POST'])
def stl_decode():
    code = open('modeling.py', 'w')
    sample = open('export-sample.py', 'r+')
    command = json.loads(request.get_data())
    code.write(command['gpt_response'] + "\n")
    code.write(sample.read())
    code.close()
    return send_file('sample.stl')
    #subprocess.run(["~/blender/blender","-b","-P","modeling.py"])

if __name__ == '__main__':
    app.run(host='192.168.1.46')

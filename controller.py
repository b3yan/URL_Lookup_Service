from flask import Flask, request
from application.db_actions import get, update, insert

application = Flask(__name__)
@application.route('/urlinfo/1/<hostname_and_port>/<original_path_and_query_string>')
def get_url(hostname_and_port, original_path_and_query_string):
    malware_info = get(hostname_and_port)
    if not malware_info: malware_info = "not malware"
    return malware_info

@application.route('/urlinfo', methods = ['POST'])
def save_url():
    url = request.form['url']
    malware_info = request.form['malware_info']
    return insert(url, malware_info)
    #test
     #test
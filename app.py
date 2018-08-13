import csv
import load
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

#def newApp():



def newApp():
	app = Flask(__name__)

	applist = load.loader('190titles.csv')
	apptrie = load.listsuggestions(applist)
	@app.route('/', methods=['GET'])
	def listall():
		prefix = request.args.get('q', '')
		fullList = apptrie.suggest(prefix)
		output = {
			'total': len(fullList),
			'results': fullList
			}
		return jsonify(output)

	@app.route('/output', methods=['POST'])
	def wordsuggest():
		req_data = request.get_json()
		prefix = req_data["prefix"]
		apps_suggest = apptrie.suggest(prefix)
		output = {
			'total': len(apps_suggest),
			'results': apps_suggest
			}
		return jsonify(output)

	#app.run(host="127.1.1.1", port=6000, debug=True, load_dotenv=True)

	return app

if __name__ == '__main__':
	newApp()
	
	


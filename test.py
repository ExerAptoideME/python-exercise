import unittest
import json
import logging
from app import newApp

class Apptest(unittest.TestCase):

	def setUp(self):
		self.app = newApp()
		self.client = self.app.test_client()

	def test_client(self):
		response = self.client.get('/')
		return "Result: " + str(response)

	def test_can_get_suggestions(self):
		question = "{ \"prefix\" : \"Fac\" }"
		# response = self.client.post('/output?q=Fac')
		response = self.client.post(question)
		suggestions = json.loads(response.data)['results']
		logging.info('1')
		logging.info(suggestions)
		expected_suggestions = [
			    'Facebook',
			    'Facebook Lite',
			    'Facebook Pages Manager'
			]
		self.assertListEqual(suggestions, expected_suggestions)



if __name__ == '__main__':
	unittest.main()



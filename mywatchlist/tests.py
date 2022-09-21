from django.test import TestCase
from django.urls import reverse  

# Create your tests here.
class HomepageTests(TestCase):
    def testingHTML(self):
        response = self.client.get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)

    def testingJson(self):  
        response = self.client.get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)

    def testingXML(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)

    
import unittest
import json

from unittest.mock import patch
from src.form_generator import FormGenerator

class TestFormGenerator(unittest.TestCase):

    def setUp(self):
        with open('tests/fixtures/example_config.json') as config:  
            self.config = json.load(config)
        
        with open('tests/fixtures/simple_form.json') as simple:  
            self.simple = json.load(simple)
        
        with open('tests/fixtures/nasty_form.json') as nasty:  
            self.nasty = json.load(nasty)

    def test_creates_simple_form(self):
        expected = '<form><div><label for="name">Name</label><input class="form-input" id="form-name" name="name"></div></form>'
        client = FormGenerator()
        html = client.process(self.simple)
        self.assertEqual(html, expected)

    def test_escapes_nasty_form(self):
        expected = '<form><div><label for="name">&lt;script&gt;something bad&lt;/script&gt;</label><input class="form-input" id="form-name" name="name"></div></form>'
        client = FormGenerator()
        html = client.process(self.nasty)
        self.assertEqual(html, expected)

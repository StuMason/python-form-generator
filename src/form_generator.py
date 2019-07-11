import dominate

from dominate.tags import *

class FormGenerator:

    def process(self, config):
        html = form()
        for input_config in config['inputs']:
            if input_config['type'] == 'text':
                with html:
                    self.generate_text_input(input_config)
            

        return html.render(pretty=False)

    def generate_text_input(self, input):
        html = div()
        with html:
            label(input['label'], _for=input['name'])
            input_(name=input['name'],
                    id=input['id'],
                    _class=input['classes'])

        return html
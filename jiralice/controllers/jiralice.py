from base import BaseController
from models.jiralice_helper import JiraliceHelper


class JiraliceController(BaseController):

    def __init__(self, *kwargs):
        super(JiraliceController, self).__init__(*kwargs)
        self.jiralice_helper = JiraliceHelper(params=self.json_params)

    def create_ticket(self):
        return self.jiralice_helper.create_ticket()

import matrix_ansible_tower_bot
from unittest import TestCase
import json
# import settings

headers = {'content-type': 'application/json'}


class MyTestCase(TestCase):

    def setUp(self):
        matrix_ansible_tower_bot.app.testing = True
        self.app = matrix_ansible_tower_bot.app.test_client()

    def test_home(self):
        # result = self.app.get('/')
        self.app.get('/')

    def test_is_dict_matrix_tokens(self):
        return True

    def test_is_dict_matrix_rooms(self):
        return True

    def test_call_token_not_provided(self):
        response = self.app.post(
            '/',
            # data=json.dumps({'a': 1, 'b': 2}),
            headers=headers
        )
        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 403
        assert not data['success']
        assert data['reason'] == 'token not provided'

    def test_call_token_not_valid(self):
        response = self.app.post(
            '/?token=badtoken',
            # data=json.dumps({'a': 1, 'b': 2}),
            # params=params,
            # params="{'ACCESS_TOKENS': 'thisISaSAMPLEtoken'}",
            headers=headers
        )
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 403, response)
        self.assertFalse(data['success'])
        self.assertTrue(data['reason'], 'token not valid')

    def test_function_validate_token_valid(self):
        self.assertTrue(matrix_ansible_tower_bot.validate_token('thisISaSAMPLEtoken'))

    def test_function_validate_token_not_valid(self):
        self.assertFalse(matrix_ansible_tower_bot.validate_token('badtoken'))

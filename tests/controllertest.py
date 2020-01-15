import unittest

from Controller.app import app


class TestController(unittest.TestCase):
    name = "TestController"

    def setUp(self) -> None:
        app.config['TESTING'] = True

        with app.test_client() as client:
            self.client = client

    def tearDown(self) -> None:
        pass

    def test_api_prefix(self):
        resp = self.client.get('/ping')
        self.assertTrue(b'The page requested does not exist' in resp.data)

        resp = self.client.get('/api/ping')
        self.assertTrue(b'The page requested does not exist' not in resp.data)

        resp = self.client.get('/upload')
        self.assertTrue(b'The page requested does not exist' in resp.data)

        resp = self.client.get('/api/upload')
        self.assertTrue(b'The page requested does not exist' not in resp.data)

        resp = self.client.get('/nonexistent')
        self.assertTrue(b'The page requested does not exist' in resp.data)

        resp = self.client.get('/api/nonexistent')
        self.assertTrue(b'The page requested does not exist' not in resp.data)

    def test_upload(self) -> None:
        handle = open('../Example_Sequence_Files/difficult_johannes.fasta', 'rb')
        response = self.client.post('/api/upload', content_type='multipart/form-data', data={'seqfile': handle})
        searchResult = eval(response.data)              #Don't do this in production code, kids! (It's okay here since our own mock data is generally trusted)
        expectedCount = 0
        for result in searchResult["result"]:
            for offer in result["offers"]:
                expectedCount = expectedCount + 1

        self.assertEqual(expectedCount, searchResult["count"], "Mismatch between declared and actual result count!")


if __name__ == '__main__':
    unittest.main()

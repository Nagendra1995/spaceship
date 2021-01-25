import json

from django.test import TestCase


class PlayerTesting(TestCase):
    Create_spaceship = '/spaceship/AddSpaceship'
    Delete_spaceship = '/spaceship/DelSpaceship'
    Delete_Location = '/spaceship/DelLocation'
    Add_Location = '/spaceship/Addlocation'
    Update_status = '/spaceship/UpdateStatus'
    travel = '/spaceship/Travel'

    def test_create_spaceship(self):
        data = {"id": 91083, "name": "First Jupyter", "model": "spaceX", "city": "Sydney", "planet": "Jupyter",
                "status": "commissioned"}
        response = self.client.post(self.Create_spaceship, json.dumps(data),
                                    content_type="application/json")
        out = json.loads(response.content)
        print(response.content)
        self.assertEqual(out['statusCode'], "200")

    def test_create_existing_spaceship(self):
        data = {"id": 91081, "name": "First mars", "model": "spaceX", "city": "Sydney", "planet": "Mars",
                "status": "operational"}
        # response = self.client.post(self.Create_spaceship, data)
        response = self.client.post(self.Create_spaceship, json.dumps(data),
                                    content_type="application/json")
        response2 = self.client.post(self.Create_spaceship, json.dumps(data),
                                     content_type="application/json")
        out = json.loads(response2.content)
        self.assertEqual(out['statusCode'], "304")

    def test_create_location(self):
        data = {"id": 3, "city": "Sydney", "planet": "Saturn"}
        print(data)
        # response = self.client.post(self.Add_Location, data)
        response = self.client.post(self.Add_Location, json.dumps(data),
                                    content_type="application/json")
        out = json.loads(response.content)
        self.assertEqual(out['statusCode'], "200")

    def test_create_existing_location(self):
        data = {"id": 2, "city": "Sydney", "planet": "Mars"}
        # response = self.client.post(self.Add_Location, data)
        response = self.client.post(self.Add_Location, json.dumps(data),
                                    content_type="application/json")
        response2 = self.client.post(self.Add_Location, json.dumps(data),
                                     content_type="application/json")
        out = json.loads(response2.content)
        self.assertEqual(out['statusCode'], "302")

    def test_update_status(self):
        data1 = {"id": 91081, "name": "First mars", "model": "spaceX", "city": "Sydney", "planet": "Mars",
                 "status": "operational"}
        data = {"id": 91081, "status": "commissioned"}
        response = self.client.post(self.Create_spaceship, json.dumps(data1),
                                    content_type="application/json")
        response2 = self.client.post(self.Update_status, json.dumps(data),
                                     content_type="application/json")
        out = json.loads(response2.content)
        self.assertEqual(out['statusCode'], "200")

    def test_update_nonexisting_status(self):
        data = {"id": 91088, "status": "commissioned"}
        # response = self.client.post(self.Update_status, data)
        response2 = self.client.post(self.Update_status, json.dumps(data),
                                     content_type="application/json")
        out = json.loads(response2.content)
        self.assertEqual(out['statusCode'], "306")

    def test_travel(self):
        data1 = {"id": 91085, "name": "First test travel", "model": "spaceX", "city": "Melb", "planet": "Mars",
                 "status": "operational"}
        data2 = {"id": 6, "city": "Sydney", "planet": "Venus"}
        response = self.client.post(self.Create_spaceship, json.dumps(data1),
                                    content_type="application/json")
        response2 = self.client.post(self.Add_Location, json.dumps(data2),
                                     content_type="application/json")
        data = {"id": 91085, "dest_id": 6}
        response3 = self.client.post(self.travel, json.dumps(data),
                                     content_type="application/json")
        out = json.loads(response3.content)
        self.assertEqual(out['statusCode'], "200")
        # response = self.client.post(self.travel, data)

    def test_nonexisting_travel(self):
        data = {"id": 91081, "dest_id": 67}
        response = self.client.post(self.travel, json.dumps(data),
                                    content_type="application/json")
        out = json.loads(response.content)
        self.assertEqual(out['statusCode'], "306")

    def test_sameport(self):
        data1 = {"id": 91085, "name": "First test travel", "model": "spaceX", "city": "Melb", "planet": "Mars",
                 "status": "operational"}
        data2 = {"id": 6, "city": "Sydney", "planet": "Venus"}
        response = self.client.post(self.Create_spaceship, json.dumps(data1),
                                    content_type="application/json")
        response2 = self.client.post(self.Add_Location, json.dumps(data2),
                                     content_type="application/json")
        data = {"id": 91085, "dest_id": 6}
        response3 = self.client.post(self.travel, json.dumps(data),
                                     content_type="application/json")
        response4 = self.client.post(self.travel, json.dumps(data),
                                     content_type="application/json")

        out = json.loads(response4.content)
        self.assertEqual(out['statusCode'], "309")

# Create your tests here.

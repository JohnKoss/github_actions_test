import pytest
import json

# from test.setup.table_setup import create_table, delete_table
# from app.main import lambda_handler as dt_create_lambda_handler
# from app.treat_delete import lambda_handler as dt_delete_lambda_handler
from app.main import inc

def test_answer():
    assert inc(3) == 4
    #assert inc(3) == 5

# # Used to set up the DynamoDb table in the docker container...
# @pytest.fixture(autouse=True)
# def setup_dynamoDb_table():
#     #create_table()
#     yield
#     #delete_table()

# # Used to read in the json event data...
# @pytest.fixture(autouse=True)
# def create_event():
#      with open(".\\events\\create_event.json") as json_file:
#          return json.load(json_file)

# # Used to read in the json event data for delete...
# @pytest.fixture(autouse=True)
# def delete_event():
#      with open(".\\events\\delete_event.json") as json_file:
#          return json.load(json_file)

# # Do the actual testing...
# def test_lambda_funcs(create_event,delete_event):
#     ret_id = dt_create_lambda_handler(create_event,None)
#     assert ret_id != None

#     delete_event["id"] = ret_id
#     assert dt_delete_lambda_handler(delete_event,None) != None
    
    

import pytest
from unittest import mock
from app import app

# sample data to be used for mocking report text
SAMPLE_TYPE = '{"organization":"Dunder Mifflin","reported_at":"2015-04-21","created_at":"2015-04-22","inventory":[{"name":"paper","price":"2.00"},{"name":"stapler","price":"5.00"}]}'
# create a test client
test_app = app.test_client()

# first, test the response content for a valid pdf with mocked data
@mock.patch("app.views.get_report_data", return_value=SAMPLE_TYPE)
def test_pdf_response_content(mocked_data):
    # well formed request
    # value of id doesn't matter too much since return from get_report data is mocked
    # it is used for the filename though
    response = test_app.get("/pdf/1234")
    # check the mocked_data was used
    mocked_data.assert_called_once()
    # ensure properly formed request headers
    assert response.headers["Content-Type"] == "application/pdf"
    assert response.headers["Content-Disposition"] == f"inline; filename = report_1234.pdf"
    

# test the response content for a valid xml with mocked data
@mock.patch("app.views.get_report_data", return_value=SAMPLE_TYPE)
def test_xml_response_content(mocked_data):
    response = test_app.get("/xml/12345")
    print(response.headers)
    mocked_data.assert_called_once()
    assert response.headers["Content-Type"] == "application/xml"
    assert response.headers["Content-Disposition"] == f"inline; filename = report_12345.xml"

# simple pdf response code test.
def test_pdf_response_codes():
    # id should be an integer, expect a bad request code
    r1 = test_app.get("/pdf/zzz")
    assert r1.status_code == 400
    # well formed request params, expect a 200 response
    r2 = test_app.get("/pdf/1")
    assert r2.status_code == 200


def test_xml_response_codes():
    # id should be an integer, expect a bad request code
    r1 = test_app.get("/pdf/xxxx")
    assert r1.status_code == 400
    # well formed request params, expect a 200 response
    r2 = test_app.get("/pdf/1234")
    assert r2.status_code == 200





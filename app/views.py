from flask import render_template, make_response, json
from app import app
from app.models import Report
from app.helpers import is_valid_id, get_report_data
import pdfkit
import dicttoxml


# Request handler for generating reports
# valid url examples are: /pdf/<integer> or /xml/<integer>
@app.route('/<format>/<id>', methods = ['GET'])
def get_report(format, id):
    # basic type validation on id
    if not is_valid_id(id):
        return f"<h4>id: {id} invalid. id must be an integer</h4>", 400

    # Get the report object from the id
    report_data = get_report_data(id)

    # Catch any empty returns (i.e. report doesnt exist in db)
    if report_data is None:
        return f"<h4>report not found for id: {id}</h4>"

    # create a dictionary object from the data
    text_data = json.loads(report_data)
    # create filename based on id and file extension
    filename = f"report_{id}.{format}"

    # create a pdf
    if format.lower()=='pdf':
        rendered = render_template('report_template.html', data=text_data)
        pdf = pdfkit.from_string(rendered, False)
        # create http response from pdf data
        response = make_response(pdf)

    # create an xml file
    elif format.lower() =='xml':
        xml = dicttoxml.dicttoxml(text_data)
        # create http response with the xml data
        response = make_response(xml)

    # if neither xml or pdf supplied in the request params, return an error message
    else:
        return f"<h3>Invalid file format {format}. Valid types are pdf and xml</h3>"

     # change the headers: tell browser expect xml/pdf so it can be displayed
    response.headers['Content-Type'] = f"application/{format}"
    response.headers['Content-Disposition'] = f"inline; filename = {filename}"

    return response



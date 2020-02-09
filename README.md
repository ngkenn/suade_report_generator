
# API to generate reports from the suade db
This flask app is an API which will generate xml or pdf reports from existing reports in the db. 

### dependencies
The pdfkit library is used. This has a dependency on wkhtmltopdf. This will need to be installed on the machine running the app:

`brew cask install wkhtmltopdf`

To install required python packages, run:
`pip install -r requirements.txt`

### Endpoints
> http://127.0.0.1:5000/xml/<report_id>
> http://127.0.0.1:5000/pdf/<report_id>

### Run the app
cd to the parent directory and enter the command:
`flask run`

### Run tests
In the parent directory, run:
`python -m pytest`


FLASK_APP=report_generator.py
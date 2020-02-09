from app.models import Report

# basic validation on the report id (int check)
# return true if int
def is_valid_id(id):
        try:
            int(id)
            return True
        except ValueError:
            return False

# Query the db with the report id
# abstracted out of view to make report data mockable for tests
def get_report_data(id):
    report = Report.query.get(id)
    # if valid request but no data, return None (handled in view)
    if report is None:
        return report
    #return report content
    return report.type

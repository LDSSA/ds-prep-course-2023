#python submit.py --slackid <your slackid>
#python submit.py --slackid "U04ST63FC02"

import requests
import os
import re
import click
from nbgrader import utils
from traitlets.config import Config
import nbconvert
import nbformat

###############################################################################
# Variables
###############################################################################
notebook_number=''


###############################################################################
# Grading
###############################################################################

def grade(nb):
    total_score = 0
    max_total_score = 0
    for cell in nb.cells:
        if utils.is_grade(cell):
            score, max_score = utils.determine_grade(cell)
            total_score += score
            max_total_score += max_score

    return total_score, max_total_score

def execute(notebook, timeout=None, allow_errors=True):
    c = Config()
    c.NotebookExporter.preprocessors = [
        "nbconvert.preprocessors.ClearOutputPreprocessor",
        "nbconvert.preprocessors.ExecutePreprocessor",
    ]
    c.ExecutePreprocessor.allow_errors = allow_errors
    if timeout:
        c.ExecutePreprocessor.timeout = timeout

    exporter = nbconvert.NotebookExporter(config=c)
    notebook, _ = exporter.from_notebook_node(notebook)

    return nbformat.reads(notebook, as_version=nbformat.NO_CONVERT)

def get_grade(notebook_path=str):
    '''Gets the grade for the given notebook.'''
    notebook = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
    notebook = execute(notebook)
    total_score, max_score = grade(notebook)
    print('total score:',total_score)
    return total_score

###############################################################################
# Submitting
###############################################################################

def submit_to_portal(slackid:str, score: float) -> None:
    '''
    Submits the notebook.
    Parameters:
        exercise_notebook: like 1
        slackid: like "U04TS63FC02"
        score: like 16.0
    '''
    if re.search("^U0[45][A-Z0-9]{8,8}$",slackid):
        #get the learning unit number from the path
        path=os.getcwd()
        path_split=path.split('/')
        lunit=int(re.findall('[0-9][0-9]',path_split[-1])[0])

        data = {
            "learning_unit": lunit,
            "exercise_notebook": 1,
            "slackid": slackid,
            "score": score,
        }
        print(data)
        response = requests.post('https://prep-course-portal.ldsacademy.org/submissions/', json=data) 
        print('Success!\n' if response.ok else 'Whoopsie Daisy', response.text)
    else:
        print('Fail - invalid slackid:',slackid)
        print('Check you slackid and try again. Example of a valid slackid: "UTS63FC02"')

@click.command()
@click.option('--slackid', help='slackid: like "UTS63FC02"', required=True)
def grade_submit(**kwargs) -> None:
    '''
    Grades the notebook and submits the grade to the prep course portal.
    Parameters:
        notebook_number: like '', ' 1' - global variable defined on top
        slackid: like "U04TS63FC02"
        score: like 16.0
    '''
    # TODO change once we releace most recent verion of ldsagrader to pip
    # from ldsagrader import notebook_grade
    # notebook_grade(notebook=notebook_name, checksum=None, timeout=None)['total_score']
    exercise_notebook='Exercise notebook'+notebook_number+'.ipynb'
    kwargs['score'] = get_grade(exercise_notebook)
    #general regex for slackid  "^[UW][A-Z0-9]{2,}$"
    #regex for prep course 2023 slackid (11 characters) "^U0[45][A-Z0-9]{8,8}$"
    submit_to_portal(**kwargs)

if __name__ == '__main__':
    grade_submit()

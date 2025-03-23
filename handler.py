from flask import Flask, render_template, request
from snowflake import connector
import pandas as pd
import os

app = Flask(__name__)

stage_name = "dev" #Can sometimes be different if you run into troubles try hardcoding

@app.route('/')
def homepage():
    cur = cnx.cursor().execute("Select Name, count(*) from ADDRESSES group by NAME;")
    data4charts=pd.DataFrame(cur.fetchall(), columns=['NAME','vote'])
    data4chartsJSON = data4charts.to_json(orient='records')
    return render_template('charts.html', data4chartsJSON=data4chartsJSON)

@app.route('/submit')
def submitpage():
    return render_template('submit.html')

@app.route('/harddata')
def hardData():
    dfhtml = updateRows().to_html()
    return render_template('index.html', dfhtml=dfhtml)

@app.route('/thanks4submit', methods=["POST"])
def thanks4submit():
    address = request.form.get("cname")
    name = request.form.get("uname")
    insertRow(address, name)
    return render_template('thanks4submit.html',
                           colorname=address,
                           username=name)
    

cnx = connector.connect(
    account= os.environ.get('REGION'),
    user= os.environ.get('USERNAME'),
    password= os.environ.get('PASSWORD'),
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
)


def insertRow(address, name):
    cur = cnx.cursor()
    update_query = "INSERT INTO ADDRESSES(ADDRESS, NAME) VALUES (%s, %s)"
    cur.execute(update_query, (address, name))

def updateRows():
    cur = cnx.cursor()
    cur.execute("SELECT * FROM ADDRESSES")
    rows = pd.DataFrame(cur.fetchall(),columns=['ADDRESS', 'NAME'])
    return rows


if __name__ == '__main__': 
    app.run()
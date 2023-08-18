from flask import Flask, render_template
import csv
app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    labels=[]
    data=[]

    with open('/home/internship/backend/result/result.csv','r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            labels.append(row['측정 종료 시각'])
            data.append(int(row['통과차량']))
    
    return render_template('chart.html', labels=labels, data=data)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
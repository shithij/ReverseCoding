from flask import Flask, render_template, request
import re
app = Flask(__name__)


@app.route('/first', methods=["post","get"] )
def first():
    inputFirst = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            if(int(request.form['input'])>=0):
                fact=1
                for i in range(1,(int(request.form['input']))+1):
                    fact*=i
                inputFirst = fact
            else:
                inputFirst= 'Invalid input for this question'
        else:
            inputFirst = 'Invalid Input'
    return render_template('first', input=inputFirst)


@app.route('/second', methods=["post","get"] )
def second():
    inputSecond = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            if (int(request.form['input']))>=0:
                inputSecond = int(((int(request.form['input']))*((int(request.form['input']))+1))*0.5)
            else:
                inputSecond='Invalid Input'
        else:
            inputSecond = 'Invalid Input'
    return render_template('second', input=inputSecond)

@app.route('/third', methods=["post","get"] )
def third():
    inputThird = None
    if request.method == "POST":
            inp=request.form['input']
            inputThird = (inp[::2]+inp[1::2])
    return render_template('third', input=inputThird)

    
@app.route('/fourth', methods=["post","get"] )
def fourth():
    inputFourth = 'Invalid Input'
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            a,b = request.form['input'].split()
            a,b = int(a), int(b)
            while b:
                a,b = b, a%b
            inputFourth = a
        else:
            inputFourth = 'Invalid Input'
    return render_template('fourth', input=inputFourth)


@app.route('/fifth', methods=["post","get"] )
def fifth():
    inputFifth = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            if float(request.form['input'])==0:
                inputFifth= 'Invalid Input for this question'
            elif float(request.form['input'])==1:
                inputFifth=0
            elif float(request.form['input'])==2:
                inputFifth=1
            elif float(request.form['input'])==3:
                inputFifth=1
            else:
                t1=0
                t2=1
                count=2
                while count<float(request.form['input']):
                    t3=t1+t2
                    t1=t2
                    t2=t3
                    count+=1
                inputFifth=t3
        else:
            inputSixth = 'Invalid Input'
    return render_template('fifth', input=inputFifth)


@app.route('/sixth', methods=["post","get"] )
def sixth():
    inputSixth = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputSixth=float(request.form['input'])-(10*((float(request.form['input']))**0.5))
        else:
            inputSixth = 'Invalid Input'
    return render_template('sixth', input=inputSixth)


@app.route('/seventh', methods=["post","get"] )
def seventh():
    inputSeventh = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            if int(request.form['input'])>2:
                inputSeventh=(int(request.form['input']))*(int(request.form['input'])-3)/2
            else:
                inputSeventh='Invalid Input for this question'
        else:
            inputSeventh = 'Invalid Input'
    return render_template('seventh', input=inputSeventh)


@app.route('/eighth', methods=["post","get"] )
def eighth():
    inputEighth = None
    if request.method == "POST":
            x=request.form['input']
            x=x.lower()
            inputEighth=""
            for i in range(len(x)):
                val=ord(x[i])
                if val>=97 and val<=122:
                    val+=4
                if val>122:
                    val=val%122+96
                inputEighth = inputEighth+chr(val)
    return render_template('eighth', input=inputEighth)


@app.route('/', methods=["post","get"] )
def opening():
    return render_template('opening')


@app.route('/actualend', methods=["post","get"] )
def actualend():
    return render_template('actualend')


@app.route('/end', methods=["post","get"] )
def end():
    return render_template('end')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)

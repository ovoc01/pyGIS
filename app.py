from flask import Flask, render_template

app = Flask(__name__)


@app.route('/',methods=['POST'])
def hello_world():  # put application's code here
    return 'Hello World!'\

@app.route('/vody')
def tay():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    #    app.run(debug=True, port=8000)
    import psycopg2

    connection = psycopg2.connect(host='localhost', port=5432, user='postgres', password='pixel', dbname='postgres')
    print(connection)

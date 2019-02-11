from app import create_app


app = create_app()


def runserver():
    app.run(host='0.0.0.0', port=9091, debug=False)


if __name__ == '__main__':
    runserver()
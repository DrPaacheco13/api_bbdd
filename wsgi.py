from main import app

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 5000, app)
    print("Servidor HTTP en ejecución en http://localhost:5000...")
    httpd.serve_forever()


import picoweb

app = picoweb.WebApp(__name__)

@app.route('/')
def index(req, resp):
    t = 123
    h = 456
    p = 789
    templateData = {
        'temp' : t,
        'humidity': h,
        'pressure': p

    }
    #yield from picoweb.start_response(resp)
    yield from picoweb.start_response(resp, content_type = "text/html")
    #yield from resp.awrite('Hello world from picoweb running on the ESP32')
    yield from app.render_template(resp, "sensor.tpl", (templateData,))

app.run(debug=True, host='especial_1')
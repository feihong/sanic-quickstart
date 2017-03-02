from pathlib import Path

from sanic import Sanic
from sanic.response import html, json


app = Sanic()


@app.route('/')
async def index(request):
    return html(Path('index.html').read_text())


@app.route('/json/')
async def data(request):
    return json(dict(name='Aubrey Plaza', job='Actress'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

# Feihong's Sanic Quickstart

## Installation

```
brew install entr
mkvirtualenv -p python3 sanic
pip install -r requirements.txt
```

## Getting started

Run the server: `inv serve`

Run the server with live reload: `inv dev`

## Notes

Passing debug=True to app.run() only enables debug output, it does not turn on
live reloading.

## Sources

- [WIP: Live Reload](https://github.com/channelcat/sanic/pull/465)
- [websocket support](https://github.com/channelcat/sanic/pull/469/)

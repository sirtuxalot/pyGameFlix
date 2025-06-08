# dev_main.py

from pyGameFlix import app

if __name__ == '__main__':
  app.run(debug=True, ssl_context='adhoc', port=5000)

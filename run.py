from app import app

@app.route('/')
def index():
  return 'server started.'
  
if __name__ == '__main__':
  app.run()

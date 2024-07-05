from reflex import Reflex

def navbar():
  return {"vspacer": 10}, {"hstack": [{"button": "Home"}, {"button": "About"}]}

def content():
  # Logic to fetch data from backend (replace with your implementation)
  data = {"title": "Welcome to the App"}
  return {"vspacer": 10}, {"h1": data["title"]}

def main():
  app = Reflex(components={"navbar": navbar, "content": content})
  return app

if __name__ == "__main__":
  main().run()

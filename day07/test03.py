import json

def load_data():
    try:
        with open("course.json","r",encoding="utf-8") as f:
            return json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        return {}

def main():
    load_data()
    print(load_data())

if __name__ == "__main__":
    main()


import json

def load_json(filename):
    try:
        with open(filename,"r",encoding="utf-8") as f:
                return json.load(f)
    except(FileNotFoundError,json.decoder.JSONDecodeError):
        return {}

def main():
    data1 = load_json("not_person.json")
    print("文件不存在时返回：",data1)

    test_data = {"name": "Tom", "age": 20}
    with open("test.json","w",encoding="utf-8") as f:
        json.dump(test_data,f,ensure_ascii=False)

    data2 = load_json("test.json")
    print("合法JSON返回：",data2)

    with open("bad.json","w",encoding="utf-8") as f:
        f.write("{name:}")

    data3 = load_json("bad.json")
    print("损坏JSON返回：",data3)

if __name__ == "__main__":
    main()
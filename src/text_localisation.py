import json


class TextLokalizashon():
    paf_to_text = '../text.json'
    text = {}

    def __init__(self, paf_to_text='text.json'):
        self.paf_to_text = paf_to_text
        with open(paf_to_text, 'r', encoding='utf-8') as file:
            self.text = json.load(file)

    def get(self, key):
        key = str(key)
        znachenie = self.text.get(key)
        if znachenie:
            return znachenie
        else:
            t = f'{key} ЗАПОЛНИ ЗНАЧЕНИЕ!'
            self.text[key] = t
            with open('../text.json', 'w', encoding='utf-8') as file:
                json.dump(self.text, file, ensure_ascii=False, indent=4)
            return t

    def __getitem__(self, item):
        t = self.get(item)
        return t


TEXT = TextLokalizashon()

if __name__ == '__main__':
    pass

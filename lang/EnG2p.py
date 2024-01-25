import re

class EnG2p:
    @staticmethod
    def convert(text):
        en_output = re.sub(r'[^\w\s]', ' ', text)
        en_output = re.sub(r'\s+', ' ', en_output).strip()
        return en_output

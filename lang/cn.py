import pypinyin
def cn_output(text):
    pinyin = " ".join(pypinyin.lazy_pinyin(text, errors='ignore'))
    return pinyin

from newspaper import Article
import nltk

url="https://udn.com/news/story/6811/5931945"
article=Article(url)
article.download()

print(article.html)
article.parse()
article.authors
article.publish_date
print(article.text)
print(article.top_image)

nltk.download('punkt')
article.nlp()
print(article.keywords)

print("-------------")
print(article.summary)
'''

import jieba
sentence1=jieba.cut("小明在塞上清華大學",cut_all=True)
原文網址：https://kknews.cc/tech/eye8qrq.html
（1）全模式：jieba分詞將根據最大的組詞可能性來進行分詞。我們設定「cut_all=True」，可以看到「小明在塞上清華大學」在全模式下的分詞結果為：

「小/明/在/塞上/上清/清華/清華大學/華大/大學」

在這裡可能的組詞方式「塞上」、「上清」、「清華」、「華大」、「大學」全部都被羅列出來。

（2）精確模式：默認情況（不設置「cut_all」）下就是精確模式（cut_all=False）。精確模式，將按最符合漢語習慣的斷句來進行分詞，往往是最精確的。例如「小明在塞上清華大學」在精確模式下的分詞結果為：

「小明/在/塞上/清華大學」

（3）搜尋引擎模式：將羅列出一句話在搜尋引擎里的所有可搜關鍵字。例如"小明碩士畢業於塞上小清華，後在波士頓大學深造"通過搜尋引擎模式後的分詞結果為：

「小明/碩士/畢業/於/塞上/小/清華/，/後/在/波士/大學/波士頓/波士頓大學/深造」

原文網址：https://kknews.cc/tech/eye8qrq.html

sentence1=jieba.cut("小明在塞上清華大學",cut_all=True)

sentence2=jieba.cut("小明在塞上清華大學",cut_all=False)

sentence3=jieba.cut("小明在塞上清華大學")

sentence4=jieba.cut_for_search("小明碩士畢業於塞上小清華，後在波士頓大學深造")

原文網址：https://kknews.cc/tech/eye8qrq.html

'''
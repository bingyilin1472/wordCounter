from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("Hello")


def eggs(request):
    # 下面這寫法其實不太建議，在這個短小的HttpResponse中置入HTML
    # HTML比較建議放在template之中
    return HttpResponse("<h1>EGGS<h1>")


def greeting(request):
    # 要三個參數render response，request/template firleName含副檔名/帶入data
    return render(request, 'greeting.html', {
        'name': 'Dante'
    })


def wordcounting(request):
    # template dir位置設定好後就能直接以它的名稱在view呼叫template去渲染
    return render(request, 'wordcount.html')


def counting(request):
    # request透過GET方法以key value方式就能取得url裡面帶的para
    # form裡面定義的name就是key會有對應到的輸入value
    request_temp = request.GET['fulltext']
    # print會在terminal上顯示(經常作為debug的一種手法
    print(request_temp)

    # Default為space，但他這種方式其實有瑕疵，會算了標點符號與\n，所以這個作法來計算word數量比較不佳
    # 想要改善的話可以用python的regular expression來處理，有很完備的工具可用，尤其面對英文字的時候
    wordlist = request_temp.split()
    worddictionary = {}
    for word in wordlist:
        # 他會去看是否有word這個key，沒有就初始化1
        if word not in worddictionary:
            worddictionary[word] = 1
        # 已存在就給他加1
        else:
            worddictionary[word] += 1

    return render(request, 'counting.html', {
        'content': request_temp,
        'text_len': len(request_temp),
        'word_number': worddictionary.items()
    })


def showInfo(request):
    return render(request, 'information.html')

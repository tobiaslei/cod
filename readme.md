# Cod
turn any site into a JSON api using xpath

# 用法
把網站的URL和對應網頁區域的xpath發給Cod server, 返回結果中的result就是對應網頁區域的html
```javascript
$(function(){
    $.ajax({
        url: 'http://127.0.0.1:5000/', 
        type: 'POST',
        dataType: 'json', 
        data: {
            'url': 'https://news.ycombinator.com/', 
            'xpath': '//*[@class="storylink"]'
        },
        success: function(data){
            $('#result').html(data['result']);
        }
        });
});
```
<img src="https://raw.githubusercontent.com/tobiaslei/cod/master/examples.png">

# TODO:
* 處理動態頁面

# Cod
turn any site into a JSON api using xpath

# Install
```bash
pip install -r requirements.txt
```

# How to use?
send the `url` and <a href='https://en.wikipedia.org/wiki/XPath'>`xpath`</a> that you want to crawl to the code server, it will return you the correponding xpath result.

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
* Handle ajax rendered pages

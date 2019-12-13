import js2py

js2py.require("xmlhttprequest").XMLHttpRequest;
js = """

var request = new XMLHttpRequest();
"""
js2py.eval_js(js)


# var XMLHttpRequest = js2py.require("xmlhttprequest").XMLHttpRequest;
# var request = new XMLHttpRequest();
# request.open("GET", 'http://www.miniclip.com');
# request.onreadystatechange = function() { 
# if (request.readystate === 4 && request.status === 200){
#     console.writeline(request.data);
# }
# };
# request.sent(null);
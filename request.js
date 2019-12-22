// Chrome Security: chrome://flags/
// Firefox Security: about:config

// var name = "codemzy";
// var url = "http://anyorigin.com/go?url=" + encodeURIComponent("https://www.codewars.com/users/") + name + "&callback=?";$.get(url, function(response) {  
//   console.log(response);
// });

////Does not work
// var myLoc = "https://www.miniclip.com/games/en/";
// getHttp =   myLoc.substring(0, 7);

// if ( getHttp == "https://")
// {
// finalUrl = myLoc;
// } else {
// finalUrl = 'https://' + myLoc;
// }

// window.location = 'view-source:' + finalUrl;

// function makeHttpObject() {
//   try {return new XMLHttpRequest();}
//   catch (error) {}
//   try {return new ActiveXObject("Msxml2.XMLHTTP");}
//   catch (error) {}
//   try {return new ActiveXObject("Microsoft.XMLHTTP");}
//   catch (error) {}

//   throw new Error("Could not create HTTP request object.");
// }
// var request = makeHttpObject();
// request.open("GET", "http://www.miniclip.com/games/en", true);
// request.send(null);
// request.onreadystatechange = function() {
//   if (request.readyState == 4)
//     alert(request.responseText);
// };

// window.location.href="http://www.miniclip.com/games/en"

// console.log('Hello, World!');
// 1. Create a new XMLHttpRequest object
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
let xhr = new XMLHttpRequest();

// 2. Configure it: GET-request for the URL /article/.../load
xhr.open('GET', 'https://www.miniclip.com/games/en/');
xhr.setRequestHeader('Content-Type', 'application/json');
// 3. Send the request over the network
xhr.send();
// 4. This will be called after the response is received
console.log(`XHR Status: ${xhr.status}`)
if (xhr.status != 200) { // analyze HTTP status of the response
    console.log(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
} else { // show the result
    conesole.log(`Done, got ${xhr.response.length} bytes`); // responseText is the server
}

// 1. Create a new XMLHttpRequest object
// var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
let xhr = new XMLHttpRequest();

// 2. Configure it: GET-request for the URL /article/.../load
xhr.open('GET', 'https://www.miniclip.com/games/en/');
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.setRequestHeader('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36');
//xhr.setRequestHeader('Host','www.miniclip.com');
xhr.setRequestHeader('Cache-Control','max-age=0');

// 3. Send the request over the network
xhr.send();

// 4. This will be called after the response is received
xhr.onload = function() {
  if (xhr.status != 200) { // analyze HTTP status of the response
    console.log(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
  } else { // show the result
    console.log(`Done, got ${xhr.responseText.length} bytes`); // responseText is the server
    let headers = xhr.getAllResponseHeaders().split('\r\n').reduce((result, current) => {
        let [name, value] = current.split(': ');
        result[name] = value;
        return xhr.responseTex;
    }, {});
    console.log(headers);
    console.log(xhr.responseText);
    return xhr.responseText;
    // return headers;
  }
};

xhr.onprogress = function(event) {
  if (event.lengthComputable) {
    console.log(`Received ${event.loaded} of ${event.total} bytes`);
    
  } else {
    console.log(`Received ${event.loaded} bytes`); // no Content-Length
  }

};

xhr.onerror = function() {
    console.log("Request failed");
};


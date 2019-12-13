// console.log('Hello, World!');
// // 1. Create a new XMLHttpRequest object
// var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
// let xhr = new XMLHttpRequest();

// // 2. Configure it: GET-request for the URL /article/.../load
// xhr.open('GET', 'https://www.miniclip.com/games/en/');
// xhr.setRequestHeader('Content-Type', 'application/json');
// // 3. Send the request over the network
// xhr.send();
// // 4. This will be called after the response is received
// console.log(`XHR Status: ${xhr.status}`)
// if (xhr.status != 200) { // analyze HTTP status of the response
//     console.log(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
// } else { // show the result
//     conesole.log(`Done, got ${xhr.response.length} bytes`); // responseText is the server
// }

// 1. Create a new XMLHttpRequest object
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
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
        return result;
    }, {});
    console.log(headers);
    console.log(xhr.responseText);
    return xhr.responseText;
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


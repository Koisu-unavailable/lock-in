const CONFIG_PATH = chrome.runtime.getURL("C:\\Users\\jalau\\Blog\\lock-in\\config.txt")
var xmlHttp = new XMLHttpRequest();
xmlHttp.onreadystatechange = function() { 
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
        callback(xmlHttp.responseText);
        console.log(xmlHttp.responseText)
}
xmlHttp.open("GET", CONFIG_PATH, true); // true for asynchronous 
xmlHttp.send(null);
// for (let i = 0; i < 10; i++) {
    
    
// }
// const URLS = [
//     "*://*.googlesyndication.com/*",
//      "*://*.google-analytics.com/*",
//     "*://*.quantserve.com/*",
//      "*://*.scorecardresearch.com/*",
//      "*://*.zedo.com/*",
//      "*://*.doubleclick.net/*",
//      "*://partner.googleadservices.com/*",
//      "*://creative.ak.fbcdn.net/*",
//      "*://*.adbrite.com/*",
//      "*://*.exponential.com/*",
//      "*://*"
    
//     ]
    
//     chrome.webRequest.onBeforeRequest.addListener(
//         function(details) { return { cancel: true }},
//         { urls: defaultFilters },
//         ["blocking"]
//     )
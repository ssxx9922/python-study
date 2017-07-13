var url = 'http://www.baidu.com'
var page = require('webpage').create();
page.viewportSize = {
    width: 1024,
    height: 769
};
page.clipRect = {
    top: 0,
    left: 0,
    width: 1024,
    height: 768
};
console.log('The default user agent is ' + page.settings.userAgent);
page.onConsoleMessage = function (msg) {
    console.log(msg);
}
page.onResourceRequested = function (request) {
    console.log('Request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function (response) {
    console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open(url, function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        page.render('example.png');
    }
    var title = page.evaluate(function () {
        return document.title
    })
    console.log("Page title is " + title);
    page.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js", function () {
        page.evaluate(function () {
            $("su").click();
        });
        phantom.exit();
    });
    
});
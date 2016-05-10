var http = require('http');
var url = require('url');

var pad = function(n)
{
    return (n<10)?'0'+n:n;
}

var server = http.createServer(function(request,response)
{
    if(request.method == 'GET')
    {
        var urlContent = url.parse(request.url,true);
        var jsonObject = {};
        var dateObj = new Date(urlContent.query.iso);
        response.writeHead(200,{'Content-Type':'application/json'});
        if(urlContent.pathname == '/api/parsetime')
        {
            jsonObject.hour = pad(dateObj.getHours());
            jsonObject.minute = pad(dateObj.getMinutes());
            jsonObject.second = pad(dateObj.getSeconds());   
        }
        if(urlContent.pathname == '/api/unixtime')
        {
            jsonObject.unixtime = dateObj.getTime();    
        }
        response.write(JSON.stringify(jsonObject));
        response.end();
    }
});


server.listen(Number(process.argv[2]));
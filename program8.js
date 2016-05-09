var http = require('http');
var content="";
http.get(process.argv[2],function(request)
{
    request.setEncoding('utf8');
    request.on('data',function(data)
    {
        content+=data;
    });
    request.on('end',function()
    {
        console.log(content.length);
        console.log(content);
        
    });
    
})
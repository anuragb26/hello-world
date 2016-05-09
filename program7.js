var http=require('http');

http.get(process.argv[2],function (request)
{
    response.setEncoding('utf8');
    /*
    response.on('data',function(data)
    {
        console.log(data);
    })
    */
    request.on('data',console.log);
});


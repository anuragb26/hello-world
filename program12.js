var http=require('http');
var mapStream= require('through2-map');


var mapStreamLogic = function (data)
{
    return data.toString().toUpperCase();
}
var server = http.createServer(function (request,response)
{
    
    if(request.method == 'POST')
        {
            request.pipe(mapStream(function(data)
            {
                return data.toString().toUpperCase()
                
            })).pipe(response);
            
        }
    
});

server.listen(Number(process.argv[2]));
var http = require('http');
var deals = require('../controllers/deals');
var settings = require('../settings');


http.createServer(function(request,response)
{
    switch(request.method)
        {
            case "GET":
                if (request.url == "/")
                    {
                        response.end();
                    }
                else if(request.url == "/deals")
                    {
                        console.log(request.url);
                        deals.getAllDeals(request,response);       
                    }
                break;
            case "POST":
                break;
            case "DELETE":
                break;
            case "PUT":
                break;
        }
    
}).listen(settings.webPort,function()
{
    console.log("Started Listening at "+ settings.webPort);
})
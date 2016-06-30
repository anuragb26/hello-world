var http = require('http');
var deals = require('../controllers/deals');
var settings = require('../settings');
var httpMsgs = require("./httpMsgs");

http.createServer(function(request,response)
{
    switch(request.method)
        {
            case "GET":
                if (request.url == "/")
                    {
                        httpMsgs.sendInfo(request,response);
                        response.end();
                    }
                else if(request.url == "/deals")
                    {
                        deals.getAllDeals(request,response);       
                    }
                else
                    {
                        var requestUrlArray = request.url.split("/");
                        var id = requestUrlArray.pop();
                        var entity= requestUrlArray.pop();
                        switch(entity)
                        {
                            case "deals":
                                deals.getDeal(request,response,id);
                                break;
                            default:
                                httpMsgs.sendPageNotFoundError(request,response);
                                break;
                        }   
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
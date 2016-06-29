var db = require("../core/db");

module.exports.getAllDeals = function(request,response)
{
    db.executeQuery(" SELECT * FROM f_rtb_dealids ",function(data,err)
    {
        if(err)
        {
            console.log("writing error in controller ");
            response.writeHead(500," Internal Server occurred ",{"Content-Type" : "text/html"});
            response.write("<html><head><title>500</title></head><body>500: Internal Error Details: " + err + "</body></html>");
        }
        else
        {
            console.log("writing data in controller ");
            response.writeHead(200,{"Content-Type" : "application/json"});
            response.write(JSON.stringify(data));
        }

        response.end();
    });
};

module.exports.get = function(request,response,empno)
{
};

module.exports.add = function(request,response,requestBody)
{

};

module.exports.update = function(request,response,requestBody)
{

};

module.exports.delete = function(request,response,requestBody)
{

};
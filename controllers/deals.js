var db = require("../core/db");
var httpMsgs = require("../core/httpMsgs");

module.exports.getAllDeals = function(request,response)
{
    db.executeQuery(" SELECT * FROM f_rtb_dealids ",function(data,err)
    {
        if(err)
        {
            httpMsgs.sendError(request,response,err);
        }
        else
        {
            httpMsgs.sendData(request,response,data);
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
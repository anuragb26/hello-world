var db = require("../core/db");
var httpMsgs = require("../core/httpMsgs");

module.exports.getAllDeals = function(request,response)
{
    db.executeQuery(" SELECT * FROM f_rtb_dealids ",function(data,err)
    {
        if(err)
        {
            httpMsgs.sendInternalServeError(request,response,err);
        }
        else
        {
            httpMsgs.sendData(request,response,data);
        }
    });
};

module.exports.getDeal = function(request,response,dealId)
{
    db.executeQuery(" SELECT * FROM f_rtb_dealids where rtb_dealid_id = '" + dealId + "'",function(data,err)
    {
        if(err)
        {
            httpMsgs.sendInternalServeError(request,response,err);
        }
        else
        {
            httpMsgs.sendData(request,response,data);
        }
    });
    
    
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
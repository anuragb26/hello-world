module.exports.sendError = function(request,response,err)
{
    response.writeHead(200," Internal Server occurred ",{"Content-Type" : "application/json"});
    response.write(JSON.stringify({data : "Error Occured " + err }));
    response.end();
};

module.exports.sendData = function(request,response,data)
{
    response.writeHead(200,{"Content-Type" : "application/json"});
    response.write(JSON.stringify(data));
    response.end()
}
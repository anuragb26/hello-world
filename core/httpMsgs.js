module.exports.sendInternalServeError = function(request,response,err)
{
    response.writeHead(500," Internal Server occurred ",{"Content-Type" : "application/json"});
    response.write(JSON.stringify({data : "Error Occured " + err }));
    response.end();
};

module.exports.sendPageNotFoundError = function(request,response)
{
    response.writeHead(404," Resource Not Found ",{"Content-Type" : "application/json"});
    response.write(JSON.stringify({data : "Resource Not Found "}));
    response.end();    
}

module.exports.sendInfo = function(request,response)
{
    response.writeHead(200,{"Content-Type" : "application/json"});
    response.write(JSON.stringify([
                                    {url : "/deals" , operation : "GET" , description : "To List All Deals"},
                                    {url : "/deals/dealid" , operations : "GET" , description : "To Search for a Deal"}
                                  ]));
    response.end();
}
module.exports.sendData = function(request,response,data)
{
    response.writeHead(200,{"Content-Type" : "application/json"});
    response.write(JSON.stringify(data));
    response.end();
}
var http=require('http');
var bl = require('bl');
var serverContents={};
var firstServerData="";
var secondServerData="";
var thirdServerData="";
var serverLength=0;
var checkifEnd = function()
{
    var status = (serverLength==3)?true:false;
    return status;
    
}

var printData = function(testingFunc)
{
    if(testingFunc())
        {
            console.log(serverContents.first);
            console.log(serverContents.second);
            console.log(serverContents.third);
        }
}
/*
http.get(process.argv[2],function(request)
{
    request.pipe(bl function(err,data)
    {
        serverContents.first=data.toString();
        serverLength+=1;
        printData(checkifEnd);
        
    })
    
});
*/
http.get(process.argv[2],function(request)
{
    request.setEncoding('utf8');
    request.on('data',function(data)
    {
        firstServerData+=data;
        
    });
    request.on('end',function()
    {
        //serverContents.push(secondServerData);
        serverContents.first=firstServerData;
        serverLength+=1;
        printData(checkifEnd);
        
    })
    
});

http.get(process.argv[3],function(request)
{
    request.setEncoding('utf8');
    request.on('data',function(data)
    {
        secondServerData+=data;
        
    });
    request.on('end',function()
    {
        //serverContents.push(secondServerData);
        serverContents.second=secondServerData;
        serverLength+=1;
        printData(checkifEnd);
        
    })
    
});

http.get(process.argv[4],function(request)
{
    request.setEncoding('utf8');
    
    request.on('data',function(data)
    {
       thirdServerData+=data; 
    });
    request.on('end',function()
    {
        //thirdServerData.push(thirdServerData);
        serverContents.third=thirdServerData;
        serverLength+=1;
        printData(checkifEnd);
        
    })
})

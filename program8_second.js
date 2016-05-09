var http=require('http');
var bl = require('bl');

http.get(process.argv[2],function(request){
    request.pipe(bl(function(err,data)
    {
        if(err)
            {
                console.log("Error");
            }
        else
            {
                var content = data.toString();
                console.log(content.length);
                console.log(content);
            }
        
    }))
    
    
});


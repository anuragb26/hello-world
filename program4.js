var fs = require('fs');


function readFile(callback)
{
    fs.readFile(process.argv[2],function printNoOfLines(err,fileContent){
        if(err)
            {
                callback("Error in processing the file");
            }
        else
            {
                noOfLines=fileContent.toString().split("\n").length - 1
                callback(noOfLines);
            }
    })
}


function writeToConsole(data)
{
    console.log(data);
}


readFile(writeToConsole);
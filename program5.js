var fs = require('fs');

fs.readdir(process.argv[2],function printFileNames(err,fileNames)
{
    if(err)
        {
            console.log("error in reading dir contents");
        }
    else
        {
            var fileEndsWith = "."+process.argv[3];
            var filteredArray = fileNames.filter(function(fileName)
            {
                return fileName.endsWith(fileEndsWith);
            })
            for (var i=0;i<filteredArray.length;i++)
                {
                    console.log(filteredArray[i]);
                }
        }
    
})
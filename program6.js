var moduleFunc=require('./ioModule.js');


var printFilteredFiles = function(err,filteredFiles)
{
	if(err)
	{
		console.log("there was some error in reading files");
	}
	else
	{
		filteredFiles.forEach(function(fileName)
		{
			console.log(fileName);
		});
	}
};

moduleFunc(process.argv[2],process.argv[3],printFilteredFiles);
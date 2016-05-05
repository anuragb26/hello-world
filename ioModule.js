var fs = require('fs');
var path = require('path');

module.exports=function filteredFiles(dirName,ext,callBack)
{
	fs.readdir(dirName,function filterFiles(err,files)
	{
		if(err)
		{
			callBack(err);
		}
		else
		{
			var fileExt = "." + ext;
			matchingFiles = files.filter(function isFileValid(fileName)
			{
				return path.extname(fileName)==fileExt;

			});
			callBack(null,matchingFiles);
		}
	});

}
var website = "http://www.html5rocks.com/en/tutorials/es6/promises/";

function get(url)
{
	return new Promise(function(resolve,reject)
	{
		var req = new XMLHttpRequest();

		req.open('GET',url);

		//console.log(" after making request " + req.readyState );
		req.onload = function()
		{
			//console.log("inside ajax request onload " + req.readyState );
			if(req.status == 200)
			{
				resolve(req.response);
			}
			else 
			{
				reject(Error(req.statusText))
			}
		}

		req.onerror = function()
		{
			//console.log(" in error " + req.readyState );
			reject(Error("Network Error"));
		}

		req.send();

	});
}

/*
get(website+"story.json").then
(
	function(result)
	{
		console.log("Success , ",result);
		resultObj=JSON.parse(result);

	},
	function(err)
	{
		console.log("Failure ",err);
	}
)

get(website+"story.json").then
(

	function(result)
	{
		return JSON.parse(result)
	}
	
).then(function (jsonData)
{
	console.log("YAYYY " + jsonData);
});

*/
function getJSON(url)
{
	 return get(url).then(JSON.parse);
}


getJSON(website+"story.json").then
(
	function(jsonObj)
	{
		console.log("Got story ",jsonObj);
		//window.location.href = website+jsonObj['chapterUrls'][0]
		return getJSON(website+jsonObj['chapterUrls'][0]) // returning a promise which the next then will receive
	}	
).then(function (chapter)
{
	console.log("Got chapter ",chapter);
})



for(i=0;i<5;i++)
{
	addHtmlToPage("anurag");
}

















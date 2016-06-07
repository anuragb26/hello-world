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

/*
getJSON(website+"story.json").then
(
	function(jsonObj)
	{
		console.log("Got story ",jsonObj);
		//window.location.href = website+jsonObj['chapterUrls'][0]
		for(var i = 0 ; i< jsonObj['chapterUrls'].length;i++)
		{
			return getJSON(website + jsonObj['chapterUrls'][i]) // returning a promise which the next then will receive
		}
	}	
).then(function (chapter)
{
	console.log("Got chapter ",chapter);
}).catch(function(error)
{
	console.log("catch " + error);
})
*/
// Below is the implementation to implement promises sequentially without loop
// Issue is to somehow synchronize the counter for getChapter
var storyPromise =false;
function getChapter(i)
{
	if(!storyPromise)
	{
		getJSON(website+"story.json").then(function(jsonObj)
		{
			addHeadingToPage(jsonObj.heading);
		})
		storyPromise = true;
	}

	return getJSON(website+"story.json").then(function(jsonObj)
	{
			return getJSON(website + jsonObj['chapterUrls'][i]);
	})
}

//  Then in all cases but better approach is the next case when you have a catch at the end
/*
getChapter(0).then(function(chapterObj)
{
	console.log("success chapter 0");
	addHtmlToPage(chapterObj.chapter,chapterObj.html)
	return getChapter(1);
},function(error)
{
	console.log("failure chapter 0");
}).then(function(chapterObj)
{
	console.log("success chapter 1");
	addHtmlToPage(chapterObj.chapter,chapterObj.html);
	return getChapter(2);
	//return Error;
},function(error)
{
	console.log("failure chapter 1");
}).then(function(chapterObj)
{
	console.log("success chapter 2");
	addHtmlToPage(chapterObj.chapter,chapterObj.html)
	return getChapter(3);
},function(error)
{
	console.log("failure chapter 2");
}).then(function(chapterObj)
{
	console.log("success chapter 3");
	addHtmlToPage(chapterObj.chapter,chapterObj.html)
	return getChapter(4);
},function(error)
{
	console.log("failure chapter 3");
}).catch(function(error)
{
	console.log("failure chapter 4");
});

*/





getChapter(0).then(function(chapterObj)
{
	console.log("success chapter 0");
	addHtmlToPage(chapterObj.chapter,chapterObj.html)
	return getChapter(1);
}).then(function(chapterObj)
{
	console.log("success chapter 1");
	addHtmlToPage(chapterObj.chapter,chapterObj.html)
	return getChapter(2);
}).then(function(chapterObj)
{
	console.log("success chapter 2");
	addHtmlToPage(chapterObj.chapter,chapterObj.html)
	return getChapter(3);
}).then(function(chapterObj)
{
	console.log("success chapter 3");
	addHtmlToPage(chapterObj.chapter,chapterObj.html)
	return getChapter(4);
}).catch(function(error)
{
	console.log("failure chapter 4");
}).then(function(){
	$('body').append('<b> I am added no matter what</b>');
});














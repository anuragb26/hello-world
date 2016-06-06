var promise = new Promise(function(resolve,reject)
{

	if(all is good)
	{
		resolve("all is good")
	}
	else
	{
		reject(Error("It broke"));
	}
});


promise.then(function(result)
{
	console.log(result);
}),function(err)
{
	console.log(err)
});

var promise = Promise.resolve($.ajax(abc));

var deffreedObj = $.ajax(abc);


// deferred Object can have many arguments for the callbacks
defferedObj.then(function (arg1,arg2,agr3)
{

},function (arg1,arg2,arg3)
{

});

//on resolving by promise ,only first argument is passed

promise.then(function(arg1)
{

},function(arg1)
{

});


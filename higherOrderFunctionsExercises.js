var createSingleArray = function(array1,array2)
{
	return array1.concat(array2);
}


var arrays = [[1, 2, 3], [4, 5], [6]];

console.log(arrays.reduce(createSingleArray));


var ancestors = JSON.parse(ANCESTRY_FILE);

console.log(ancestors.length);





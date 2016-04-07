var createSingleArray = function(array1,array2)
{
	return array1.concat(array2);
}


var arrays = [[1, 2, 3], [4, 5], [6]];

console.log(arrays.reduce(createSingleArray));


var ancestors = JSON.parse(ANCESTRY_FILE);

console.log(ancestors.length);

var objectsByNameKey = {};
var getObjectsByNameKey = function(person)
{
		objectsByNameKey[person.name]=person;
}

ancestors.forEach(getObjectsByNameKey); 

var validPerson = 0 ;

function average(array)
{
    function plus(a,b)
    {
        return a+b;
    }
    
    return array.reduce(plus)/array.length;
}

var getAgeDifferenceArray = function(person)
{
        return person.born - objectsByNameKey[person.mother].born ;
}

var filterByMotherNameExistsInDataSet = function(person)
{
    return objectsByNameKey[person.mother] !=null;   
}

var ageDifferenceArray=ancestors.filter(filterByMotherNameExistsInDataSet).map(getAgeDifferenceArray);
console.log(average(ageDifferenceArray));

var objectsByCentury = {};
var groupPersonsByCentury = function(person)
{
    var century = Math.ceil(person.died/100);
    if(century in objectsByCentury)
        {
            objectsByCentury[century].push(person.died -person.born);
        }
    else
        {
            objectsByCentury[century]=[];
            objectsByCentury[century].push(person.died -person.born);
        }
}
ancestors.forEach(groupPersonsByCentury);

var getAgeOfPerson = function(person)
{
    return person.died - person.born;
}
var printAverageAgeByCentury = function(groupedObject)
{
    for(century in groupedObject)
        {
            console.log(century + " - " +average(groupedObject[century].map(getAgeOfPerson)));
        }
}

var genericGroupBy = function(array,groupByFunc)
{
    var groupByObject={};
    array.forEach(function(element)    /* Decision whether to write the callback anonymously or make a seperate function call */
    {
        groupByKey = groupByFunc(element);
        if(groupByKey in groupByObject)
            {
                groupByObject[groupByKey].push(element);
            }
            else
            {
                groupByObject[groupByKey]=[];
                groupByObject[groupByKey].push(element);
            }   
    });
    return groupByObject;
}

var logicForCenturyGroups = function(element)
{
    return Math.ceil(element.died/100);
}

var groupedObject = genericGroupBy(ancestors,logicForCenturyGroups);
console.log(printAverageAgeByCentury(groupedObject));


/* Sometimes good old for loops are better
var every = function(array,func)
{
    var count = 0;
    array.forEach(function(element)
    {
            if(func(element) == true)
                {
                    count++;
                }
    });
    return count == array.length;
}

var some = function(array,func)
{
    var returnValue = false;
    array.forEach(function(element)
    {
        if(!func(element) && !returnValue)
            {
                returnValue=true;;
            }
        
    });
    return returnValue;
}

*/

var every = function(array,predicate)
{
    for(var i = 0 ; i < array.length;i++)
        {
            if(!predicate(array[i]))
                {
                    return false; // you can return out of a for loop 
                }
        }
    return true;
}

var some = function(array,predicate)
{
    for(var i = 0 ; i < array.length ; i++)
        {
            if(predicate(array[i]))
                {
                    return true;
                }
        }
    return false;
}
console.log(every([NaN, NaN, NaN], isNaN));
// → true
console.log(every([NaN, NaN, 4], isNaN));
// → false
console.log(some([NaN, 3, 4], isNaN));
// → true
console.log(some([2, 3, 4], isNaN));





















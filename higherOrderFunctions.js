/* Functions that operate on other functions either by taking them as arguments or by returning them are called 
Higher order functions 

JSON.stringify -> Takes a js object and returns a json string
JSON.parse -> Takes a json string and returns  a js array of objects

*/

function greaterThanN(n)
{
    return function(m)
    {
        return m>n;
    };
}

var greaterThan10  = greaterThanN(10);
console.log(greaterThan10(11));
console.log(greaterThan10(9));

function utilityWithComparison(n,utilityFunc)
{
    return function(m)
    {
        utilityFunc(n);
        if(m > n)
            {
               // console.log(m + " is greater than " + n);
            }
        else
            {
                //console.log(m + " is smaller than " + n);
            }
        utilityFunc(m)
    }
}

function oddOrEven(n)
{
    if(Array.isArray(n))
        {
            n.forEach(oddOrEven);
        }
    if(n%2==0)
        {
            console.log(n + " is even ");
        }
    else
        {
            console.log(n + " is odd ");
        }
}

utilityWithComparison(1,oddOrEven)(2);  // one way of calling (cryptic)

var oddEvenUtilityWithComparisonTo10 = utilityWithComparison(10,oddOrEven);
oddEvenUtilityWithComparisonTo10(11); // standard way of calling (understandable)

function noisy(f)
{
    return function(arg)
    {
        console.log("initially called with " + arg);
        var flag =  f(arg);
        console.log("return value is " + flag);
        return flag;
    };
}

noisy(Boolean)(0);

function transparentWrapping(utilityFunc)
{
    return function()
    {
      return utilityFunc.apply(null,arguments);  
    };
}

transparentWrapping(oddOrEven)([1,2,3]);

var ancestry = JSON.parse(ANCESTRY_FILE); // ancestry is now js object , methods in Object.Prototype can be called on it
console.log(Array.isArray(ancestry));

function filter(array,test)
{
    var passed = [];
    for(var i =0;i< array.length;i++)
    {
        if(test(array[i]))
        {
            passed.push(array[i]);
        }
    }

    return passed;
}



var x = filter(ancestry,function(person)
{
    return person.born > 1900 && person.born < 1925;
});
console.log(x);


function checkFatherName(person)
{
    return person.father == "Carel Haverbeke";
}


console.log(ancestry.filter(function(person){
   return person.father  =="Carel Haverbeke";
}));

console.log(ancestry.filter(checkFatherName));

var filterAgeGreaterThan90 =function(person)
{
    return person.died - person.born  > 90;
}
function returnNamesArray(person)
{ 
    return person.name;
}

console.log(ancestry.filter(filterAgeGreaterThan90).map(returnNamesArray));


function reduce(array,combine,start)
{
    var current = start;
    for(var i = 0 ; i < array.length;i++)
        {
            current =  combine(current,array[i]);
        }
    return current;
}

console.log(reduce([1,2,3,4,5],function(a,b){return a+b;},0));

var oldestAncestor = function(min,cur)
{
    if(cur.born < min.born)
        {
            return cur;
        }
    else
        {
            return min;
        }
}
console.log(ancestry.reduce(oldestAncestor));

// the average age for men and for women  in the data set


var filterMale = function(person)
{
    return person.sex=="m";
}

var filterFemale=function(person)
{
    return person.sex == "f";
}

var age = function(person)
{
    return person.died - person.born;
}
var average =function(array)
{
    function plus(a,b)
    {
        return a+b;
    }
    return array.reduce(plus)/array.length;
}
console.log(average(ancestry.filter(filterMale).map(age)));

var byName = {};
function createObjectByName(person)
{
    byName[person.name] =person;
}
ancestry.forEach(createObjectByName); // create object which has objects
function mapObjectsByName(person)
{
    var obj = {};
    obj[person.name]=person;
    return obj;
}
var mapByName = ancestry.map(mapObjectsByName);  // return array of object;
console.log(byName);

function reduceAncestors(person,f,defaultValue)
{
    function valueFor(person)
    {
        if(person == null)
            {
              //  console.log("in default value");
                return defaultValue;
            }
        else
            {
              //  console.log("in else for "+ person.name);
              //  console.log("will search for " + person.father);
              //  console.log("will search for " + person.mother);
                return f(person,valueFor(byName[person.mother]),valueFor(byName[person.father]));
            }
    }
    return valueFor(person);
}

function sharedDNA(person,fromMother,fromFather)
{
   
    if(person.name == "Pauwels van Haverbeke")
        {
            // console.log("in sharedDNA  return one for " + person.name);
            return 1 ;
        }
    else
        {
            // console.log("in sharedDNA sum object for " + person.name+ " with value " + (fromMother + fromFather)/2);
            return (fromMother + fromFather)/2;
        }
}

var ph = byName["Philibert Haverbeke"];
//console.log(ph);
console.log(reduceAncestors(ph,sharedDNA,0)/4);


function countAncestors(person,test)
{
    function combine(current,fromMother,fromFather)
    {
        var thisOneCounts = current!=person && test(current);
        return fromMother + fromFather + (thisOneCounts?1:0);
    }
    
    return reduceAncestors(person,combine,0); // combine is passed to reduceAncestors but is has access to person variable (inner function has access to outer variable)
    
}

function longLivingAncestors(person)
{
    var all = countAncestors(person,function(person){
        return true;
    });
    
    var longLiving = countAncestors(person,function(person){
        return (person.died - person.born) >= 70;
    })
    return longLiving/all;
}

console.log(longLivingAncestors(byName["Emile Haverbeke"]))

/*
x->y->z->q->a

e->r->y->b

t->z->a   

everyPerson who exists call sharedDna on it..
if person.name == "correct" then dna sharing is 1
else dnasharing is halfOf 
1/2
*/





































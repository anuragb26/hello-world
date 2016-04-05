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
                console.log(m + " is greater than " + n);
            }
        else
            {
                console.log(m + " is smaller than " + n);
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



console.log(ancestry.filter(function(person){
   return person.father  =="Carel Haverbeke";
}));
















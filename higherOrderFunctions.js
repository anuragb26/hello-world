/* Functions that operate on other functions either by taking them as arguments or by returning them are called 
Higher order functions */

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


/*
Local variables are recreated every time a function is called.
Hence every function call retains the value of its local variables.
*/


var multiplier  = function(factor)
{
    return function(number)
    {
        return factor*number;
    };
};

var twice = multiplier(2);
var thrice = multiplier(3);

alert(twice(5));
alert(twice(10));

alert(thrice(5));
alert(thrice(10));


/* Recursion example 

*/
var solution = function findSolution(target)
{
    function find(start,history)
    {
        if(start == target)
            {
                return history;
            }
        else if(start > target)
            {
                return null;
            }
        else 
            {
                return find(start+5,"("+history+"+5)") || find(start * 3,"("+history+"*3)");
            }
            
    }
    return find(1,"1");
}

alert(solution(11));
alert(solution(14));
alert(solution(5));

var zeroPad = function(number,width)
{
    var string = String(number);
    
    while(string.length < width)
        {
            return "0"+string;
        }
    return string;
    
}

var printFarmInventory = function(cows,chicken,pigs)
{
    console.log(zeroPad(cows,3) + " Cows ");
    console.log(zeroPad(chicken,3) + " Chicken ");
    console.log(zeroPad(pigs,3) + " Pigs ");
}

printFarmInventory(3,16,155);


var min = function(num1,num2)
{
    if(num1<=num2)
        {
            return num1;
        }
    else
        {
            return num2;
        }
}

var isEven = function(n)
{
    if(n==0)
        {
            return true;
        }
    else if(n==1)
        {
            return false;
        }
    else 
        {
            return isEven(n-2);
        }
}

var countBs = function(content)
{
    
}








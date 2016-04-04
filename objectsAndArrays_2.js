/* Exercises for chapter 4 */

function range(start,end)
{
    var array = []
    for(var i = start;i<=end;i++)
        {
            array.push(i);
        }
    return array;
}

function sum(array)
{
    var sum = 0;
    for(var i =0;i<array.length;i++)
        {
            sum = sum + array[i];
        }
    return sum;
}
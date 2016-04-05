/* Exercises for chapter 4 */

function range(start,end,step)
{
    var array=[];
    if(step == null)
        {
            step =1;
        }
    if(step == 1 && start > end)
        {
            step=-1;
        }
    
    if(step > 0)
        {
            for(var i = start;i<=end;i+=step)
                {
                    array.push(i);
                }
        }
    else
        {
            for(var i =start;i>=end;i+=step)
                {
                    array.push(i);
                }
            
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

function reverseArray(array)
{
    var reverseArray = [];
    for(var i = array.length -1;i>=0;i--)
        {
            reverseArray.push(array[i]);
        }
    return reverseArray;
}

function reverseArrayInPlace(array)
{
    for(var i = 0,j=array.length -1;i<=j;i++,j--)
        {
            var temp = array[i];
            array[i]=array[j];
          	array[j]=temp;
        }
    return array;
}


function arrayToList(array)
{
    var list = {};
    var initialList=list;
    for(var i = 0 ; i < array.length;i++)
    {
        list.value=array[i];
        list.rest={};
        list=list.rest;
    }
    list.rest=null;
    return initialList;
}

function listToArray(listObject)
{
    var array = [];
    while(listObject.rest !== null)
    {
        array.push(listObject.value);
        listObject = listObject.rest;
    }

    return array;
}

function prepend(number,listObject)
{
    var newListObject = {};
    newListObject.value = number;
    
    newListObject.rest = listObject;
    
    return newListObject;
}

function prependCorrect(number,listObject)
{
    return {value: number,rest: listObject};
}


function nth(listObject,number)
{
    for(var i=0;i<number;i++)
        {
            listObject=listObject.rest;
        }
    if(listObject.value != null)
        {
            return listObject.value;
        }
    else
        {
            return undefined;
        }
}

function nth(listObject,number)
{
    if(number==0 && listObject.value !=null)
        {
            return listObject.value;
        }
    if(number == 0 && listObject.value == null)
        {
            return undefined;
        }
    return nth(listObject.rest,number-1);
}











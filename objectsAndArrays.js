/* accessing property 

if variable then x[var] 
if property name is known then x.propertyName or x["propertyName"]
x.propertyName can be used if propertyName is a valid variable name which maps to a property
array.length and array["length"] both work

0 -> 00 -> both false
1 -> 01 -> first false and second true
2 -> 10 -> first true and second false
3 -> 11 -> both true
peanuts and brushed teeth

*/

var journal = [];
function addEntry(events,didItTurnIntoSquirrel)
 {
     journal.push({
         events : events,
         squirrel : didItTurnIntoSquirrel
     }); 
 }

function phi(table)
{
    return ((table[3]*table[0] - table[1]*table[2])/(Math.sqrt((table[2] + table[3])*(table[0]+table[1])*(table[1]+table[3])*(table[0]+table[2]))));
}

function hasEvent(event,eventObject)
{
    return eventObject.events.indexOf(event) !=-1 ;
}

function tableFor(event,journal)
{
    var table=[0,0,0,0];  
    for(var i = 0 ; i < journal.length;i++)
        {
            var index=0;
            var eventObject=journal[i];
            if(hasEvent(event,eventObject))
                {
                    index+=1;
                }
            if(eventObject.squirrel==true)
                {
                    index+=2;
                }
            table[index]+=1;
        }
    return table;
    
}

function gatherCorrelations(journal)
{
    var phis = {};
    for(var entry = 0 ; entry < journal.length;entry++)
        {
            var events=journal[entry].events;
            for(var i = 0 ; i < events.length;i++)
                {
                    var event= events[i];
                    if(!(event in phis))
                        {
                            phis[event]=phi(tableFor(event,journal));
                        }
                }
        }
    return phis;
}
function printCorrelations(correlations)
{
    for(var event in correlations)
        {
            console.log("The correlation for '" + event + "' is " + correlations[event]);
            
        }
}
var correlations = gatherCorrelations(JOURNAL);
//printCorrelations(correlations);

function findCorelation(journal,firstEvent,secondEvent)
{
    var linkedEvent = firstEvent + " " + secondEvent;
    for(var i = 0 ; i < journal.length;i++)
        {
            var eventObject=journal[i];
            if(hasEvent(firstEvent,eventObject) && !hasEvent(secondEvent,eventObject))
                {
                    eventObject.events.push(linkedEvent);
                }
        }
    return phi(tableFor(linkedEvent,journal));
}
var probability = findCorelation(JOURNAL,"peanuts","brushed teeth");
console.log("Probability variable " + probability);




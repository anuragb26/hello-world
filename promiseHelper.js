/**
 * Created by Anurag on 6/5/2016.
 */


function addHtmlToPage(index,htmlString)
{
    console.log("index " + index);
    var d=document.createElement("div");
    var newdiv = document.createElement( "div" );
    //$(d).attr("",id);
    $(d).html("<h3>"+index+"</h3>"+htmlString);
   // console.log($(d).text());
   // var div = "<div><b>"+id+"</b></div>";
 //   $(d).appendTo("body");
    $("body").append(d);
}

function addHeadingToPage(headingString)
{
    $("body").append(headingString);
}
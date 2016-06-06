/**
 * Created by Anurag on 6/5/2016.
 */


function addHtmlToPage(id)
{
    d=document.createElement("div");
    $(d).attr("id",id);
    $(d).html("<b>id</b>");
    $(d).appendTo()
    //$("body").append($(d).html());
}

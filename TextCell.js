
function TextCell(cellContent)
{
	this.text=cellContent.split("\n");
}

TextCell.prototype.toString = function()
{
	return this.text.join("");
}
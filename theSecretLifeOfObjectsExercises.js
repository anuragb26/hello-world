function Vector(x,y)
{
    this.x = x;
    this.y = y;
}

Vector.prototype.plus = function(v)
{
    newX=this.x + v.x;
    newY = this.y + v.y;
    
    return new Vector(newX,newY);
}

Vector.prototype.minus = function(v)
{
    newX=this.x - v.x;
    newY=this.y - v.y;
    
    return new Vector(newX,newY);
}

Object.defineProperty(Vector.prototype,"length",{get:function()
{
    return Math.sqrt(Math.pow(this.x,2) + Math.pow(this.y,2));
}});


console.log(new Vector(1, 2).plus(new Vector(2, 3)));
// → Vector{x: 3, y: 5}
console.log(new Vector(1, 2).minus(new Vector(2, 3)));
// → Vector{x: -1, y: -1}
console.log(new Vector(3, 4).length);
// → 5



function StretchCell(cell,reqWidth,reqHeight)
{
    this.innerCell = cell;
    this.reqWidth = reqWidth;
    this.reqHeight = reqHeight;
}

StretchCell.prototype.minWidth = function()
{
    return Math.max(this.reqWidth,this.innerCell.minWidth());
}

StretchCell.prototype.minHeight = function()
{
    return Math.max(this.reqHeight,this.innerCell.minHeight());
}

StretchCell.prototype.draw = function(width,height)
{
    return this.innerCell.draw(width,height);
}



var cell = new TextCell("abc");

console.log(cell.minWidth());
console.log(cell.minHeight());
console.log(cell.draw(3,2));


var sc = new StretchCell(new TextCell("abc"),1,2);

console.log(sc.minWidth());
console.log(sc.minHeight());
console.log(sc.draw(3,2));



























function TextCell(cellContent)
{
	this.text=cellContent.split("\n");
}

function pad(paddingData,paddingLength)
{
	var paddingContent="";
	for(i=0;i<paddingLength;i++)
	{
		paddingContent+=paddingData;
	}
	return paddingContent;
}


TextCell.prototype.minWidth = function()
{
	return this.text.reduce(function(current,line)
	{
		return Math.max(current,line.length);

	},0);
}

TextCell.prototype.minHeight = function()
{
	return this.text.length;
}

TextCell.prototype.draw = function(width,height)
{
	var result=[];
	for(i=0;i<height;i++)
	{
		var line = this.text[i] || "";
		result.push(line + pad(" ",width - line.length));
	}
	return result;
}

function UnderlineCell(innerCell)
{
	this.inner = innerCell;
}

UnderlineCell.prototype.minWidth = function()
{
	return this.inner.minWidth();
}

UnderlineCell.prototype.minHeight = function()
{
	return this.inner.minHeight()+1;
}

UnderlineCell.prototype.draw = function(width,height)
{
	return this.inner.draw(width,height-1).concat([pad("-",width)]);
}

function minHeight(rows)
{
	return rows.map(function(row)
	{
		return row.reduce(function(current,cell)
			{
				return Math.max(current,cell.minHeight());
			},0);
	});

}
function minWidth(rows)
{
	return rows[0].map(function(_,index)
	{
		return rows.reduce(function(current,row)
		{
			return Math.max(current,row[index].minWidth());

		},0);
	})
}

function drawTable(rows)
{
	var widths = minWidth(rows);
	var heights = minHeight(rows);

	function drawLine(blocks,index)
	{
		return blocks.map(function(block)
			{
				return block[index];
			}).join(" ");
	}

	function drawRow(row,rowIndex)
	{
		var blocks = row.map(function(cell,cellIndex)
		{
			return cell.draw(widths[cellIndex],heights[rowIndex]);
		});
		
		return blocks[0].map(function(_,index)
		{
			return drawLine(blocks,index);
		}).join("\n");
	}

	return rows.map(drawRow).join("\n");

}


function dataTable(data)
{
	var keys = Object.keys(data[0]);

	var headers = keys.map(function(key)
	{
		return new UnderlineCell(new TextCell(String(key)));
	});
	
	var content = data.map(function(dataObject)
	{
		return keys.map(function(key)
		{
			return new TextCell(String(dataObject[key]));
		});
	});

	return [headers].concat(content);
}











var rows = [];

for(i = 0 ;i < 5;i++)
{
	var row=[];
	for(j=0;j<5;j++)
	{
		if((i+j)%2==0)
		{
			row.push(new TextCell("abcd"))
		}
		else
		{
			row.push(new TextCell("ef"));
		}
	}
	rows.push(row);
}

console.log(rows.toString());
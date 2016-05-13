var rows = [];


var MOUNTAINS = [
  {name: "Kilimanjaro", height: 5895, country: "Tanzania"},
  {name: "Everest", height: 8848, country: "Nepal"},
  {name: "Mount Fuji", height: 3776, country: "Japan"},
  {name: "Mont Blanc", height: 4808, country: "Italy/France"},
  {name: "Vaalserberg", height: 323, country: "Netherlands"},
  {name: "Denali", height: 6168, country: "United States"},
  {name: "Popocatepetl", height: 5465, country: "Mexico"}
];

for(i = 0 ;i < 5;i++)
{
	var row=[];
	for(j=0;j<5;j++)
	{

		if(j==0)
		{
			row.push(new TextCell("a"));
		}
		else if((i+j)%2==0)
		{
			row.push(new TextCell("abc"))
		}
		else
		{
			row.push(new TextCell("ef"));
		}
	}
	rows.push(row);
}
//console.log(dataTable(MOUNTAINS));
console.log(drawTable(dataTable(MOUNTAINS)));
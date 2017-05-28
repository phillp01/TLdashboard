queue()
    .defer(d3.json, "/dash/projects")
    .await(makeGraphs);

function print_filter(filter){
	var f=eval(filter);
	if (typeof(f.length) != "undefined") {}else{}
	if (typeof(f.top) != "undefined") {f=f.top(Infinity);}else{}
	if (typeof(f.dimension) != "undefined") {f=f.dimension(function(d) { return "";}).top(Infinity);}else{}
	console.log(filter+"("+f.length+") = "+JSON.stringify(f).replace("[","[\n\t").replace(/}\,/g,"},\n\t").replace("]","\n]"));
}

function makeGraphs(error, projectsJson)    {

    var tlDash = projectsJson; //Get the SQL Data passed over
    var dateFormat = d3.time.format("%Y-%m-%d %H:%M:%S");

    //Create crossfilter for the Digit Totals

    var count = crossfilter(tlDash);
    var totalActiveAccounts = count.size();

    var totalAdmin = count.dimension(function(d)    {
        return d[2];
    })

    var adminUsers = totalAdmin.filter(5);
    //print_filter(adminUsers);
    animateValue("totalUserNumber", 0, totalActiveAccounts, 2000);

    /////////////////////////////////////////

    var ndx = crossfilter(tlDash); //Create crossfilter for main charts

    var memberTypeDim = ndx.dimension(function(d)   {
        return d[3];
    })

    var numMemberTypes = memberTypeDim.group();
    var userTypeChart = dc.pieChart("#chart-users");


    var count =0;
    var dataTable = dc.dataTable("#dc-table-graph");
    var userList = ndx.dimension(function(d)    {
        return d[0] + d[1];
    });





    dataTable.width(960).height(800)
        .dimension(userList)
        .group(function(d)  {
            return "User List";
        })
        .size(10)
        .columns([
            function(d) { return d[0]},
            function(d) { return d[1]},
            function(d) { return d[3]}
        ])
        .sortBy(function(d) { return d[0]})
        .order(d3.ascending)
        .size(Infinity);


    userTypeChart
       .height(420)
       .radius(140)
       .innerRadius(40)
       .transitionDuration(1500)
       .dimension(memberTypeDim)
       .group(numMemberTypes);

    dc.renderAll();
}

/*Animate number function taken from a Stack overflow article :
https://stackoverflow.com/questions/16994662/count-animation-from-number-a-to-b
 */
function animateValue(id, start, end, duration) {
    var range = end - start;
    var current = start;
    var increment = end > start? 1 : -1;
    var stepTime = Math.abs(Math.floor(duration / range));
    var obj = document.getElementById(id);
    var timer = setInterval(function() {
        current += increment;
        obj.innerHTML = current;
        if (current == end) {
            clearInterval(timer);
        }
    }, stepTime);
}



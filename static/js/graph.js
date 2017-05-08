queue()
    .defer(d3.json, "/dash/projects")
    .await(makeGraphs);

function makeGraphs(error, projectsJson)    {

    var tlDash = projectsJson;
    var dateFormat = d3.time.format("%Y-%m-%d %H:%M:%S");

    var ndx = crossfilter(tlDash);

    var memberTypeDim = ndx.dimension(function(d)   {
        return d[3];
    })

    var numMemberTypes = memberTypeDim.group();

    var userTypeChart = dc.pieChart("#chart-users");

    var dataTable = dc.dataTable("#dc-table-graph");
    //var users = crossfilter(tlDash);
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
        .order(d3.ascending);


    userTypeChart
       .height(420)
       .radius(140)
       .innerRadius(40)
       .transitionDuration(1500)
       .dimension(memberTypeDim)
       .group(numMemberTypes);

    dc.renderAll();
}
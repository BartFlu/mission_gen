function get_insert_terrain(mission_id, session_type) {
    console.log(session_type)
    let req_terrain = "/getTerrainMap?mission_id="+mission_id+"&type="+session_type;
    $.get(req_terrain, function(data, status) { // function(data, status) contains data from the get request
        let terrain_data = JSON.parse(data); // assing parsed data to terrain data var
        if(terrain_data["table_img"]){ // triggers function if terrain data have the table img
            let img_path1 = "../static/imgs/tables/" + terrain_data["table_img"] + ".png";
            let img_path2 = "../static/imgs/tables/" + terrain_data["table_img"] + "m.png";
            let html_content = // build the new html content
                '<div class="d-flex flex-row">' +
                '<div class="p-6">' +
                '<img class="terrain_img" src='+img_path2+' alt=""/>' +
                '</div>'+
                '<div class="p-6">' +
                '<img class="terrain_img" src='+img_path1+' alt=""/>' +
                '</div>'+
                '</div>';
            html_content += '<div class="d-flex justify-content-end">Maps created by: <img class="img-fluid logo_img" src="../static/imgs/logo/logo_wtc.png" alt=""/></div>';
            $('#terrainMap').html(html_content); // change the html content of the terrainMap id
        }
    });
}



function insert_mission(data_obj) {
    let temp = data_obj["mission_id"].split('-')[0];
    $("#missionSource").html("Mission source: " + temp + " "+ data_obj["mission_scale"]);
    $("#missionName").html(data_obj["mission_name"]);
    let img_path = "../static/imgs/" + data_obj["deployment_img"];
    $('#missionImg').html('<img class="img-fluid map_img" src='+img_path+' alt=""/>');
    $("#missionContent").html(data_obj["mission_desc"]);
}

function update_selector() {
    console.log(NAMESPACE.scale_filter);
    console.log(NAMESPACE.user_group_filter);
    console.log(NAMESPACE.missions_data);
    let data = NAMESPACE.missions_data;
    let group_filtered = {};
    if(NAMESPACE.user_group_filter){
        console.log("DSADSA");
        group_filtered = NAMESPACE.missions_data[NAMESPACE.user_group_filter];
    }
    else{
        for(let key in data) {
            for(let scale in data[key]){
                if(!group_filtered.hasOwnProperty(scale)){
                    group_filtered[scale] = []
                }
                group_filtered[scale] = group_filtered[scale].concat(data[key][scale]);
            }
        }
    }
    console.log("res1: ", group_filtered);
    let scale_group_filtered = group_filtered[NAMESPACE.scale_filter];
    console.log("res2: ", scale_group_filtered);
    let selector_element = $("#chooseMission");
    selector_element.empty();
    for(let mission in scale_group_filtered){
        selector_element.append(new Option(
            scale_group_filtered[mission]["name"],
            scale_group_filtered[mission]["mission_id"]))
    }
}

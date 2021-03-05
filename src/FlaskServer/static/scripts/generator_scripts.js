$(document).ready(function(){
     // Global variables - managing dropdowns
     window.NAMESPACE= {
         user_group_filter: "",
         scale_filter: "StrikeForce",
         // missions: [],
         missions_data: [],
     };

     // $.get("/getAvailableScenarios", function(data, status){
     //     let data_obj = JSON.parse(data);
     //     NAMESPACE.missions = data_obj["scenarios"];
     //     console.log(NAMESPACE.missions);
     //     for(let mis_id in NAMESPACE.missions){
     //         $("#chooseMission").append(new Option(
     //             NAMESPACE.missions[mis_id],
     //             NAMESPACE.missions[mis_id]));
     //     }
     // });


     $.get("/getAvailableScenariosData", function(data, status){
         let data_obj = JSON.parse(data);
         NAMESPACE.missions_data = data_obj;
         update_selector();
     });

     // On btn select click
     $("#btnGetMission").click(function() {
         let selected_id = $("#chooseMission").val();
         if (selected_id)
         {
             let req_url = "/getScenarioByID?mission_id=" + selected_id;
             $.get(req_url, function(data, status){
                 let data_obj = JSON.parse(data);
                 insert_mission(data_obj);
             });
             let get_terrain_flag = $("#terrainCheck1").prop('checked');
            if(get_terrain_flag)
            {
                var session_type = "select";
                console.log(session_type)
                get_insert_terrain(selected_id, session_type);
            }
         }
     });

    // On Randomize click
    $("#btnRandomize").click(function(){

        let req_url = "/getRandomScenario";
        // check if group filter is set
        // console.log(NAMESPACE.user_group_filter);
        req_url+="?source="+NAMESPACE.user_group_filter+"&scale="+NAMESPACE.scale_filter;

        $.get(req_url, function(data, status){
            let data_obj = JSON.parse(data);
            insert_mission(data_obj);
            let get_terrain_flag = $("#terrainCheck1").prop('checked');
            if(get_terrain_flag) {
                var session_type = "random";
                console.log(session_type);
                get_insert_terrain(data_obj["mission_id"], session_type);
            }
            else{
                $('#terrainMap').html("");
            }
        });
    });


    function switch_visibility(){
        if(NAMESPACE.user_group_filter === "GTpack" && NAMESPACE.scale_filter === "StrikeForce"){
            $('#terrainCheck1').css("visibility", "visible");
            $('#terrainCheck1Label').css("visibility", "visible");
        }
        else{
            $('#terrainCheck1').css("visibility", "hidden");
            $('#terrainCheck1Label').css("visibility", "hidden");
        }
    }

    $("#selectMissionGroup").change(function () {
        // Change mission group filter variable
        NAMESPACE.user_group_filter = $("#selectMissionGroup").val();
        switch_visibility();
        update_selector();
    });

    $("#selectMissionScale").change(function () {
        // Change mission scale filter variable
        NAMESPACE.scale_filter = $("#selectMissionScale").val();
        switch_visibility();
        update_selector();
    })
});

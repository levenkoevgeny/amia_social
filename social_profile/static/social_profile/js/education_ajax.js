$("#education_data_add").click(function() {

    let form_data = $("form").serializeArray();

    $.ajax({
        url: "/profiles/education/add/",
        method: "POST",
        dataType: 'json',
        data: form_data,
        timeout : 100000,
        success: function (data) {
            console.log(data);
            if (data['error']) {
                alert(data['error']);
            } else {
                window.opener.location.href = window.opener.location.href;
                window.close();
            }
        },
        error: function (e) {
            console.log("ERROR: ", e);
        },
        done: function (e) {
            console.log("DONE");
        }
    });
});

function education_delete(){
    alert('werw');
}
// $("#id_education_delete_button").click(function() {
// alert('werw');
    // education_id = 7;
    //
    // $.ajax({
    //     url: "/profiles/education/delete/" + education_id + "/",
    //     method: "POST",
    //     timeout : 100000,
    //     success: function (data) {
    //         window.opener.location.href = window.opener.location.href;
    //         window.close();
    //     },
    //     error: function (e) {
    //         console.log("ERROR: ", e);
    //     },
    //     done: function (e) {
    //         console.log("DONE");
    //     }
    // });
// });



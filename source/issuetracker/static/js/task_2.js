const indexLink = "http://localhost:8000/api/project/";


$.ajax({
    url: 'http://localhost:8000/api/login/',
    method: 'post',
    data: JSON.stringify({username: 'admin', password: 'admin'}),
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){
        localStorage.setItem('apiToken', response.token);
        console.log(response)
        },
    error: function(response, status){console.log(response);}
});


function jqueryParseData(response, status) {
    console.log(response);
	console.log(status);

}

function jqueryAjaxError(response, status) {
    console.log(response);
    console.log(status);
    console.log('error');

}

function jqueryLoadIndex(){
    $.ajax({
       url: indexLink,
        method: 'GET',
        success: jqueryParseData,
        error: jqueryAjaxError
    });

}

function jqueryLoadIndexTask(){
    $.ajax({
       url: "http://localhost:8000/api/task/",
        method: 'GET',
        success: jqueryParseData,
        error: jqueryAjaxError
    });

}

function jqueryLoadProjectDetail(){
    $.ajax({
       url: "http://localhost:8000/api/project/3/",
        method: 'GET',
        success: function(response, status){console.log(response.task_project)},
        error: jqueryAjaxError
    });

}

function jqueryCreateTask(){
    $.ajax({
    url: 'http://localhost:8000/api/task/',
    method: 'post',
    data: JSON.stringify({summary: "test", description: "test3", status: 5, type: 5, project: 3,
    assigned_to: 1}),
    dataType: 'json',
    headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
    contentType: 'application/json',
    success: function(response, status){
        console.log(response)
        },
    error: function(response, status){console.log(response);}
    });

}

function ajaxDeleteTask() {
    $.ajax({
    url: 'http://localhost:8000/api/task/100/',
    method: 'delete',
    dataType: 'json',
    headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
    contentType: 'application/json',
    success: function(response, status){
        console.log('deleted')
        },
    error: function(response, status){console.log(response);}
    });
}

$(document).ready(function () {
    // jqueryLoadIndex();
    // jqueryLoadIndexTask();
    jqueryLoadProjectDetail();
    // jqueryCreateTask();
    // ajaxDeleteTask();

});
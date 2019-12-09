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
};


function jqueryAjaxError(response, status) {
    console.log(response);
    console.log(status);
    console.log('error');
    
};

function jqueryLoadIndex(){
    $.ajax({
       url: indexLink,
        method: 'GET',
        success: jqueryParseData,
        error: jqueryAjaxError
    });

};

$(document).ready(function () {
    jqueryLoadIndex();

});
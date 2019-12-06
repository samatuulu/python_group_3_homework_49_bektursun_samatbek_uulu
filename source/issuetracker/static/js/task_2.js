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


$.ajax({
     url: 'http://localhost:8000/api/project/',
     method: 'get',
     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
     data: JSON.stringify({username: 'admin', password: 'admin'}),
     dataType: 'json',
     contentType: 'application/json',
     success: function(response, status){console.log(response);},
     error: function(response, status){console.log(response);}
});
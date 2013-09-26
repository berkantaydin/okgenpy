$(function () {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather?q=istanbul,tr",
        type: 'GET',
        dataType: 'JSONP',
        success: function (data) {
            $("#weather").text(data.name + ' ' + parseInt(data.main.temp - 273.15) + ' C')
        }
    });
});

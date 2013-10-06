$(function () {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather?q=istanbul,tr",
        type: 'GET',
        dataType: 'JSONP',
        success: function (data) {
            $("#weather").text(data.name + ' ' + parseInt(data.main.temp - 273.15) + ' C')
        }
    });

    $.ajax({
        url: "http://rate-exchange.appspot.com/currency?from=USD&to=TRY&q=1",
        type: 'GET',
        dataType: 'JSONP',
        success: function (data) {
            $("#currency_dolar").text('$' + ' ' + data.rate.toFixed(2) + ' TL');
        }
    });

    $.ajax({
        url: "http://rate-exchange.appspot.com/currency?from=EUR&to=TRY&q=1",
        type: 'GET',
        dataType: 'JSONP',
        success: function (data) {
            $("#currency_euro").text('€' + ' ' + data.rate.toFixed(2) + ' TL');
        }
    });



});

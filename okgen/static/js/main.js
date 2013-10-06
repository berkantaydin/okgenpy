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

    $.fn.Scroll = function (opt, callback) {
        if (!opt) var opt = $.extend({}, opt);
        var _this = $(this).find("ul:first");
        var lineH = _this.find("li:first").height(), line = opt.line ? parseInt(opt.line, 10) : parseInt(this.height() / lineH, 10), speed = opt.speed ? parseInt(opt.speed, 10) : 500, timer = opt.timer ? parseInt(opt.timer, 10) : 3000;
        if (line == 0) line = 1;
        _this.upHeight = 0 - line * lineH;
        scrollUp = function (me) {
            me.animate({marginTop: me.upHeight}, speed, function () {
                for (i = 1; i <= line; i++) {
                    me.find("li:first").appendTo(me);
                }
                me.css({marginTop: 0});
            });
        };
        _this.hover(function () {
            clearInterval(_this.timerID);
        },function () {
            _this.timerID = setInterval(function () {
                scrollUp(_this);
            }, timer);
        }).mouseout();
    };


    $("#scrollDiv").Scroll({line: 1, speed: 300, timer: 2000});
    $("#scrollDivBuyTr").Scroll({line: 1, speed: 300, timer: 2000});

    var container = document.querySelector('.links2');
    var msnry = new Masonry(container, {
        itemSelector: '.pin'
    });
});

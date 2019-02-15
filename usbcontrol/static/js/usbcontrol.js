/*
 * View model for USBControl
 *
 * Author: OutsourcedGuru
 * License: AGPLv3
 */
$(function() {
    function UsbcontrolViewModel(parameters) {
        var self = this;

        saveInit = function() {
            $.ajax({
                url:         "/api/plugin/usbcontrol",
                type:        "POST",
                contentType: "application/json",
                dataType:    "json",
                headers:     {"X-Api-Key": UI_API_KEY},
                data:        JSON.stringify({"command": "save", "init": true}),
                complete: function () {
                }
            });
            return true;
        };

        togglePower2 = function() {
            var e =  document.getElementById('idUSB2');
            console.log('togglePower2(): ', e.checked ? 'ON' : 'OFF');
            $.ajax({
                url:         "/api/plugin/usbcontrol",
                type:        "POST",
                contentType: "application/json",
                dataType:    "json",
                headers:     {"X-Api-Key": UI_API_KEY},
                data:        JSON.stringify({"command": "usb2", "arg2": e.checked ? "on" : "off"}),
                complete: function () {
                }
            });
            return true;
        };

        togglePower3 = function() {
            var e =  document.getElementById('idUSB3');
            console.log('togglePower3(): ', e.checked ? 'ON' : 'OFF');
            $.ajax({
                url:         "/api/plugin/usbcontrol",
                type:        "POST",
                contentType: "application/json",
                dataType:    "json",
                headers:     {"X-Api-Key": UI_API_KEY},
                data:        JSON.stringify({"command": "usb3", "arg3": e.checked ? "on" : "off"}),
                complete: function () {
                }
            });
            return true;
        };

        togglePower4 = function() {
            var e =  document.getElementById('idUSB4');
            console.log('togglePower4(): ', e.checked ? 'ON' : 'OFF');
            $.ajax({
                url:         "/api/plugin/usbcontrol",
                type:        "POST",
                contentType: "application/json",
                dataType:    "json",
                headers:     {"X-Api-Key": UI_API_KEY},
                data:        JSON.stringify({"command": "usb4", "arg4": e.checked ? "on" : "off"}),
                complete: function () {
                }
            });
            return true;
        };

        togglePower5 = function() {
            var e =  document.getElementById('idUSB5');
            console.log('togglePower5(): ', e.checked ? 'ON' : 'OFF');
            $.ajax({
                url:         "/api/plugin/usbcontrol",
                type:        "POST",
                contentType: "application/json",
                dataType:    "json",
                headers:     {"X-Api-Key": UI_API_KEY},
                data:        JSON.stringify({"command": "usb5", "arg5": e.checked ? "on" : "off"}),
                complete: function () {
                }
            });
            return true;
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct:                          UsbcontrolViewModel,
        dependencies:                       [],
        elements:                           []
    });
});

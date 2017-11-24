$.fn.aesEncrypt = function(n) {
    var t = CryptoJS.MD5("login.189.cn"),
        i = CryptoJS.enc.Utf8.parse(t),
        r = CryptoJS.enc.Utf8.parse("1234567812345678"),
        u = CryptoJS.AES.encrypt(n, i, {
            iv: r
        });
    return u + ""
};
$.fn.aesDecrypt = function(n) {
    var t = CryptoJS.MD5("login.189.cn"),
        i = CryptoJS.enc.Utf8.parse(t),
        r = CryptoJS.enc.Utf8.parse("1234567812345678");
    return CryptoJS.AES.decrypt(n, i, {
        iv: r
    }).toString(CryptoJS.enc.Utf8)
};


d = CryptoJS.AES.encrypt('密码原文',
CryptoJS.enc.Utf8.parse(CryptoJS.MD5("login.189.cn")), {
    iv: CryptoJS.enc.Utf8.parse("1234567812345678"),
    mode:CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
});
alert(d + "");


login('18926089010', '159753')


var c = "";
var b = "login.189.cn";
c = c + $("#txtAccount").val() + "$";
c = c + $("#txtUType").val() + "$";
c = c + $("#hidUType").val() + "$";
c = c + $("#txtCityNo").val() + "$";
c = c + $("#hidProvinceID").val() + "$";
c = c + $("#hidAreaCode").val() + "$";
c = c + $("#hidCityNo").val() + "$";
c = c + $("#hidRandomFlag").val();
c = CryptoJS.AES.encrypt(c, b);
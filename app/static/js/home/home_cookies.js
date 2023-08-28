// Чтение cookie
function getCookie(name) {
	var cookieArr = document.cookie.split(";");

	for (var i = 0; i < cookieArr.length; i++) {
		var cookiePair = cookieArr[i].split("=");

		// Удаляем пробелы в начале и конце имени cookie
		var cookieName = cookiePair[0].trim();

		// Если найдено совпадение имени cookie, возвращаем значение
		if (cookieName === name) {
			return decodeURIComponent(cookiePair[1]);
		}
	}

	// Если cookie не найдено, возвращаем пустую строку
	return "";
	}
console.log("Hello");
// Чтение печенек
var username = getCookie("outputFileName");
console.log(username);
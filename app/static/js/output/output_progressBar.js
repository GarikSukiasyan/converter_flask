function updateNumConvert() {
// Создаем новый объект XMLHttpRequest
var xhr2 = new XMLHttpRequest();


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
//console.log("Hello");
// Чтение печенек
var file_id = getCookie("id");
//console.log(username);



// Настраиваем обработчик события при успешном получении ответа от сервера
xhr2.onreadystatechange = function() {
    if (xhr2.readyState === 4 && xhr2.status === 200) {
//        console.log(xhr2.responseText);

        var response = JSON.parse(xhr2.responseText);

        const progressBar = document.querySelector('.progress-bar-inner');
        function updateProgressBar(value) {
            progressBar.style.width = value + '%';
        }
        // Пример использования функции updateProgressBar():
        updateProgressBar(response.progress); // установить прогресс-бар на 50%

        if (response.progress == 100) {
            var submitButton = document.getElementById('submitButton');
            var downloadLink = 'http://127.0.0.1:5000/static/output/' + file_id + '/output.mp4';

            submitButton.style.display = 'block'; // Показываем кнопку отправки
            submitButton.href = downloadLink;
        }

        //document.getElementById('num_file').innerHTML = 'Name: ' + response.name + ', Age: ' + response.age;
        //$('#num_file').text(response.name);
    }
};

// Открываем соединение с сервером с помощью метода GET
xhr2.open("GET", "/ffmpeg_start", true);

// Отправляем запрос на сервер
xhr2.send();
}

// Запускаем обновление каждую секунду
setInterval(updateNumConvert, 1000);
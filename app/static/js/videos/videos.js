// Проверяем загрузку файла
function checkFile() {
    var fileInput = document.getElementById('fileInput'); // Получаем элемент input
    var submitButton = document.getElementById('submitButton'); // Получаем кнопку отправки

    if (fileInput.files.length > 0) { // Проверяем, есть ли загруженный файл
        submitButton.style.display = 'block'; // Показываем кнопку отправки
    } else {
        submitButton.style.display = 'none'; // Скрываем кнопку отправки
    }
}




// Обновляем ProgressBar
function updateProgressBar() {
    // Создаем новый объект XMLHttpRequest
    var xhr2 = new XMLHttpRequest();

    // Настраиваем обработчик события при успешном получении ответа от сервера
    xhr2.onreadystatechange = function() {
        if (xhr2.readyState === 4 && xhr2.status === 200) {
            console.log(xhr2.responseText);

            var response = JSON.parse(xhr2.responseText);

            const progressBar = document.querySelector('.progress-bar-inner');
            function updateProgressBar(value) {
                progressBar.style.width = value + '%';
            }
            // Пример использования функции updateProgressBar():
            updateProgressBar(response.progress); // установить прогресс-бар на 50%
        }
    };

    // Открываем соединение с сервером с помощью метода GET
    xhr2.open("GET", "/progress", true);

    // Отправляем запрос на сервер
    xhr2.send();
}




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

// Чтение печенек
var file_id = getCookie("id");

if (file_id != "0"){
    var submitButton = document.getElementById('submitButton'); // Получаем кнопку отправки
    submitButton.style.display = 'none'; // Скрываем кнопку отправки

    // Запускаем обновление каждую секунду
    setInterval(updateProgressBar, 1000);
}
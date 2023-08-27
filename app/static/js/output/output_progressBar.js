function updateNumConvert() {
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

        //document.getElementById('num_file').innerHTML = 'Name: ' + response.name + ', Age: ' + response.age;
        //$('#num_file').text(response.name);
    }
};

// Открываем соединение с сервером с помощью метода GET
xhr2.open("GET", "/progress", true);

// Отправляем запрос на сервер
xhr2.send();
}

// Запускаем обновление каждую секунду
setInterval(updateNumConvert, 1000);
// Подключаемся к серверу ffmpeg_status , отправив наш id
// Если вернуло download True выводим все для скчивание
// Если вернуло download False и nameFile None - выдаем ошибку
// Если вернуло download False и nameFile Имя_Файла - обновляем прогресс бар

var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

// Обработчик события, когда приходит новое значение подсчета
socket.on('count_update', function(data) {
    $('#count').text(data.count);


socket.on('update_data', function (data) {
    console.log('Получено обновление:', data);
});


var json_data = JSON.parse('{{ json_data | tojson | safe }}');

// Делаем что-то с данными JSON
console.log(json_data);
// Например, получение значения "progress"
console.log(json_data.progress);

// Можно использовать данные JSON для динамического обновления элементов на странице
//var progressElement = document.getElementById('progress');
//progressElement.textContent = jsonData.progress;



//console.log(response);


//// Создаем объект XMLHttpRequest
//var xhr = new XMLHttpRequest();
//
//// Устанавливаем обработчик для события завершения запроса
//xhr.onreadystatechange = function() {
//    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
//        // Парсим JSON-ответ
//        var response = JSON.parse(xhr.responseText);
//        // Делаем что-то с ответом
//        console.log(response);
//    }
//};
//
//// Открываем GET-запрос
//xhr.open('GET', 'http://' + document.domain + ':' + location.port + '/ffmpeg_status/123', true);
//
//// Отправляем запрос
//xhr.send();







//$(document).ready(function() {
//    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
//
//    // Обработчик события, когда приходит новое значение подсчета
//    socket.on('count_update', function(data) {
//        $('#count').text(data.count);
//    });
//
//    socket.on('update_data', function(data) {
//        console.log('Получено обновление:', data);
//    });
//});
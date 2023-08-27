function checkFile() {
    var fileInput = document.getElementById('fileInput'); // Получаем элемент input
    var submitButton = document.getElementById('submitButton'); // Получаем кнопку отправки

    if (fileInput.files.length > 0) { // Проверяем, есть ли загруженный файл
        submitButton.style.display = 'block'; // Показываем кнопку отправки
    } else {
        submitButton.style.display = 'none'; // Скрываем кнопку отправки
    }
}
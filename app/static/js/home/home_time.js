window.onload = function() {
    var targetDate = new Date("2022/01/01"); // Укажите желаемую дату здесь

    function updateTimer() {
        // Указываем дату, от которой нужно считать время
        var specifiedDate = new Date('2023-08-21T00:00:00');

        // Получаем текущую дату и время
        var currentDate = new Date();

        // Разница между указанной датой и текущей датой в миллисекундах
        var timeDiff = currentDate - specifiedDate;

        // Количество миллисекунд в одной минуте, часе, дне и месяце
        var millisecondInMinute = 1000 * 60;
        var millisecondInHour = millisecondInMinute * 60;
        var millisecondInDay = millisecondInHour * 24;
        var millisecondInMonth = millisecondInDay * 30;

        // Вычисляем количество месяцев, дней, часов, минут и секунд
        var months = Math.floor(timeDiff / millisecondInMonth);
        var days = Math.floor((timeDiff % millisecondInMonth) / millisecondInDay);
        var hours = Math.floor((timeDiff % millisecondInDay) / millisecondInHour);
        var minutes = Math.floor((timeDiff % millisecondInHour) / millisecondInMinute);
        var seconds = Math.floor((timeDiff % millisecondInMinute) / 1000);

        // Выводим результат на страницу
        var result = document.getElementById('result');
        result.innerHTML = '0000-' + months + '-' + days + '-' + hours + ':' + minutes + ':' + seconds;
        }

    // Запускаем обновление каждую секунду
    setInterval(updateTimer, 1000);
    };
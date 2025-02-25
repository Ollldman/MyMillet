document.addEventListener('DOMContentLoaded', function() {
    // Находим сообщения
    const successMessage = document.querySelector('#successMessage');
    const errorMessage = document.querySelector('#errorMessage');

    // Функция для скрытия сообщения
    function hideMessage(element) {
        if (element) {
            element.style.display = 'none';
        }
    }

    // Показываем и скрываем successMessage
    if (successMessage) {
        successMessage.style.display = 'block'; // Показываем сообщение
        setTimeout(() => hideMessage(successMessage), 1000); // Скрываем через 400 мс
    }

    // Показываем и скрываем errorMessage
    if (errorMessage) {
        errorMessage.style.display = 'block'; // Показываем сообщение
        setTimeout(() => hideMessage(errorMessage), 1000); // Скрываем через 400 мс
    }
});
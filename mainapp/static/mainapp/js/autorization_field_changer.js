document.addEventListener('DOMContentLoaded', function() {
    const signInButton = document.getElementById('signInB');
    const authField = document.getElementById('modalAuth');
    const closeButton = document.querySelector('.close');

    signInButton.addEventListener('click', function(event) {
        event.preventDefault();
        
        // Показываем поле авторизации
        authField.style.display = 'block';
        
        // Центрируем поле авторизации
        authField.style.position = 'fixed';
        authField.style.top = '50%';
        authField.style.left = '50%';
        authField.style.transform = 'translate(-50%, -50%)';
        
        // Добавляем затемнение фона
        document.body.style.backgroundColor = 'rgba(0,0,0,0.5)';
    });

    // Закрытие модального окна при клике вне его
    closeButton.addEventListener('click', function(event) {
            authField.style.display = 'none';
            document.body.style.backgroundColor = '#FFF6EA';
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.getElementById('menuB');
    const MenuBlock = document.getElementById('menuBlock');

    menuButton.addEventListener('click', function(event) {
        event.preventDefault();
        
        // Показываем поле авторизации
        MenuBlock.style.display = 'block';
        
        // Центрируем поле авторизации
        MenuBlock.style.position = 'fixed';
        MenuBlock.style.top = '50%';
        MenuBlock.style.left = '50%';
        MenuBlock.style.transform = 'translate(-50%, -50%)';
        MenuBlock.style.height = 'auto';
        MenuBlock.style.width = '300px';
        
        // Добавляем затемнение фона
        document.body.style.backgroundColor = 'rgba(0,0,0,0.5)';
    });

    // Закрытие модального окна при клике вне его
    window.addEventListener('click', function(event) {
        if (event.target == authField) {
            MenuBlock.style.display = 'none';
            document.body.style.backgroundColor = '';
        }
    });
});
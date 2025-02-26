document.addEventListener('DOMContentLoaded', function() {
    const productCards = document.querySelectorAll('.product-card');

    productCards.forEach(card => {
        const addToCartButton = card.querySelector('.add_to_cart');
        const quantityInput = card.querySelector('.quantity_input');
        const minusButton = card.querySelector('.minus');
        const plusButton = card.querySelector('.plus');
        const quantitySpan = card.querySelector('.quantity');
        const notification = card.querySelector('#notification');
        const stockQuantity = parseInt(quantitySpan.getAttribute('data-stock'));
        const goToCartButton = card.querySelector('.go_to_cart');
        const productId = goToCartButton.getAttribute('data-product-id');

        let quantity = 1;

        addToCartButton.addEventListener('click', function() {
            quantitySpan.textContent = quantity;
            quantityInput.style.display = 'flex';
            this.style.display = 'none';
            card.classList.add('added');
        });

        minusButton.addEventListener('click', function() {
            if (quantity > 1) {
                quantity--;
                quantitySpan.textContent = quantity;
            } else if (quantity === 1) {
                quantity = 1;
                quantitySpan.textContent = quantity;
                quantityInput.style.display = 'none';
                addToCartButton.style.display = 'block'; 
                card.classList.remove('added');
            }
        });

        plusButton.addEventListener('click', function() {
            if (quantity < stockQuantity)
            {
                quantity++;
                quantitySpan.textContent = quantity;
            }
            else
            {
                notification.textContent = 'Max Value';
                notification.style.display = 'block';
                setTimeout(() => {
                    notification.style.display = 'none';
                }, 400);
            }
        });

        goToCartButton.addEventListener('click', function(){
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const quantity = quantitySpan.textContent;
            console.log("Добавлен товар ID:", productId);
            fetch("/cart/add_to_cart/", {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: `product_id=${productId}&quantity=${quantity}`
            })
            .then(response => response.json())
            .then(data => {
                const cartCount = document.getElementById('cart-count');
                if (cartCount){
                    cartCount.textContent = data.total_positions
                }
                if (data.success) {
                    alert('Товар добавлен в корзину');
                } else {
                    alert('Ошибка: ' + data.error);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});
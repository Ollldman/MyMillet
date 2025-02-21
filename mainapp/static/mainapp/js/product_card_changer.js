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
    });

});
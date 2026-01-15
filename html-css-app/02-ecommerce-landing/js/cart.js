let cart = [];
let cartCount = 0;

function addToCart(product) {
    cart.push(product);
    cartCount++;
    updateCartDisplay();
    console.log('Added to cart:', product);
}

function updateCartDisplay() {
    document.getElementById('cart-count').textContent = cartCount;
}

function calculateTotal() {
    return cart.reduce((total, item) => total + item.price, 0);
}

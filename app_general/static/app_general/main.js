console.log('จันทร์ไรเดอร์');

// Site header
const siteHeaderToggleMenuButton = document.querySelector('.site-header-toggle-menu-button');
const siteHeaderMenu = document.querySelector('.site-header-menu');
siteHeaderToggleMenuButton.addEventListener('click', () => {
  siteHeaderMenu.classList.toggle('is-active')
});

// Subscription form
const subscriptionForm = document.querySelector('.subscription-form');

function foodSetValidation(event) {
  const checkedFoodSet = document.querySelectorAll('input[name="food_set"]:checked');
  if (checkedFoodSet.length === 0) {
    event.preventDefault();
    alert('กรุณาเลือกเมนูอย่างน้อย 1 เมนู');
  }
}

if (!!subscriptionForm) {
  subscriptionForm.addEventListener('submit', foodSetValidation);
}

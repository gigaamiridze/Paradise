const burgerMenu = document.querySelector('.burger-menu');
const sidebar = document.querySelector('.sidebar');
const header = document.querySelector('header');
const pageContent = document.querySelector('.page-content');
const container = document.querySelectorAll('.container');

burgerMenu.addEventListener('click', (item) => {
  sidebar.classList.toggle('active');
  header.classList.toggle('less-padd');
  pageContent.classList.toggle('less-padd');
  for (let item of container) {
    item.classList.toggle('more-width');
  }
})
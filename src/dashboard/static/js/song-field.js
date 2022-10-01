// Song file field functionality
const realFileBtn = document.querySelector('.real-file');
const customBtn = document.querySelector('.custom-btn');
const customTxt = document.querySelector('.custom-txt');

customBtn.addEventListener('click', () => {
  realFileBtn.click();
})

realFileBtn.addEventListener('change', () => {
  if (realFileBtn.value) {
    customTxt.innerHTML = realFileBtn.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/);
  } else {
    customTxt.innerHTML = "No file chosen, yet";
  }
})
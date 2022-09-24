// Questions
const artistQuestion = document.querySelector('.artist-question');
const listenerQuestion = document.querySelector('.listener-question');

// Modals
const artistModal = document.querySelector('.artist-modal');
const listenerModal = document.querySelector('.listener-modal');

// Artist's question functionality
artistQuestion.addEventListener('mouseover', () => {
  artistModal.style.display = 'block';
})

artistQuestion.addEventListener('mouseout', () => {
  artistModal.style.display = 'none';
})

// Listener's question functionality
listenerQuestion.addEventListener('mouseover', () => {
  listenerModal.style.display = 'block';
})

listenerQuestion.addEventListener('mouseout', () => {
  listenerModal.style.display = 'none';
})
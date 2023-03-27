// Get all parent-comment-buttons and forms
const parentCommentButtons = document.querySelectorAll('.parent-comment-button');
const parentCommentForms = document.querySelectorAll('.form_parent');

// Add a click event listener to each parent-comment-button
parentCommentButtons.forEach((button, index) => {
  button.addEventListener('click', () => {
    // Toggle the display of the corresponding form
    parentCommentForms[index].style.display = parentCommentForms[index].style.display === 'none' ? 'block' : 'none';
  });
});
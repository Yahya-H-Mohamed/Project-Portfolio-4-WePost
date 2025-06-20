/**
 * @jest-environment jsdom
 */

beforeEach(() => {
  document.body.innerHTML = `
    <form id="commentForm"></form>
    <textarea id="id_content"></textarea>
    <button id="submitButton"></button>
    <div id="comment1">Test comment 1</div>
    <button class="btn-edit" comment_id="1"></button>
    <button class="btn-delete" comment_id="1"></button>
    <a id="deleteConfirm"></a>
    <div id="deleteModal"></div>
  `;

  // Mock Bootstrap Modal
  window.bootstrap = {
    Modal: jest.fn().mockImplementation(() => ({
      show: jest.fn(),
    })),
  };

  require('./comments.js'); 
});

test('Clicking edit button populates form and changes submit button', () => {
  // Simulate clicking the edit button
  document.querySelector('.btn-edit').click();

  // Expect the textarea is populated
  expect(document.getElementById('id_content').value).toBe('Test comment 1');
  // Expect the submit button text is changed
  expect(document.getElementById('submitButton').innerText).toBe('Update');
  // Expect the form action is set correctly
  expect(document.getElementById('commentForm').getAttribute('action')).toBe('edit_comment/1');
});

test('Clicking edit button populates form and changes submit button', () => {
  // Simulate clicking the edit button
  document.querySelector('.btn-edit').click();

  // Expect the textarea is populated
  expect(document.getElementById('id_content').value).toBe('Test comment 1');
  // Expect the submit button text is changed
  expect(document.getElementById('submitButton').innerText).toBe('Update');
  // Expect the form action is set correctly
  expect(document.getElementById('commentForm').getAttribute('action')).toBe('edit_comment/1');
});
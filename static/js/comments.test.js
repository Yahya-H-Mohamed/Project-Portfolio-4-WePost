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
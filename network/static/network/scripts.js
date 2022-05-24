// https://docs.djangoproject.com/en/4.0/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// ***** like button *****
document.querySelectorAll('[data-like-form]').forEach(form => {
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    fetch("/post/reaction", {
      method: 'POST',
      headers: {'X-CSRFToken': this.csrfmiddlewaretoken.value},
      body: JSON.stringify({
        post: Number(this.post.value),
        type: this.type.value,
        action: this.action.value
      })
    })
    .then(r => console.log(r))
    .catch(e => console.error(e));
  
    let postId = this.dataset.likeForm;
    let likeBtn = document.querySelector('[data-like-btn="' + postId + '"]');
    let counter = document.querySelector('[data-like-count="' + postId + '"]');
    
    if (this.action.value === 'add') {
      counter.innerText = Number(counter.innerText) + 1;
      likeBtn.classList.add('liked');
      likeBtn.value = 'remove';
    } else if (this.action.value === 'remove') {
      counter.innerText = Number(counter.innerText) - 1;
      likeBtn.classList.remove('liked');
      likeBtn.value = 'add';
    }
  })
})


// ***** add posts *****
if (document.querySelector('[data-add-post-form]')) {
  const addForm = document.querySelector('[data-add-post-form]');
  const addContent = document.querySelector('[data-add-post-content]');

  addForm.addEventListener('submit', (event) => {
    event.preventDefault();

    fetch('/post/add', {
      method: 'POST',
      headers: {'X-CSRFToken': csrftoken},
      body: JSON.stringify({
        content: addContent.value
      })
    })
    .then(r => {
      console.log(r);
      if (r.ok) {
        addContent.value = '';
        history.go(0);
      } else {
        window.alert('Failed to create post')
      }
    })
    .catch(e => {
      console.error(e);
      window.alert('Failed to create post')
    });
  })
}


// ***** edit posts *****
if (document.querySelector('[data-post-edit-btn]')) {
  const postContent = document.querySelector('[data-post-content]');
  const editBtn = document.querySelector('[data-post-edit-btn]');
  const editForm = document.querySelector('[data-post-edit-form]');
  const editInput = document.querySelector('[data-post-edit-input]');
  const postId = document.querySelector('[data-post-edit-form]').dataset.postEditForm;

  function toggleEfitForm() {
    if (editForm.style.display == 'none') {
      postContent.style.display = 'none';
      editForm.style.display = 'block';
      editBtn.innerText = 'Back';
    } else {
      postContent.style.display = 'block';
      editForm.style.display = 'none';
      editBtn.innerText = 'Edit';
    }
  }
  toggleEfitForm();
  editBtn.addEventListener('click', toggleEfitForm);

  editForm.addEventListener('submit', (event) => {
    event.preventDefault()
  
    editBtn.disabled = true;

    fetch('/post/edit', {
      method: 'POST',
      headers: {'X-CSRFToken': csrftoken},
      body: JSON.stringify({
        post: Number(postId),
        content: editInput.value
      })
    })
    .then(r => {
      console.log(r);
      if (r.ok) {
        postContent.innerText = editInput.value;
        toggleEfitForm();
      } else {
        editInput.value = postContent.innerText;
      }
      editBtn.disabled = false
    })
    .catch(e => {
      console.error(e);
      editInput.value = postContent.innerText;
      editBtn.disabled = false
    });
  
  });
}


// ***** add comment *****
if (document.querySelector('[data-comment-form]')) {
  const commentForm = document.querySelector('[data-comment-form]');

  commentForm.addEventListener('submit', (event) => {
    event.preventDefault();

    fetch('/post/comment', {
      method: 'POST',
      headers: {'X-CSRFToken': csrftoken},
      body: JSON.stringify({
        post: Number(commentForm.post.value),
        content: commentForm.content.value
      })
    })
    .then(r => {
      console.log(r);
      if (r.ok) {
        commentForm.content.value = '';
        history.go(0);
      } else {
        window.alert('Failed to create comment')
      }
    })
    .catch(e => {
      console.error(e);
      window.alert('Failed to create comment')
    });    
  })
}


// ***** follow user *****
if (document.querySelector('[data-follow-form]')) {
  const followForm = document.querySelector('[data-follow-form]');

  followForm.addEventListener('submit', (event) => {
    event.preventDefault();

    fetch('/user/follow', {
      method: 'POST',
      headers: {'X-CSRFToken': csrftoken},
      body: JSON.stringify({
        user: Number(followForm.user.value),
        follow: followForm.follow.value
      })
    })
    .then(r => {
      console.log(r);
      if (r.ok) {
        history.go(0);
      } else {
        window.alert('Failed to update follow status')
      }
    })
    .catch(e => {
      console.error(e);
      window.alert('Failed to update follow status')
    });

  })
}

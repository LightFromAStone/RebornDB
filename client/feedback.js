const DEFAULT_PATH = 'http://localhost:8765'

function showFeedback() {
   axios.get(`${DEFAULT_PATH}/feedback`)
   .then(res => {
      let fbSection = document.getElementById('all-feedback');
      for (let i = 0; i < res.data.length; i++) {
         let {feedback_name, feedback_content} = res.data[i];
         let fbCard = document.createElement('div');
         fbCard.className = 'feedback-card'
         fbCard.innerHTML = `<h4 class='fb-name'>${feedback_name}</h4><p class='fb-content'>${feedback_content}</p>`;
         fbSection.appendChild(fbCard);
      }
   })
   .catch(err => console.log(err));
   console.log('feedback loading');
}

function submitFeedback(event) {
   event.preventDefault();
   let submitName = document.getElementById('feedback-name').value;
   submitName.trim();
   if (submitName === '') { submitName = 'anonymous'; }

   let submitContent = document.getElementById('feedback-content').value;
   submitContent.trim();
   if (submitContent === '') { alert('Feedback cannot be blank!'); return; }
   else if (submitContent.length > 2000) { alert('Feedback cannot be longer than 2000 characters'); return; }

   axios.post(`${DEFAULT_PATH}/feedback`, {name: submitName, content: submitContent})
   .then(() => showFeedback())
   .catch(err => console.log(err));

   document.getElementById('feedback-name').value = '';
   document.getElementById('feedback-content').value = '';
}


let feebackForm = document.getElementById('feedback-form');
feebackForm.addEventListener('submit', submitFeedback);

showFeedback();
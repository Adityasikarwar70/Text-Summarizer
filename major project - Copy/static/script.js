const fileInput = document.querySelector('#uploadBtn');
const preview = document.getElementById('textarea');

fileInput.addEventListener('change', () => {
// This function runs when file is selected

    const fr = new FileReader(); 
    // Creates new FileReader instance

    fr.readAsText(fileInput.files[0]);
    // Reads user-selected file (other reading methods possible)
    
    fr.addEventListener('load', () => {
        // This function runs when reading is complete
        preview.textContent = fr.result;
        
    })

});

const msg = document.querySelector('#textarea')

const PASTE = document.querySelector('#paste')
PASTE.addEventListener('click', async()=> {
    let messageValue = msg.value;
    navigator.clipboard.readText().then(clipText =>{
        const add= `${messageValue + " " + clipText}`.toString();
        msg.value = add;
    })
})
const autorizationForm = document.getElementById('modalAuth');
const signInButton = document.getElementById('signInB');

signInButton.onclick = function(event)
{
    event.preventDefault();
    this.autorizationForm.style.display = "block";
}

window.onclick = function(event)
{
    if (event.target == autorizationForm)
    {
        autorizationForm.style.display = "none"
    }
}
const content = document.getElementById('content');
const display = document.getElementById('latex');
display.innerText = content.getAttribute('placeholder');

MathJax.typeset([display]);

content.addEventListener('input', () => {
    display.innerText = content.value;
    MathJax.typeset([display]);

    var contentChg = document.getElementById('content').value;
    if (contentChg === '') {
        display.innerText = content.getAttribute('placeholder');
        MathJax.typeset([display]);
    }
});

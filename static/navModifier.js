function navController() {
    const navEls = document.querySelectorAll('#nav a');
    const mainElHash = nav.children.item(0).hash;
    const divEls = document.querySelectorAll('.main');

    const activate = (hash) => {
        const selector = `a[href="${hash}"]`;
        target = document.querySelector(selector);
        navEls.forEach((navEl) => (navEl.className = ''));
        target.className = 'active';
    };

    navEls.forEach((navEl) => {
        navEl.addEventListener('click', (e) => {
            hash = navEl.getAttribute('href');
            activate(hash);

            divEls.forEach((div) => {
                div.style.display = 'none';
            });
            if (hash == '#main') {
                const content = document.getElementById('main');
                content.style.display = '';
            } else if (hash == '#addNotes') {
                const content = document.getElementById('AddNotes');
                content.style.display = '';
            } else if (hash == '#viewNotes') {
                const content = document.getElementById('ViewNotes');
                content.style.display = '';
            } else if (hash == '#commingUp') {
                const content = document.getElementById('CommingUp');
                content.style.display = '';
            } else if (hash == '#quiz') {
                const content = document.getElementById('Quiz');
                content.style.display = '';
            } else {
                divEls.forEach((div) => {
                    div.style.display = '';
                });
            }
        });
    });

    // activate main by default
    activate(mainElHash);
    divEls.forEach((div) => {
        div.style.display = 'none';
    });
    const content = document.getElementById('main');
    content.style.display = '';
}

navController();

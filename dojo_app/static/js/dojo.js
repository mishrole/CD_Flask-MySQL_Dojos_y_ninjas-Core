'use strict';

const formNewDojo = document.querySelector('#formDojo');
const dojoName = document.querySelector('#dojoName');

formNewDojo.addEventListener('submit', (e) => {
    const inputs = [dojoName];
    Validate(inputs);

    const totalValid = Array.from(document.querySelectorAll('.valid-feedback')).length;

    if (totalValid === inputs.length) {
        return true;
    } else {
        e.preventDefault();
    }
});
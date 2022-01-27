'use strict';

const formNewNinja = document.querySelector('#formNinja');
const ninjaFirstname = document.querySelector('#firstname');
const ninjaLastname = document.querySelector('#lastname');
const ninjaAge = document.querySelector('#age');
const ninjaDojo = document.querySelector('#dojo');

formNewNinja.addEventListener('submit', (e) => {
    const inputs = [ninjaFirstname, ninjaLastname, ninjaAge, ninjaDojo];
    Validate(inputs);
    
    const totalValid = Array.from(document.querySelectorAll('.valid-feedback')).length;

    if (totalValid === inputs.length) {
        return true;
    } else {
        e.preventDefault();
    }
});
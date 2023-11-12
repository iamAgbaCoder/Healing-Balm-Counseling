// Function to validate the form step and display error messages
function validateStep(step) {
    const errorMessage = step.querySelector('.error-message');
    errorMessage.textContent = ''; // Clear any previous error messages

    const inputs = step.querySelectorAll('input, select');
    let isValid = true;

    for (const input of inputs) {
        if (input.type === 'radio' || input.type === 'checkbox') {
            const inputName = input.name;
            const checkedInput = step.querySelector(`input[name="${inputName}"]:checked`);
            if (!checkedInput) {
                errorMessage.textContent = 'Please select an option for each question.';
                isValid = false;
                break;
            }
        } else if (input.value === '' || input.value === 'select age' || input.value === 'select country') {
            errorMessage.textContent = 'Please fill out all fields.';
            isValid = false;
            break;
        }
    }

    return isValid;
}

// Function to handle "Next" button click
function handleNextButtonClick(event) {
    event.preventDefault();
    const currentStep = event.target.closest('.form-step');
    const errorMessage = currentStep.querySelector('.error-message');

    if (validateStep(currentStep)) {
        errorMessage.textContent = ''; // Clear any previous error messages
        const nextStep = currentStep.nextElementSibling;
        if (nextStep) {
            currentStep.classList.remove('form-step-active');
            nextStep.classList.add('form-step-active');
        }
    }
}

// Function to handle "Previous" button click
function handlePrevButtonClick(event) {
    event.preventDefault();
    const currentStep = event.target.closest('.form-step');
    const prevStep = currentStep.previousElementSibling;
    if (prevStep) {
        currentStep.classList.remove('form-step-active');
        prevStep.classList.add('form-step-active');
    }
}

// Get all "Next" buttons and attach event listeners
const nextButtons = document.querySelectorAll('.btn-next');
nextButtons.forEach(button => {
    button.addEventListener('click', handleNextButtonClick);
});

// Get all "Previous" buttons and attach event listeners
const prevButtons = document.querySelectorAll('.btn-prev');
prevButtons.forEach(button => {
    button.addEventListener('click', handlePrevButtonClick);
});

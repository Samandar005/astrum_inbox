// Add auto-focus to next input field
const otpInputs = document.querySelectorAll('input[type="text"]');
otpInputs.forEach((input, index) => {
    input.addEventListener('input', (e) => {
        if (e.target.value.length === 1 && index < otpInputs.length - 1) {
            otpInputs[index + 1].focus();
        }
    });
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Backspace' && index > 0 && input.value.length === 0) {
            otpInputs[index - 1].focus();
        }
    });
});
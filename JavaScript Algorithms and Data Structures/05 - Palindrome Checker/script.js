const input = document.getElementById("text-input");
const button = document.getElementById("check-btn");
const result = document.getElementById("result");

const checkInput = () => {
  const textInput = input.value;
  let updatedTextInput = textInput.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');
  let textLength = updatedTextInput.length;

  if (!updatedTextInput) {
    alert("Please input a value");
  } else if (textLength === 1) {
    return result.innerHTML = (`<span id="text">${textInput}</span> is a palindrome`);
  } else {
    for (let i = 0; i < textLength / 2; i++) {
      if (updatedTextInput[i] !== updatedTextInput[textLength - 1 - i]) {
        return result.innerHTML = (`<span id="text">${textInput}</span> is not a palindrome`);
      }
    }
    return result.innerHTML = (`<span id="text">${textInput}</span> is a palindrome`);
      
    } 
};

button.addEventListener("click", checkInput);
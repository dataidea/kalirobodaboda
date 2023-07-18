const form = document.querySelector("form");
const labels = document.querySelectorAll("label");
const inputs = document.querySelectorAll("input");
inputs.forEach((input) => {
  input.classList.add("border", "rounded", "p-2", "block", "w-full");
});

labels.forEach((label) => {
  label.classList.add("py-3");
});

form.first_name.placeholder = "John";
form.last_name.placeholder = "Doe";
form.email.placeholder = "johndoe@gmail.com";
form.gender.classList.add("p-2");
